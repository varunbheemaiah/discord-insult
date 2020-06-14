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
    if message.content.startswith('!'):
        if message.content.startswith('!insult help'):
            response = '''
            Bot Commands:\n!insult: Insult a random person on the server\n!insult <name>: Insults person with name <name>.\n!insult me: Insults you\n!insult yourself: Insults itself
            '''
        elif message.content.startswith('!insult'):
            insultToSend = random.choice(insults).strip()
            name = None
            if ' ' in message.content:
                name = message.content.split()[1]
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
        else:
            response = "Invalid Command. Please type '!insult help' for a list of commands"
        await message.channel.send(response)

client.run(TOKEN)