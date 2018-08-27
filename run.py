import asyncio
import configparser
import json
import random
import os
from subprocess import check_output, CalledProcessError
from sys import version_info

import discord



@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="Message me for help!"))
    
client.run(os.getenv('TOKEN'))
