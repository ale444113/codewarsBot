import discord, requests
async def helpcodewars(message,args,prefix):
    embed_helpcodewars = discord.Embed(title="Available Commands", color=0xff0000)
    embed_helpcodewars.add_field(name=f"{prefix}getuserinfo", value="```Returns specified user's info. \n args: !?getuserinfo <valid username> ```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}getkatainfo", value="```Returns specified kata's info. \n args: !?getkatainfo <valid kata name>```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}getrandomkata", value="```Returns a random kata, also you can specify the expected kyu, topic and language. \n args: !?getrandomkata N/A \n !?getrandomkata <kyu topic language>```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}invite", value="```Returns an invitation to add Codewars bot to your server. \n args: !?invite N/A```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}github", value="```Returns the project's GitHub repository. \n args: !?github N/A```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}languages", value="```Returns Codewars supported languages. \n args: !?languages N/A```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}topics", value="```Returns available topics. \n args: !?topics N/A```", inline=False)
    embed_helpcodewars.add_field(name=f"{prefix}authors", value="```Info about the devs :) \n args: !?authors N/A```", inline=False)
    await message.channel.send(embed=embed_helpcodewars)
