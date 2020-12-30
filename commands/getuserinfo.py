import discord, requests
async def getuserinfo(message,args):
    if(args == []):
        await message.channel.send(f'{message.author.mention}, you must specify a valid username')
        return
    data = requests.get(f"https://www.codewars.com/api/v1/users/{args[0]}").json()
    if "success" in data: 
        await message.channel.send(f"{message.author.mention}, I couldn't find {args[0]}")
        return

    name = data['name'] if data['name'] != '' else 'N/A'
    embed_with_user_data = discord.Embed(title=f"{args[0]}'s info", description="Here is all the info I founded about he/her", color=0x00ff00)
    embed_with_user_data.add_field(name="👾 User info 👾", value=f"Username: {data['username']} \n Name: {name} \n Clan: {data['clan']}", inline=True)
    ranks = ""
    for x in data['ranks']:
        if x != "languages":
            ranks += f"Rank: {x}, {data['ranks'][x]['name']}, {data['ranks'][x]['color']} \n"
    embed_with_user_data.add_field(name="📈 User stats 📉", value=f"Honor: {data['honor']} \n LeaderBoard position: {data['leaderboardPosition']} \n Ranks: {ranks}", inline=True)
    languages = ""
    skills = ""
    for x in data['ranks']['languages']: languages += f"{x.capitalize()}: {data['ranks']['languages'][x]['name']}, {data['ranks']['languages'][x]['color']}, {str(data['ranks']['languages'][x]['score'])} score \n"
    for skill in data['skills']: skills += skill + ", "
    if skills != '': skills = skills[:len(skills)-2] 
    if skills == '': skills = "N/A"
    embed_with_user_data.add_field(name="⌨️ Languagues and skills 📱", value=f"Languages: {languages} \n Skills: {skills}", inline=False)
    embed_with_user_data.add_field(name="💻 Code Challengues 💾", value=f"Authored: {data['codeChallenges']['totalAuthored']} \n Completed: {data['codeChallenges']['totalCompleted']}", inline=True)
    
    kyu_level = data['ranks']['overall']['rank']
    if kyu_level == -1: embed_with_user_data.set_image(url="https://i.ibb.co/16whS56/1.png")
    elif kyu_level == -2: embed_with_user_data.set_image(url="https://i.ibb.co/MDBvfKw/2.png")
    elif kyu_level == -3: embed_with_user_data.set_image(url="https://i.ibb.co/7kn00Jt/3.png")
    elif kyu_level == -4: embed_with_user_data.set_image(url="https://i.ibb.co/TRH8Y6b/4.png")
    elif kyu_level == -5: embed_with_user_data.set_image(url="https://i.ibb.co/q9x4W6F/5.png")
    elif kyu_level == -6: embed_with_user_data.set_image(url="https://i.ibb.co/dLmn8Tx/6.png")
    elif kyu_level == -7: embed_with_user_data.set_image(url="https://i.ibb.co/G96g8Cd/7.png")
    elif kyu_level == -8: embed_with_user_data.set_image(url="https://i.ibb.co/K0YdSVc/8.png")

    embed_with_user_data.set_footer(text="Made by: ale444113#6621")
    await message.channel.send(embed=embed_with_user_data)
