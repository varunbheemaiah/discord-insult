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

with open("static/insults.txt","r") as insultFile:
	insults = list(insultFile)

with open('static/shakespearean.txt', "r") as shakespeare:
	shakespeareInsults = list(shakespeare)

with open('static/jokes.txt') as jokesFile:
	jokes = list(jokesFile)

with open("static/comebacks.txt","r") as comebacksFile:
	comebacks = list(comebacksFile)

with open("static/kissass.txt","r") as kissassFile:
	kissass = list(kissassFile)

with open("static/compliments.txt",'r') as complimentsFile:
	compliments = list(complimentsFile)