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
    print('------')

delay = 0.8 #edit this for the delay in sending messages
count = 0 #initalisation for a counting var

@client.event
async def on_message(message):
    global count
    if message.content.startswith('!numbers'):
        """
        await client.send_message(message.channel, 'test')
        print("sent test")
        """
        #copy and paste these to adjust amount of messages, 50 by default xd, not got a good way to do these yet
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        await client.send_message(message.channel, random.randint(1,1000))
        count += 1
        print("sent", count)
        time.sleep(delay)
        count = 0

client.run('token', bot=False)
