from bot.constants import *
import random
import requests

def getInsult():
	return random.choice(insults).strip()

def getShakespeareanInsult():
	return random.choice(shakespeareInsults).strip()

def getCompliment():
	return random.choice(compliments).strip()

def getJoke():
	return random.choice(jokes).strip()

def getComeback():
	return random.choice(comebacks).strip()

def getKissass():
	return random.choice(kissass).strip()

def getDarkJoke():
	r = requests.get("https://v2.jokeapi.dev/joke/Dark?type=twopart")
	joke = r.json()
	return joke['setup'] +'\n ' + joke['delivery']

def getInsult(client, message):

	msg = message.content.strip()

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
	
	return response

def getJoke(client, message):

	msg = message.content.strip()

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
	
	return response

def getCompliment(client, message):

	msg = message.content.strip()

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

	return response