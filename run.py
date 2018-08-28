import discord
from discord.ext import commands
import random
import asyncio
import time
import os

Client = discord.Client()
       
 @client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="Create a ticket for help!!"))            
            
            

client.run(os.getenv('TOKEN'))           
            
                       
