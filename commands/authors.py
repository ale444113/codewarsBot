import discord
async def authors(message,args):
    embed_authors = discord.Embed(title="🐧 About us 🐈", description=f"Hello {message.author.name} here is some info about us", color=0x00FFFF)
    embed_authors.add_field(name="ale444113", value="Something", inline=False)
    embed_authors.add_field(name="imTDB", value="Something", inline=False)
    embed_authors.add_field(name="Mariovlv", value="Something", inline=False)
    embed_authors.set_footer(text="Thanks for reading this <3")
    await message.channel.send(embed=embed_authors)