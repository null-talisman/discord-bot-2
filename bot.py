# discord bot

import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

client=discord.Client()

@client.event
async def on_message(msg):

    # vars
    words = []
    standard_scoring = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, \
            "i": 9, "j": 10, "k":11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, \
            "r": 18, "s": 19, "t": 20, "u": 21, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} 
    scr = 0

    # check recursion
    if msg.author == client.user:
        return

    # content, channel, author
    x    = msg.content
    chn  = msg.channel
    athr = msg.author

    # x
    for i in x:
        if i == " ":
            continue
        else:
            ctr = 0
            for y in standard_scoring:
                if y == i:
                    words.append(standard_scoring[y])
                ctr+=1

    # score
    for z in words:
        scr = scr + z

    # TODO: send athr and scr to db
    

    # scoring
    if scr > 100:
        await chn.send("pog")
    else:
        await chn.send("unpog")

# run bot program
client.run(TOKEN)
