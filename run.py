import discord
from discord.ext import commands
import random
import asyncio
import time
import os


Client = discord.Client()

client = commands.Bot(command_prefix = "?")

chat_filter = ["FUCK", "CUNT", "BITCH", "DICK", "KYS", "FAGGOT", "FUCKING", "NIGGER", "NIGGA", "WHORE", "ASS", "KILL YOUR SELF", "IDIOT", "DUMBASS", "LOSER"]
bypass_list = []

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** Don't swear 😡 Thank you")
                except discord.errors.NotFound:
                    return
         
                
                                 
@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="& Mining ⛏"))
        
        
        
                    


client.run(os.getenv('TOKEN'))     
            
                       
