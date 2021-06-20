import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix = "?", help_command = None)

for file_name in os.listdir("./cogs"):
    if file_name.endswith(".py"): 
        client.load_extension(f"cogs.{file_name[:-3]}")

client.run("BOT TOKEN")
