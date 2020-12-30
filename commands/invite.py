import discord
async def invite(message,args):
    embed_invite = discord.Embed(title=message.author.name, description="Do you want to join us?", color=0x00FFFF)
    embed_invite.add_field(name="Join us by codewars!", value="Go to --> account settings and set the name: *😈 Las putas de TD 😈* and update the changes!", inline=False)
    embed_invite.add_field(name="Join our discord", value="Url --> https://discord.gg/zXKTWfc", inline=False)
    await message.channel.send(embed=embed_invite)