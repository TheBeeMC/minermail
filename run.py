import discord
import asyncio
import random
import requests
import io
import safygiphy

client = discord.Client()
g = safygiphy.Giphy()
DEIN_USERNAME = "DEINE_USER_ID"

minutes = 0
hour = 0

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    # await client.change_presence(game=discord.Game(name="on grewoss.com"))


@client.event
async def on_message(message):
    if message.content.lower().startswith('?test'):
        await client.send_message(message.channel, "Test bestanden")

    if message.content.lower().startswith('?coin'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    if message.content.startswith('?game') and message.author.id == DEIN_USERNAME:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Ich habe meinen Status zu {0} geaendert".format(game))

    if message.content.startswith('?bild'):
        response = requests.get("https://media3.giphy.com/media/6C9CMGMFtzzbO/giphy.gif", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='bild.gif', content='Test Bild.')

    if message.content.startswith('?uptime'):
        await client.send_message(message.channel, "`Ich bin schon {0} stunde/n und {1} minuten online auf {2}. `".format(hour, minutes, message.server))

    if message.content.startswith('?gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.startswith('?fun'):
        gif_tag = "fun"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')


@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "Willkommen {0} auf {1}".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)


@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "Bye Bye {0}".format(member.mention)
    await client.send_message(serverchannel, msg)


async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

 @client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="Create a ticket for help!!"))            
            
            
client.loop.create_task(tutorial_uptime())
client.run(os.getenv('TOKEN'))           
            
                       
