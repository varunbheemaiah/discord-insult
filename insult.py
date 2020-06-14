from os import environ
import discord
import random

TOKEN = environ['DISCORD']

client = discord.Client()

insultFile = open('static/insults.txt')
insults = list(insultFile)
insultFile.close()

@client.event
async def on_ready():
    print(f'{client.user} has connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    insultToSend = random.choice(insults).strip()
    if message.content.startswith('!insult'):
        name = None
        if ' ' in message.content:
            name = message.content.split()[1]
        if name:
            if name != 'me':
                response = "Hey "+name+", "+insultToSend
            if name == 'me':
                response = "Hey "+message.author+", "+insultToSend
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
        await message.channel.send(response)

client.run(TOKEN)