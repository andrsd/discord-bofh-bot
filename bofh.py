"""
BOFH - Bastard Operator From Hell

Bot for Discord
"""

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from excuses import excuses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='bofh', help='Responds with a random Bastard Operator From Hell quote')
async def bofh_quote(ctx):
    response = random.choice(excuses)
    await ctx.send(response)

@bot.command(name='topic-bofh', help='Sets the channel topic to a random Bastard Operator From Hell quote')
async def bofh_channel_topic(ctx):
    response = random.choice(excuses)
    if hasattr(ctx.channel, "edit"):
        await ctx.channel.edit(topic=response)

bot.run(TOKEN)
