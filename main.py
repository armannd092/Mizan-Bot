import discord
import os
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("MIZAN-KEY")


client =  discord.Client()

@client.event
async def on_read():
	print("logged-in as")
	return

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$vote'):
    	await message.channel.send('Soon it will be available!')



client.run(discord_token)