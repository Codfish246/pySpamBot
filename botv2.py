import discord
import asyncio
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

prefix = '!'
delay = 1
numMessages = 1000 #number of messages to spam, 0 for infinite
#also change user id where it says

sentCount = 0

@client.event
async def on_message(message):
    global count
    global prefix
    global numMessgaes
    global sentCount
    if message.content.startswith('!numberspam' and message.author.id == 'USER ID HERE'): #may not work yet but this very important xd
        if numMessages > 0:
        	for i in range(0, numMessages):
        		await client.send_message(message.channel, random.randint(1,1000))
        		sentCount += 1
        		print("sent", sentCount)
        		time.sleep(delay)
        elif numMessgaes == 0:
        	while(True):
        		await client.send_message(message.channel, random.randint(1,1000))
        		sentCount += 1
        		print("sent", sentCount)
        		time.sleep(delay)
sentCount = 0
    #if message.content.startswith("logout"): #test logout cmd
    	#self.logout()
client.run('token', bot=False)
