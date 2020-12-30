import discord
languages_list = ["Javascript", "Coffeescript", "Ruby", "Python", "Haskell", "Clojure", "Java", "Csharp", "Elixir", "Cpp", "Typescript", "Php", "Crystal", "Dart", "Rust", "Fsharp", "Swift", "Go", "Shell", "C", "Lua", "Sql", "Bf", "R", "Nim", "Erlang", "Objc", "Scala", "Kotlin", "Solidity", "Groovy", "Fortran", "Nasm", "Julia", "Powershell", "Purescript", "Elm", "Ocaml", "Reason", "Idris", "Racket", "Agda", "Coq", "Vb", "Forth", "Factor", "Prolog", "Cfml", "Lean", "Cobol", "Haxe", "Commonlisp", "Raku", "Perl", "Pascal"]
languages_list.sort()
async def languages(message, args):
    languages_for_embed = ''
    for l in languages_list:
        if (len(languages_for_embed.split(' ')) % 5 == 0): languages_for_embed += " \n"
        languages_for_embed += l +", "
    languages_for_embed = "```"+languages_for_embed[:len(languages_for_embed)-2]+"```"
    embed_languages = discord.Embed(title="Supported languages:", description=languages_for_embed, color=0xFF00FF)
    await message.channel.send(embed=embed_languages)