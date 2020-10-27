# Scripts for importing the files
import requests
import datetime


headers = {'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}
params = {"hl": "en-US"}


def getLeagues():
    return requests.get('https://esports-api.lolesports.com/persisted/gw/getLeagues', params=params, headers=headers).json()


def getTournamentFromLeague(leagueId):
    params['leagueId'] = leagueId
    return requests.get('https://esports-api.lolesports.com/persisted/gw/getTournamentsForLeague', params=params, headers=headers).json()


def getStandings(tournamentId):
    params['tournamentId'] = tournamentId
    return requests.get('https://esports-api.lolesports.com/persisted/gw/getStandings', params=params, headers=headers).json()


def getSchedule(leagueId, pageToken=None):
    params['leagueId'] = leagueId
    if pageToken is not None:
        params['pageToken'] = pageToken
    return requests.get('https://esports-api.lolesports.com/persisted/gw/getSchedule', params=params, headers=headers).json()


# datetime format: 2020-09-25T12:43:00Z (YYYY-MM-dd'T'hh-mm-ss'Z')
def getWindow(gameId, startingTime=None):
    params['gameId'] = gameId
    if startingTime is not None:
        params['startingTime'] = startingTime
    else:
        params['startingTime'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    return requests.get("https://feed.lolesports.com/livestats/v1/window/{0}".format(gameId), params=params, headers=headers)


def getEventDetails(eventId):
    params['id'] = eventId
    return requests.get("https://esports-api.lolesports.com/persisted/gw/getEventDetails", params=params, headers=headers).json()


def getCompletedEvents(tournamentId):
    params['tournamentId'] = tournamentId
    return requests.get("https://esports-api.lolesports.com/persisted/gw/getCompletedEvents", params=params, headers=headers).json()

# datetime format: 2020-09-25T12:43:00Z (YYYY-MM-dd'T'hh-mm-ss'Z')
def getFullGameWindow(gameId, startingTime):
    master_window = {}
    window = getWindow(gameId, startingTime)
    start_date = datetime.datetime.strptime(startingTime, '%Y-%m-%dT%H:%M:%SZ')
    formatted_start = ''
    valid_start = False
    if window.status_code == 204:
        pass
        # print("not ok")
    elif window.status_code == 404:
        print("Not valid game")
        return None
    else:
        valid_start = True

    # games don't start exactly at the scheduled time
    while valid_start is not True:
        start_date += datetime.timedelta(seconds=10)
        formatted_date = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        window = getWindow(gameId, formatted_date)
        if window.status_code == 204:
            pass
        elif window.status_code == 400:
            break
        else:
            print("ok")
            valid_start = True
            formatted_start = formatted_date

    # storing variables in the master dict
    master_window['start_date'] = formatted_start
    master_window['esportsGameId'] = window.json()['esportsGameId']
    master_window['esportsMatchId'] = window.json()['esportsMatchId']
    master_window['gameMetadata'] = window.json()['gameMetadata']
    master_window['frames'] = window.json()['frames']

    current_time = start_date
    finished = False
    # iterating until you've reached the last frame
    while finished is False:
        current_time += datetime.timedelta(seconds=100)
        formatted_date = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        window = getWindow(gameId, formatted_date)
        for frame in window.json()['frames']:
            if frame['gameState'] == 'in_game':
                master_window['frames'].append(frame)
            elif frame['gameState'] == 'finished':
                master_window['frames'].append(frame)
                master_window['finished_time'] = frame['rfc460Timestamp']
                finished = True

    return master_window

