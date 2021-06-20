import discord, json
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def snipe(self, ctx):
        with open("logged_message.json", "r") as f:
            open_file = json.load(f)

        if str(ctx.channel.id) not in open_file: 
            no_message_embed = discord.Embed(
                title = "Nothing to snipe.",
                color = discord.Color.red()
            )
            return await ctx.send(embed = no_message_embed)
        user = await self.client.fetch_user(open_file[str(ctx.channel.id)]["author"])
        content = open_file[str(ctx.channel.id)]["message_content"]
        
        sniped_embed = discord.Embed(
            description = f"**Message from** {user.mention}",
            color = discord.Color.dark_blue()
        )
        sniped_embed.add_field(name = "Deleted Message", value = f"```{content}```", inline = False)
        sniped_embed.set_author(name = user, icon_url = str(user.avatar_url))
        await ctx.send(embed = sniped_embed)

def setup(client):
    client.add_cog(Commands(client))
