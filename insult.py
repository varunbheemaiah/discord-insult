from os import environ
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import requests
from textblob import TextBlob
import sys
from bot.helpers import *
TOKEN = sys.argv[1]

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected')

print("RUNNING")

@client.event
@commands.cooldown(1, 300, commands.BucketType.user)
async def on_message(message):
	if message.author.bot:
		return
	msg = message.content.strip()
	tts = True if ' ' in msg and "tts" in msg.split(" ") else False
	if msg.startswith('!'):

		if msg.startswith('!vb help'):
			embed = discord.Embed(title="VB Bot Help", color=0x2196F3)
			embed.description = botHelp
			
		elif msg.startswith('!darkjoke'):
			response = getDarkJoke(client, message)
		
		elif msg.startswith('!insult'):
			response = getInsult(client, message)
		
		elif msg.startswith('!joke'):
			response = getJoke(client, message)

		elif msg.startswith("!compliment"):
			response = getCompliment(client, message)

		else:
			# response = "Invalid Command. Please type '!insult help' for a list of commands"
			embed = discord.Embed(title="Invalid command. try one of these", color=0x2196F3)
			embed.description = botHelp
		await message.delete()
		try:
			newmessage = await message.channel.send(embed=embed)
			# await newmessage.delete(delay=10)
		except NameError:
			await message.channel.send(response, tts=tts)

	elif client.user in message.mentions:

		messageAnalysis = TextBlob(msg)
		sentimentValue = messageAnalysis.sentiment.polarity
		if sentimentValue > 0.5:
			response = random.choice(kissass).strip()
		else:
			await message.add_reaction('🇸')
			await message.add_reaction('🇹')
			await message.add_reaction('🇫')
			await message.add_reaction('🇺')
			response = random.choice(comebacks).strip()

		await message.channel.send("Hey "+str(message.author.mention)+", "+response) 

client.run(TOKEN)