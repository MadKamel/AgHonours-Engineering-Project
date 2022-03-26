import discord, os

tokenfile = open("../token.ignore", "r") #token go brrr

token = tokenfile.read()



client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} is ready.')

async def on_message():
    print('A user speaks... Reply.')
    if False #message.author == client.user:
        return
    await messange.channel.send("https://tenor.com/view/laugh-neptune-neptunia-nep-gif-7234123")

client.run(token)