import discord
from client import Client
import os

client = Client(command_prefix=["t!"], intents=discord.Intents.all(), help_command=None, allowed_mentions=discord.AllowedMentions.all())
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
@client.event
async def on_ready():
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('n!help'))
    print("We have logged in as {0.user}".format(client))
    
# @check.is_staff()
# @client.command()
# async def _load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# @check.is_staff()
# @client.command()
# async def _unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

@client.command()
async def teekitstore(ctx):
    if not await client.is_owner(ctx.author):
        embed = discord.Embed(
            title=f"Skem not a nianny.",
            description="This is very bad!!! You should not be trying be imposter :",
            colour=discord.Colour.orange()
        )
        ctx.send(embed=embed)
    # print(ctx.guild.id)
    with open(f'{ctx.guild.id}.txt', 'a') as f:
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                async for message in channel.history():
                    if not message.author.bot:
                        f.write(f'{message.author.name} ({message.author.id}): {message.content}\n')
                print(f'Scraping: {channel.name}')
            # print(channel.name)
    
    await ctx.send("Yayyyyy")

@client.command()
async def teekitpoof(ctx):
    if not await client.is_owner(ctx.author):
        embed = discord.Embed(
            title=f"Skem not a nianny.",
            description="This is very bad!!! You should not be trying be imposter :",
            colour=discord.Colour.orange()
        )
        ctx.send(embed=embed)
    # print(ctx.guild.id)
    with open(f'{ctx.guild.id}.txt', 'a') as f:
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                if channel.name.startswith('closed'):
                    print(f'Deleting: {channel.name}')
                    await channel.delete(reason="poof")
            # print(channel.name)
    
    await ctx.send("Yayyyyy")
    
client.run(os.getenv('teekit'))