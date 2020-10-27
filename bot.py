import discord
import json
import datetime
import esports_lib as esports

client = discord.Client()

leagues_codes = {
    'eum': '100695891328981122',
    'tal': '101097443346691685',
    'lla': '101382741235120470',
    'pcs': '104366947889790212',
    'worlds': '98767975604431411',
    'all-stars': '98767991295297326',
    'lcs': '98767991299243165',
    'lec': '98767991302996019',
    'lck': '98767991310872058',
    'lpl': '98767991314006698',
    'msi': '98767991325878492',
    'cblol': '98767991332355509',
    'tcl': '98767991343597634',
    'ljl': '98767991349978712',
    'lcsa': '99332500638116286'
}

with open('bot.keys') as f:
    keys = json.load(f)

# graph bot is going to respond to the messages that start with .
# so stuff like .info, .graphs gold


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # getting
    userInput = message.content.split()

    # .info
    if userInput[0] == '.info':
        await message.channel.send(
            "Commands are:\n"
            ".graphs [league] [blue team code] [red team code]"
        )

    # .graphs
    if userInput[0] == '.graphs':
        if len(userInput) != 4:
            await message.add_reaction(emoji='⛔')
        else:
            await create_graphs(message, userInput)


# .graphs
'''
args[1]: tournament (worlds, LCS, LEC, etc...)
args[2]: blue side,
args[3]: red side,
args[4]: game number
'''
async def create_graphs(message, args):
    await message.channel.send('TODO: args {0} {1} {2}'.format(args[1], args[2], args[3]))
    league = str(args[1]).lower()
    print(league)
    tournament = esports.getTournamentFromLeague(leagues_codes[league])
    start_dates = [datetime.datetime.strptime(date['startDate'], "%Y-%m-%d") for date in tournament['data']['leagues'][0]['tournaments']]
    tourney_date = sorted(start_dates, reverse=True)[0]

client.run(keys['clientToken'])
