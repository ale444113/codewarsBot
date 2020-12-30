import discord
async def authors(message,args):
    embed_authors = discord.Embed(title="🐧 About us 🐈", description=f"Hello {message.author.name} here is some info about the devs!", color=0x00FFFF)
    embed_authors.add_field(name="[ale444113](https://github.com/ale444113)", value="```A 14 year old programmer from Spain that enjoys making software.```", inline=False)
    embed_authors.add_field(name="[imTDB](https://github.com/imTDB)", value="```CS Student and attempt of techtuber```", inline=False)
    embed_authors.add_field(name="[Mariovlv](https://github.com/Mariovlv)", value="```Python programming ?```", inline=False)
    embed_authors.set_footer(text="Thanks for reading this ❤️")
    await message.channel.send(embed=embed_authors)
