import boto3
import esports_lib as esports
import pprint
import time
import pandas as pd
import psycopg2

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


# we've sunset rds something something can't be public serverless
def connect_to_rds(endpoint, port, user, password, database):
    connection = psycopg2.connect(
        host=endpoint,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection


def get_unique_player_ids():
    teams = esports.getAllTeams()
    _p = []
    for team in teams:
        players = team.pop('players')
        for player in players:
            player['currentTeam'] = team['code']
            _p.append(player)

    unique_p = []
    seen = set()
    for player in _p:
        _id = player['id']
        if _id not in seen:
            seen.add(_id)
            unique_p.append(player)
    return unique_p


def insert_static_data():
    _league = dynamodb.Table('leagues')
    _tournament = dynamodb.Table('tournaments')
    _teams = dynamodb.Table('teams')
    _players = dynamodb.Table('players_static')

    unique_players = get_unique_player_ids()
    with _players.batch_writer() as batch:
        for p in unique_players:
            batch.put_item(p)

    leagues = esports.getLeagues()
    with _league.batch_writer() as batch:
        for league in leagues['data']['leagues']:
            batch.put_item(league)

    with _tournament.batch_writer() as batch:
        for league in leagues['data']['leagues']:
            tournaments = esports.getTournamentFromLeague(league['id'])
            for tournament in tournaments['data']['leagues'][0]['tournaments']:
                batch.put_item(tournament)

    with _teams.batch_writer() as batch:
        teams = esports.getAllTeams()
        for team in teams:
            if team['homeLeague'] is not None:
                team['league'] = team['homeLeague']['name']
            else:
                team['league'] = team['homeLeague']
            team.pop('homeLeague')
            team.pop('players')
            batch.put_item(team)


def load_complete_games():
    leagues = esports.getLeagues()
    _tournaments = []
    _completed_events = []
    for league in leagues['data']['leagues']:
        tournaments = esports.getTournamentFromLeague(league['id'])
        most_recent_tournament = sorted(tournaments['data']['leagues'][0]['tournaments'], key=lambda tournament: tournament['startDate'], reverse=True)[0]
        start_date = time.strptime(most_recent_tournament['startDate'], "%Y-%m-%d")
        new_year_date = time.strptime("01/01/2021", "%d/%m/%Y")
        if start_date > new_year_date:
            _tournaments.append(most_recent_tournament['id'])
    for tournament in _tournaments:
        completed_event = esports.getCompletedEvents(tournament)
        for event in completed_event['data']['schedule']['events']:
            _event = {'blockName': event['blockName'], 'id': event['games'][0]['id'],
                      'leagueName': event['league']['name'], 'startTime': event['startTime'],
                      'matchId': event['match']['id']}
            _completed_events.append(_event)
    return _completed_events


def load_games_to_ddb():
    _events = dynamodb.Table("events")
    completed_events = load_complete_games()

    with _events.batch_writer() as batch:
        for event in completed_events:
            batch.put_item(event)


def load_matches_to_ddb():
    _matches = dynamodb.Table("matches")
    completed_events = load_complete_games()
    for completed_event in completed_events:
        match = loading_matches(completed_event['matchId'])
        match['startTime'] = completed_event['startTime']
        with _matches.batch_writer() as batch:
            batch.put_item(match)


def loading_matches(match_id):
    event = esports.getEventDetails(match_id)
    event = event['data']['event']
    event['leagueId'] = event['league']['id']
    event.pop('league')
    event['bestOf'] = event['match']['strategy']['count']
    event['match'].pop('strategy')
    event['blueTeam'] = event['match']['teams'][0]['id']
    event['redTeam'] = event['match']['teams'][1]['id']
    event['blueWins'] = event['match']['teams'][0]['result']['gameWins']
    event['redWins'] = event['match']['teams'][1]['result']['gameWins']
    event['match'].pop('teams')
    game_id_string = ''
    for game in event['match']['games']:
        game_id_string += game['id'] +','
    event['gameIds'] = game_id_string[:-1]
    event.pop('match')
    event.pop('streams')
    event['tournamentId'] = event['tournament']['id']
    event.pop('tournament')
    return event


def set_post_game_stats(game_id, starting_time):
    game = esports.getFullGameWindow(game_id, starting_time)
    pprint.pprint(game)

set_post_game_stats('105522217233187996', '2021-01-23T21:00:00Z')

# window = esports.getWindow('105522217233187989', '2021-01-27T09:00:00Z')
# pprint.pprint(window.json())
