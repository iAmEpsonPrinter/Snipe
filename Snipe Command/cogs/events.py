import discord, json
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()       
    async def on_message_delete(self, message):
        if message.author == self.client.user:
            return

        with open("logged_message.json", "r") as f:
            open_file = json.load(f)

        if str(message.channel.id) not in open_file:
            open_file[str(message.channel.id)] = {}

        open_file[str(message.channel.id)] = {"message_content": message.content, "author": str(message.author.id)}


        with open("logged_message.json", "w") as f:
            json.dump(open_file, f, indent = 1)
            

def setup(client):
    client.add_cog(Events(client))



