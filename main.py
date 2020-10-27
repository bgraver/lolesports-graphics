import esports_lib as esports
import graphs
import datetime
import pprint
import os
# from bot import leagues_codes

# window = esports.getFullGameWindow('104841804589544576', '2020-10-18T10:00:00Z')

# leagues = esports.getLeagues()
# pprint.pprint(leagues)

# tournament = esports.getTournamentFromLeague('98767991299243165')
# pprint.pprint(tournament)

# start_dates = [datetime.datetime.strptime(date['startDate'], "%Y-%m-%d") for date in tournament['data']['leagues'][0]['tournaments']]
# pprint.pprint(sorted(start_dates, reverse=True)[0])

# schedule = esports.getSchedule('98767975604431411')
# pprint.pprint(schedule)

# graphs.kpBar(window)
# graphs.teamGoldLine(window)
# graphs.playerGoldLine(window)

'''
def generateATournament(tournamentId):
'''

def generateGraphFileStructure():
    # starting in the root
    # making the top level 'graphs' folder
    path = os.getcwd()
    g = 'graphs'
    path = os.path.join(path, g)
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    os.chdir(path)
    # generating a list of leagues
    leagues = esports.getLeagues()['data']['leagues']
    for league in leagues:
        name = "{0}/{1}".format(path, league['name'])
        if os.path.isdir(name):
            pass
        else:
            print(name)
            os.mkdir(name)
        tournaments = esports.getTournamentFromLeague(league['id'])['data']['leagues'][0]['tournaments']
        for tournament in tournaments:
            tourney_name = "{0}/{1}".format(name, tournament['slug'])
            if os.path.isdir(tourney_name):
                pass
            else:
                os.mkdir(tourney_name)
            events = esports.getCompletedEvents(tournament['id'])['data']['schedule']['events']
            '''
             for event in events:
                event_name = "{0}/{1}".format(tourney_name, event['blockName'])
                if os.path.isdir(event_name):
                    pass
                else:
                    print(event_name)
                    os.mkdir(event_name)
            '''

        # print("---")
    # work through each league and generate the tournament folders


generateGraphFileStructure()

# events = esports.getCompletedEvents('104174992692075107')
# pprint.pprint(events['data']['schedule']['events'])
