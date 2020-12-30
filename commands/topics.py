import discord
async def topics(message,args):
    embed_topic = discord.Embed(title=message.author.name, description="Here is a list of all the topics we have", color=0xFF00FF)
    embed_topic.add_field(name="Topics", value=" 1) Algorithms \n 2) Logic \n 3) Fundamentals \n 4) Games \n 5) Data Types", inline=False)
    await message.channel.send(embed=embed_topic)