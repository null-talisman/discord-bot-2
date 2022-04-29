# discord bot

import os
import discord
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_message(msg):

    scr = 0
    words = []
    standard_scoring_lower = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
                              "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
                              "r": 18, "s": 19, "t": 20, "u": 21, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    standard_scoring_upper = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                              "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
                              "R": 18, "S": 19, "T": 20, "U": 21, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}

    if msg.author == client.user:
        return

    if msg.content == '!scoreboard':
        try:
            with connect(
                host="localhost",
                user="n1lla",
                database="discord_user_scores"
            ) as connection:
                with connection.cursor(buffered=True) as cursor:
                    qry = "SELECT name, SUM(score) FROM discord_scores GROUP BY name;"
                    cursor.execute(qry)
                    scoreboard = cursor.fetchall()
                    await msg.channel.send(scoreboard)
        except Error as e:
            print(e)
 
    x = msg.content
    chn = msg.channel
    athr = msg.author

    for i in x:
        if i == " ":
            continue
        else:
            for y in standard_scoring_lower:
                if y == i:
                    words.append(standard_scoring_lower[y])
            for y in standard_scoring_upper:
                if y == i:
                    words.append(standard_scoring_upper[y])

    # score
    for z in words:
        scr = scr + z

    # db
    try:
        with connect(
            host="localhost",
            user="n1lla",
            database="discord_user_scores"
        ) as connection:
            with connection.cursor() as cursor:
                insert_stmt  = """
                INSERT INTO discord_scores(name, score) VALUES("{}", "{}");""".format(athr, scr)
                cursor.execute(insert_stmt)
                connection.commit()
                print(scr)
    except Error as e:
        print(e)

# TODO: When a user enters "!scoreboard", a visualization of the below query is sent to the channel
# sql query: SELECT name, SUM(score) FROM discord_scores GROUP BY name;
#@client.event
#async def on_message(msg):

# run bot program
client.run(TOKEN)
