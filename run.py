import discord
from discord.ext import commands
import random
import asyncio
import time
import os


Client = discord.Client()


         
                                      
@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="Message me for help!"))
        
        
        
                    


client.run(os.getenv('TOKEN'))
