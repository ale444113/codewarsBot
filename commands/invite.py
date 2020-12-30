import discord
async def invite(message,args):
    embed_invite = discord.Embed(title="Invite link", description="Click the link below to invite me to your server", color=0x00FF00)
    embed_invite.set_thumbnail(url="https://mailtrack.io/wp-content/uploads/2017/05/cropped-mailtrack-logo-chrome-ext-1.png")
    embed_invite.add_field(name="    ‏‏‎",value="[Invite me!](https://discord.com/api/oauth2/authorize?client_id=793518686459527199&permissions=0&scope=bot)")
    await message.channel.send(embed=embed_invite)