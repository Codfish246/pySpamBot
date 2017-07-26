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

delay = 0.8
count = 0

@client.event
async def on_message(message):
    global count
    if message.content.startswith('!numbers'):
        """
        await client.send_message(message.channel, 'test')
        print("sent test")
        """
       3 while (True):
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            await client.send_message(message.channel, random.randint(1,1000))
            count += 1
            print("sent", count)
            await asyncio.sleep(delay)
            count = 0

client.run('token', bot=False)