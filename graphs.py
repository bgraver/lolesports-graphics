import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def teamGoldLine(window, gameNumber=1):
    gold_data = {'blue': [], 'red': []}

    for frame in window['frames']:
        gold_data['blue'].append(frame['blueTeam']['totalGold'])
        gold_data['red'].append(frame['redTeam']['totalGold'])

    gold_df = pd.DataFrame(gold_data)
    gold_df['gold_diff'] = gold_df['blue'] - gold_df['red']

    plt.style.use('seaborn-poster')
    plt.style.use('ggplot')
    plot = sns.lineplot(data=gold_df['gold_diff'])
    plot.set(xlabel="frames", ylabel="gold", title="Team Gold Difference - {2} - {0} vs. {1} -Game {3}".format(window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], window['frames'][0]['rfc460Timestamp'].split("T")[0], gameNumber))
    size = gold_df['gold_diff'].count()
    plt.plot([0, size], [0, 0])

    plt.savefig('teamGoldGraph-{0}.png'.format(window['esportsGameId']))

    return plot


def playerGoldLine(window, gameNumber=1):
    # indiv gold graph over time
    player_gold = {
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName']: [],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][1]['summonerName']: [],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][2]['summonerName']: [],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][3]['summonerName']: [],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][4]['summonerName']: [],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName']: [],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][1]['summonerName']: [],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][2]['summonerName']: [],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][3]['summonerName']: [],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][4]['summonerName']: [],
    }

    for frame in window['frames']:
        player_gold[window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName']].append(
            frame['blueTeam']['participants'][0]['totalGold'])
        player_gold[window['gameMetadata']['blueTeamMetadata']['participantMetadata'][1]['summonerName']].append(
            frame['blueTeam']['participants'][1]['totalGold'])
        player_gold[window['gameMetadata']['blueTeamMetadata']['participantMetadata'][2]['summonerName']].append(
            frame['blueTeam']['participants'][2]['totalGold'])
        player_gold[window['gameMetadata']['blueTeamMetadata']['participantMetadata'][3]['summonerName']].append(
            frame['blueTeam']['participants'][3]['totalGold'])
        player_gold[window['gameMetadata']['blueTeamMetadata']['participantMetadata'][4]['summonerName']].append(
            frame['blueTeam']['participants'][4]['totalGold'])
        player_gold[window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName']].append(
            frame['redTeam']['participants'][0]['totalGold'])
        player_gold[window['gameMetadata']['redTeamMetadata']['participantMetadata'][1]['summonerName']].append(
            frame['redTeam']['participants'][1]['totalGold'])
        player_gold[window['gameMetadata']['redTeamMetadata']['participantMetadata'][2]['summonerName']].append(
            frame['redTeam']['participants'][2]['totalGold'])
        player_gold[window['gameMetadata']['redTeamMetadata']['participantMetadata'][3]['summonerName']].append(
            frame['redTeam']['participants'][3]['totalGold'])
        player_gold[window['gameMetadata']['redTeamMetadata']['participantMetadata'][4]['summonerName']].append(
            frame['redTeam']['participants'][4]['totalGold'])

    player_gold_df = pd.DataFrame(player_gold)

    plt.style.use('seaborn-poster')
    plt.style.use('ggplot')
    plot = sns.lineplot(data=player_gold_df, dashes=False)
    plot.set(xlabel="frames", ylabel="gold", title="Player Gold Difference - {2} - {0} vs. {1} - Game {3}".format(window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], window['frames'][0]['rfc460Timestamp'].split("T")[0], gameNumber))
    plt.savefig('playerGoldGraph-{0}.png'.format(window['esportsGameId']))
    return plot


def kpBar(window, gameNumber=1):
    last_frame = window['frames'][len(window['frames']) - 1]
    blue_kills = last_frame['blueTeam']['totalKills']
    red_kills = last_frame['redTeam']['totalKills']

    kp = {
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName']: [(last_frame['blueTeam'][
                                                                                                    'participants'][0][
                                                                                                    'kills'] +
                                                                                                last_frame['blueTeam'][
                                                                                                    'participants'][0][
                                                                                                    'assists']) / blue_kills],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][1]['summonerName']: [(last_frame['blueTeam'][
                                                                                                    'participants'][1][
                                                                                                    'kills'] +
                                                                                                last_frame['blueTeam'][
                                                                                                    'participants'][1][
                                                                                                    'assists']) / blue_kills],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][2]['summonerName']: [(last_frame['blueTeam'][
                                                                                                    'participants'][2][
                                                                                                    'kills'] +
                                                                                                last_frame['blueTeam'][
                                                                                                    'participants'][2][
                                                                                                    'assists']) / blue_kills],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][3]['summonerName']: [(last_frame['blueTeam'][
                                                                                                    'participants'][3][
                                                                                                    'kills'] +
                                                                                                last_frame['blueTeam'][
                                                                                                    'participants'][3][
                                                                                                    'assists']) / blue_kills],
        window['gameMetadata']['blueTeamMetadata']['participantMetadata'][4]['summonerName']: [(last_frame['blueTeam'][
                                                                                                    'participants'][4][
                                                                                                    'kills'] +
                                                                                                last_frame['blueTeam'][
                                                                                                    'participants'][4][
                                                                                                    'assists']) / blue_kills],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName']: [(last_frame['redTeam'][
                                                                                                   'participants'][0][
                                                                                                   'kills'] +
                                                                                               last_frame['redTeam'][
                                                                                                   'participants'][0][
                                                                                                   'assists']) / red_kills],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][1]['summonerName']: [(last_frame['redTeam'][
                                                                                                   'participants'][1][
                                                                                                   'kills'] +
                                                                                               last_frame['redTeam'][
                                                                                                   'participants'][1][
                                                                                                   'assists']) / red_kills],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][2]['summonerName']: [(last_frame['redTeam'][
                                                                                                   'participants'][2][
                                                                                                   'kills'] +
                                                                                               last_frame['redTeam'][
                                                                                                   'participants'][2][
                                                                                                   'assists']) / red_kills],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][3]['summonerName']: [(last_frame['redTeam'][
                                                                                                   'participants'][3][
                                                                                                   'kills'] +
                                                                                               last_frame['redTeam'][
                                                                                                   'participants'][3][
                                                                                                   'assists']) / red_kills],
        window['gameMetadata']['redTeamMetadata']['participantMetadata'][4]['summonerName']: [(last_frame['redTeam'][
                                                                                                   'participants'][4][
                                                                                                   'kills'] +
                                                                                               last_frame['redTeam'][
                                                                                                   'participants'][4][
                                                                                                   'assists']) / red_kills],
    }

    kp_df = pd.DataFrame(kp)

    plt.style.use('seaborn-poster')
    plt.style.use('ggplot')
    plot = sns.barplot(data=kp_df)
    plot.set(xlabel="Kill Participation", ylabel="% KP", title="Kill Participation - {0} - {1} vs. {2} - Game {3}".format(window['frames'][0]['rfc460Timestamp'].split("T")[0], window['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], window['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName'].split(" ")[0], gameNumber))
    plot.set_xticklabels(plot.get_xticklabels(), rotation=45, size=4)

    plt.savefig("KPGraph - {0}".format(window['esportsGameId']))

    return plot
