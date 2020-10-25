import esports_lib as esports
import graphs
import pprint

headers = {'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}
params = {"hl": "en-US"}

window = esports.getFullGameWindow(headers, params, '104841804589544576', '2020-10-18T10:00:00Z')

leagues = esports.getLeagues(headers, params)
# print(leagues)
tournament = esports.getTournamentFromLeague(headers, params, '98767975604431411')
# print(tournament)
schedule = esports.getSchedule(headers, params, '98767975604431411')
# pprint.pprint(schedule)

# plot = graphs.teamGoldLine(window)
# plot = graphs.playerGoldLine(window)
# plot = graphs.kpBar(window)
