import discord
import json

client = discord.Client()

# graph bot is going to respond to the messages that start with .
# so stuff like .info, .graphs gold

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.info'):
        await message.channel.send('Something informational...')

client.run()