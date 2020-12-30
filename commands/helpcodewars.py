import discord, requests
async def helpcodewars(message,args,prefix):
    embed_helpcodewars = discord.Embed(title=message.guild.name ,description="The commands are: ", color=0x00ff00)
    embed_helpcodewars.add_field(name=f"{prefix}getuserinfo", value="Get the user info like rank, clan, honor, etc. \n **Argument**: *a valid username*", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}getkatainfo", value="Get the kata info like rank, category, languages, user invovled, collected info, etc. \n **Argument**: *a valid kata name*", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}getrandomkata", value="Search a kata, randomly, by level, or by level and category \n **Argument**: *none*: return a random kata, \n *Language* select a valid lenguage \n *1-8* return a *1-8* kata rank \n *1-8* *a valid cathegory*, return a kata with 1-8 rank and with according cathegory", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}invite", value="Create and invitation to the discord server and codewars clan \n **Argument**: N/A", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}github", value="Show the project's github and our githubs \n **Argument**: N/A", inline=False)
    embed_helpcodewars.set_image(url="https://withoutstress.com/wp-content/uploads/2019/03/ask-for-help.jpg")
    await message.channel.send(embed=embed_helpcodewars)