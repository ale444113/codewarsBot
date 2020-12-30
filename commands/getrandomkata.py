import discord, requests, random, json

#Here we load all the info from our data.json and save it as a dictionary in the var data
with open('data.json','r') as f:
    data = json.load(f)
#This function take a language wich is l and check if it is in the list, if it is it return the language if it doesn't it return False
async def get_and_check_languague(l,message,prefix,args):
    languages = ["Javascript", "Coffeescript", "Ruby", "Python", "Haskell", "Clojure", "Java", "Csharp", "Elixir", "Cpp","C++", "Typescript", "Php", "Crystal", "Dart", "Rust", "Fsharp", "Swift", "Go", "Shell", "C", "Lua", "Sql", "Bf", "R", "Nim", "Erlang", "Objc", "Scala", "Kotlin", "Solidity", "Groovy", "Fortran", "Nasm", "Julia", "Powershell", "Purescript", "Elm", "Ocaml", "Reason", "Idris", "Racket", "Agda", "Coq", "Vb", "Forth", "Factor", "Prolog", "Cfml", "Lean", "Cobol", "Haxe", "Commonlisp", "Raku", "Perl", "Pascal"]
    language = l.lower().capitalize()
    if language == "C++": language = "Cpp"
    if language not in languages:
        await message.channel.send(f"{message.author.mention}, {args[len(args)-1]} is not a language, to see a list of languages use {prefix}languagues")
        return False
    return language
#It check if the level(l) exist and if it does return the level, if it doesn't exist it return False
async def get_and_check_lvl(l,message,args):
    kyu_lvls = ["1","2","3","4","5","6","7","8"]
    lvl = l.replace('-','')
    if lvl not in kyu_lvls:
        await message.channel.send(f"{message.author.mention}, {args[0]} is not a valid level!")
        return False
    return lvl
#This check if there is a valid topic in the args
async def get_and_check_topic(args,topics,message,prefix):
    topic = ""
    for x in args:
        topic += x.lower().capitalize()
    if topic not in topics:
        await message.channel.send(f"{message.author.mention}, {topic} is not a valid topic, if you want to see all the topics use {prefix}topics")
        return False
    return topic
#This function will take a language a lvl a topic and the list of topics and it will get the kata and all info of it
async def getkata(language,lvl,topic, topics):
    if lvl == None: lvl = random.randint(1,8)
    if topic == None: topic = random.choice(topics)
    kata = random.choice(data[str(lvl)][topic])
    kata = kata.lower().replace(' ','-')
    try: kata_data = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata}").json()
    except: return await getkata(language, lvl, topic, topics)
    if 'success' in kata_data:
        return await getkata(language,lvl,topic,topics)

    if language != None and language.lower() not in kata_data["languages"]:
        return await getkata(language, lvl, topic, topics)
    return kata_data

async def getrandomkata(message,args, prefix):
    topics = ["Algorithms","Logic", "Fundamentals", "Games", "Data Types"]

    if args == []:
        kata_data = await getkata(None, None, None, topics)
    elif len(args) == 1:
        lvl = lvl = await get_and_check_lvl(args[0],message,args)
        if lvl == False: return

        kata_data = await getkata(None, lvl, None, topics)

    elif len(args) == 2:
        lvl = await get_and_check_lvl(args[0],message,args)
        if lvl == False: return

        topic = await get_and_check_topic(args,topics,message,prefix)
        if topic == False: return

        kata_data = await getkata(None, lvl, None, topics)

    elif len(args) >= 3:
        lvl = await get_and_check_lvl(args[0],message,args)
        if lvl == False: return
        args.pop(0)
        
        language = await get_and_check_languague(args[len(args)-1],message,prefix,args)
        if language == False: return
        args.pop(len(args)-1)
        
        topic = await get_and_check_topic(args,topics,message,prefix)
        if topic == False: return


        kata_data = await getkata(language, lvl, topic, topics)

    embed_kata = discord.Embed(title=f"💥 {kata_data['name']} 💥", description=f"Hello {message.author.name} here is a random kata", color=0x00FFFF)
    embed_kata.add_field(name="Category", value=kata_data['category'].capitalize(), inline=False)

    languages = ""
    for language in kata_data['languages']: languages += language.capitalize() + ", "
    languages = languages[:len(languages)-2] 

    embed_kata.add_field(name="Languages", value=languages, inline=False)
    rank = kata_data['rank']['name'] + " " + kata_data['rank']['color']
    embed_kata.add_field(name="Rank", value=rank, inline=False)
    embed_kata.add_field(name="Url", value=kata_data['url'], inline=False)
    embed_kata.set_footer(text="Good luck!")
    await message.channel.send(embed=embed_kata)