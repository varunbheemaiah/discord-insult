from os import environ
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
from textblob import TextBlob

TOKEN = environ['DISCORD']

client = discord.Client()


with open("static/insults.txt","r") as insultFile:
	insults = list(insultFile)

with open("static/comebacks.txt","r") as comebacksFile:
	comebacks = list(comebacksFile)

with open("static/kissass.txt","r") as kissassFile:
	kissass = list(kissassFile)

with open("static/compliments.txt",'r') as complimentsFile:
	compliments = list(complimentsFile)

def getInsult():
	return random.choice(insults).strip()

def getCompliment():
	return random.choice(compliments).strip()

@client.event
async def on_ready():
	print(f'{client.user} has connected')

# @client.event
# async def on_member_join(member):
#     response = "Welcome <@"+str(member.id)+">, "+getInsult()
#     for channel in member.guild.channels:
#         if channel.name == 'general':
#             await channel.send(response)

@client.event
@commands.cooldown(1, 300, commands.BucketType.user)
async def on_message(message):
	if message.author == client.user:
		return
	msg = message.content.strip()
	if msg.startswith('!'):
		if msg.startswith('!insult help'):
			response = '''
			Bot Commands: \n!insult: Insult a random person on the server\n!insult <name>: Insults person with name <name>.\n!insult me: Insults you\n!insult yourself: Insults itself
			'''
		elif msg.startswith('!insult'):
			insultToSend = getInsult()
			name = ''
			if ' ' in msg:
				name = msg.split()[1]
			if len(name)>0:
				if name != 'me':
					response = "Hey "+name+", "+insultToSend
				if name == 'me':
					response = "Hey <@"+str(message.author.id)+">, "+insultToSend
				if name == 'yourself':
					response = "Hey Insult Bot, "+insultToSend
			else:
				members = message.guild.members
				memberList = []
				for member in members:
					if not member.bot:
						memberList.append(member.id)
				person = random.choice(memberList)
				response = "Hey <@"+str(person)+">, "+insultToSend
		elif msg.startswith("!compliment"):
			complimentToSend = getCompliment()
			name = ''
			if ' ' in msg:
				name = msg.split()[1]
			if len(name)>0:
				if name != 'me':
					response = "Hey "+name+", "+complimentToSend
				if name == 'me':
					response = "Hey <@"+str(message.author.id)+">, "+complimentToSend
				if name == 'yourself':
					response = "Hey Insult Bot, "+complimentToSend
			else:
				members = message.guild.members
				memberList = []
				for member in members:
					if not member.bot:
						memberList.append(member.id)
				person = random.choice(memberList)
				response = "Hey <@"+str(person)+">, "+insultToSend
		else:
			response = "Invalid Command. Please type '!insult help' for a list of commands"
		await message.channel.send(response)
	elif client.user in message.mentions:
		messageAnalysis = TextBlob(msg)
		sentimentValue = messageAnalysis.sentiment.polarity
		if sentimentValue > 0.5:
			response = random.choice(kissass).strip()
		else:
			response = random.choice(comebacks).strip()
		await message.channel.send(response) 

client.run(TOKEN)