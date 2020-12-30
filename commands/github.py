import discord
async def github(message,args):
    embed_github = discord.Embed(title="💫 Our githubs 💫", description=f"{message.author.name} here is our githubs!", color=0xFF00FF)
    embed_github.add_field(name="Project github", value="https://github.com/ale444113/codewarsBot", inline=False)
    embed_github.add_field(name="ale444113's github", value="https://github.com/ale444113", inline=False)
    embed_github.add_field(name="imTDB's github", value="https://github.com/imTDB", inline=False)
    embed_github.add_field(name="Mariovlv's github", value="https://github.com/Mariovlv", inline=False)
    embed_github.set_footer(text="Thanks for reading this <3")
    await message.channel.send(embed=embed_github)