from os import environ
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import requests
from textblob import TextBlob
import sys

TOKEN = sys.argv[1]

client = discord.Client()



with open("static/insults.txt","r") as insultFile:
	insults = list(insultFile)

with open('static/shakespearean.txt', "r") as shakespeare:
	shakespeareInsults = list(shakespeare)

jokesFile = open('static/jokes.txt')
jokes = list(jokesFile)
jokesFile.close()

with open("static/comebacks.txt","r") as comebacksFile:
	comebacks = list(comebacksFile)

with open("static/kissass.txt","r") as kissassFile:
	kissass = list(kissassFile)

with open("static/compliments.txt",'r') as complimentsFile:
	compliments = list(complimentsFile)

def getInsult():
	return random.choice(insults).strip()

def getShakespeareanInsult():
	return random.choice(shakespeareInsults).strip()

def getCompliment():
	return random.choice(compliments).strip()

def getJoke():
	return random.choice(jokes).strip()

@client.event
async def on_ready():
	print(f'{client.user} has connected')

print("RUNNING")

# @client.event
# async def on_member_join(member):
#     response = "Welcome <@"+str(member.id)+">, "+getInsult()
#     for channel in member.guild.channels:
#         if channel.name == 'general':
#             await channel.send(response)

botHelp = '''Hey, i am an **interactive bot**. Feel free to enjoy the following commands.\n
**Bot Commands:** \n
**Insults**
- **!insult random**: Insult a random person on the server
- **!insult <name>**: Insults person with name <name>.
- **!insult me**: Insults you
- **!insult yourself**: Insults itself
You can add 'shakespearean' to any insult command to make the insult exotic\n

**Compliment**
- **!compliment**: Compliment a random person on the server
- **!compliment <name>**: Compliments person with name <name>.
- **!compliment me**: Compliments you
- **!compliment yourself**: Compliments itself\n

**Jokes**
- **!joke**: Cracks a joke
- **!darkjoke**: Cracks a dark joke\n
Optionally all commands accept a "tts" parameter at the end. this results in a text to speech insult'''

@client.event
@commands.cooldown(1, 300, commands.BucketType.user)
async def on_message(message):
	if message.author == client.user:
		return
	msg = message.content.strip()
	tts = True if ' ' in msg and "tts" in msg.split(" ") else False
	if msg.startswith('!'):

		if msg.startswith('!vb help'):
			embed = discord.Embed(title="VB Bot Help", color=0x2196F3)
			embed.description = botHelp
		elif msg.startswith('!darkjoke'):
			r = requests.get("https://v2.jokeapi.dev/joke/Dark?type=twopart")
			j=r.json()
			response = j['setup'] +'\n ' + j['delivery']
		elif msg.startswith('!insult'):
			if 'shakespearean' in msg:
				insultToSend = getShakespeareanInsult()
			else:
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
					# response = "Hey Insult Bot, "+insultToSend
					response = "Hey <@"+str(client.user.id)+">, "+insultToSend
				if name == 'random':
					members = message.guild.members
					memberList = []
					for member in members:
						if not member.bot:
							memberList.append(member.id)
					person = random.choice(memberList)
					response = "Hey <@"+str(person)+">, "+insultToSend
			else:
				response = "Please specify whom I should insult"
		
		elif msg.startswith('!joke'):
			joke = getJoke()
			name = ''
			if ' ' in msg:
				name = msg.split()[1]
			if len(name)>0:
				if name != 'me':
					response = "Hey "+name+", "+joke
				if name == 'me':
					response = "Hey <@"+str(message.author.id)+">, "+joke
				if name == 'yourself':
					response = "Hey Insult Bot, "+joke
			else:
				members = message.guild.members
				memberList = []
				for member in members:
					if not member.bot:
						memberList.append(member.id)
				print(memberList)
				person = random.choice(memberList)
				response = "Hey <@"+str(person)+">, " + joke

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
				response = "Hey <@"+str(person)+">, "+complimentToSend
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
		await message.add_reaction('🇸')
		await message.add_reaction('🇹')
		await message.add_reaction('🇫')
		await message.add_reaction('🇺')
		messageAnalysis = TextBlob(msg)
		sentimentValue = messageAnalysis.sentiment.polarity
		if sentimentValue > 0.5:
			response = random.choice(kissass).strip()
		else:
			response = random.choice(comebacks).strip()

		await message.channel.send("Hey "+str(message.author.mention)+", "+response) 

client.run(TOKEN)