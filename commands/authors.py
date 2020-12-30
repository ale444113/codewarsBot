import discord
async def authors(message,args):
    embed_authors = discord.Embed(title="🐧 About us 🐈", description=f"Hello {message.author.name} here is some info about the devs!", color=0x00FFFF)
    embed_authors.add_field(name="    ‏‏‎", value="[**ale444113**](https://github.com/ale444113) \n ```A 14 year old programmer from Spain that enjoys making software.```", inline=False)
    embed_authors.add_field(name="    ‏‏‎", value="[**imTDB**](https://github.com/imTDB) \n ```CS Student and attempt of techtuber```", inline=False)
    embed_authors.add_field(name="    ‏‏‎", value="[**Mariovlv**](https://github.com/Mariovlv) \n ```Python programming ?```", inline=False)
    embed_authors.set_footer(text="Thanks for reading this ❤️")
    await message.channel.send(embed=embed_authors)
