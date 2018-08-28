import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os


        

 @client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="Create a ticket for help!!"))            
            
            

client.run(os.getenv('TOKEN'))           
            
                       
