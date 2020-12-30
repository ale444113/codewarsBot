import discord, os, requests
from dotenv import load_dotenv

from commands.getuserinfo import getuserinfo
from commands.getkatainfo import getkatainfo
from commands.helpcodewars import helpcodewars
from commands.invite import invite
from commands.authors import authors
from commands.github import github
from commands.getrandomkata import getrandomkata
from commands.topics import topics
from commands.languages import languages

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

PREFIX = "!?"

n_servers = 0
@client.event
async def on_ready():
    global n_servers
    for guild in client.guilds:
        print(f"I'm in {guild.name} (id: {guild.id})")
        n_servers+=1
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f" codewars.com | Active in {n_servers}"))#Set the presence

@client.event
async def on_guild_join(guild):
    global n_servers
    embedVar = discord.Embed(title="Say hi!", description="codewarsBot has joined the server", color=0x0000FF)
    embedVar.add_field(name="Prefix", value=f"My prefix is {PREFIX} 😃", inline=False)
    embedVar.add_field(name="Get help", value=f"Use {PREFIX}help to see a list of commands n.n", inline=False)
    embedVar.set_image(url="https://jungladigital.com/wp-content/uploads/2019/03/codewars-800-350.png")
    embedVar.set_footer(text="Made by: ale444113#6621")

    print(f"I just joined {guild.name} (id: {guild.id})")
    n_servers += 1
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f" codewars.com | Active in {n_servers}"))#Set the presence again

    await guild.text_channels[0].send(embed=embedVar)
@client.event
async def on_guild_remove(guild):
    global n_servers
    print(f"I was removed from {guild.name} (id: {guild.id})")
    n_servers -= 1
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f" codewars.com | Active in {n_servers}"))#Set the presence again
@client.event
async def on_message(message):
    args = message.content.split(' ')
    if PREFIX not in args[0]: return
    cmd = args[0].replace(PREFIX,'')
    args.remove(args[0])

    if cmd.lower() == "getuserinfo": await getuserinfo(message,args)
    elif cmd.lower() == "getkatainfo": await getkatainfo(message,args)
    elif cmd.lower() == "help": await helpcodewars(message,args, PREFIX)
    elif cmd.lower() == "invite": await invite(message,args)
    elif cmd.lower() == "authors" or cmd.lower() == "author": await authors(message,args)
    elif cmd.lower() == "github" or cmd.lower() == "githubs": await github(message,args)
    elif cmd.lower() == "getrandomkata": await getrandomkata(message,args, PREFIX)
    elif cmd.lower() == "topics" or cmd.lower() == "topic": await topics(message,args)
    elif cmd.lower() == "languages" or cmd.lower() == "language": await languages(message,args)

client.run(TOKEN)