import discord
async def github(message,args):
    embed_github = discord.Embed(title="Project's Repository", color=0xFF00FF)
    embed_github.add_field(name="Source Code", value="https://github.com/ale444113/codewarsBot", inline=False)
    embed_github.set_footer(text="Give us a star ⭐")
    await message.channel.send(embed=embed_github)
