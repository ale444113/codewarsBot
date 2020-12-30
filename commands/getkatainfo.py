import discord, requests
async def getkatainfo(message,args):
    if(args == []):
        await message.channel.send(f'{message.author.mention}, you must specify a valid kata name')
        return
        
    slug = ""
    for x in args:
        slug += x + "-"
    slug = slug[:len(slug)-1]

    kata_tittle = slug.lower()
    data = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata_tittle}").json()
    if "success" in data: 
        await message.channel.send(f"{message.author.mention}, I couldn't find {kata_tittle}")
        return
    
    embed_with_user_data = discord.Embed(title=f"{kata_tittle}'s info", description="Here is all the info about this kata", color=0xFFFF00)
    publishedAt = data['publishedAt'][:10]
    approvedAt = data['approvedAt'][:10]
    embed_with_user_data.add_field(name="🌴 Kata's info 🌴", value=f"Rank: {data['rank']['name']} \n Category: {data['category']} \n Published at: {publishedAt} \n Aproved at: {approvedAt} \n Id: {str(data['id'])} \n", inline=True)
    
    languages = ""
    for language in data['languages']: languages += language.capitalize() + ", "
    languages = languages[:len(languages)-2] 

    embed_with_user_data.add_field(name="👅 Languagues 👅", value=f'{languages} \n', inline=False)
    try: 
        author = data['createdBy']['username']
        author_url = data['createdBy']['url']
    except: 
        author = "N/A"
        author_url = "N/A"
    try: 
        aproved = data['approvedBy']['username']
        aproved_url = data['approvedBy']['url']
    except: 
        aproved = "N/A"
        aproved_url = "N/A"
    embed_with_user_data.add_field(name="👩 Users involve in the kata 👦", value=f"Creator username: {author} \n Creator url: {author_url} \n Approved by: {aproved} \n Approved by url: {aproved_url} \n", inline=False)
    embed_with_user_data.add_field(name="📬 Collected info 📬", value=f"Total attempts: {data['totalAttempts']} \n Total completes: {data['totalCompleted']} \n Total stars: {data['totalStars']} \n Issues: {data['unresolved']['issues']} \n", inline=True)
    embed_with_user_data.set_footer(text="Made by: ale444113#6621")
    await message.channel.send(embed=embed_with_user_data)