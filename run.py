import discord
from discord.ext import commands
import random
import asyncio
import time
import os


Client = discord.Client()

client = commands.Bot(command_prefix = "?")

chat_filter = ["Hi", "Hello"]
bypass_list = []

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.send_message(message.channel, "Hi, What is up? I am just a bot. If you have any questions pm me and it will be send to the owner's")
                except discord.errors.NotFound:
                    return
         
                
                                 
@client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="Maybe sleeping or just doing something else if not I am coding"))
        
        
        
                    



            
                       
