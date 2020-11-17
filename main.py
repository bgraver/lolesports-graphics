import esports_lib as esports
import graphs
import datetime
import pprint
import os
import json

# 3252 games total
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
            os.mkdir(name)
        tournaments = esports.getTournamentFromLeague(league['id'])['data']['leagues'][0]['tournaments']
        for tournament in tournaments:
            tourney_name = "{0}/{1}".format(name, tournament['slug'])
            if os.path.isdir(tourney_name):
                pass
            else:
                os.mkdir(tourney_name)
            events = esports.getCompletedEvents(tournament['id'])['data']['schedule']['events']
            for event in events:
                event_name = "{0}/{1}".format(tourney_name, event['blockName'])
                if os.path.isdir(event_name):
                    pass
                else:
                    print(event_name)
                    os.mkdir(event_name)
                matches = esports.getEventDetails(event['match']['id'])
                # for game in matches['data']['event']['match']['games']:

                    # enter the graphs you want to generate here


# generateGraphFileStructure()
# match = esports.getEventDetails('104174992730350834')['data']['event']['match']['games']
# pprint.pprint(match)

