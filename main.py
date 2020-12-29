import discord, os, requests
from commands.getuserinfo import getuserinfo
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

PREFIX = "!?"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" people coding"))#Set the presence

@client.event
async def on_guild_join(guild):
    embedVar = discord.Embed(title="Say hi!", description="codewarsBot has joined the server", color=0x0000FF)
    embedVar.add_field(name="Prefix", value=f"My prefix is {PREFIX} 😃", inline=False)
    embedVar.add_field(name="Get help", value=f"Use {PREFIX}help to see a list of commands n.n", inline=False)
    embedVar.set_image(url="https://jungladigital.com/wp-content/uploads/2019/03/codewars-800-350.png")
    embedVar.set_footer(text="Made by: ale444113#6621")

    await guild.text_channels[0].send(embed=embedVar)

@client.event
async def on_message(message):
    args = message.content.split(' ')
    if PREFIX not in args[0]: return
    cmd = args[0].replace(PREFIX,'')
    args.remove(args[0])

    if cmd.lower() == "getuserinfo": await getuserinfo(message,args)
        
client.run(TOKEN)