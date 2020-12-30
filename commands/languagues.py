import discord
languagues_list = ["Javascript", "Coffeescript", "Ruby", "Python", "Haskell", "Clojure", "Java", "Csharp", "Elixir", "Cpp", "Typescript", "Php", "Crystal", "Dart", "Rust", "Fsharp", "Swift", "Go", "Shell", "C", "Lua", "Sql", "Bf", "R", "Nim", "Erlang", "Objc", "Scala", "Kotlin", "Solidity", "Groovy", "Fortran", "Nasm", "Julia", "Powershell", "Purescript", "Elm", "Ocaml", "Reason", "Idris", "Racket", "Agda", "Coq", "Vb", "Forth", "Factor", "Prolog", "Cfml", "Lean", "Cobol", "Haxe", "Commonlisp", "Raku", "Perl", "Pascal"]
languagues_list.sort()
async def languagues(message, args):
    languagues_for_embed = ''
    for l in languagues_list:
        if (len(languagues_for_embed.split(' ')) % 10 == 0): languagues_for_embed += " \n"
        languagues_for_embed += l +" ,"
    languagues_for_embed = languagues_for_embed[:len(languagues_for_embed)-1]

    embed_languagues = discord.Embed(title=message.author.name, description="Here is a list of all the languagues codewars support", color=0xFF00FF)
    embed_languagues.add_field(name="Languagues", value=languagues_for_embed, inline=False)
    await message.channel.send(embed=embed_languagues)