import discord
from discord.ext import commands

from config import TOKEN, PREFIX


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")


async def load_extensions():
    await bot.load_extension("cogs.economy")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


import asyncio

asyncio.run(main())
