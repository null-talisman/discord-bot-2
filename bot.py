# discord bot

import os
import discord
from connect.db_connect import db_connect
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

database=db_connect()

client = discord.Client()


@client.event
async def on_message(msg):
    scr = 0
    words = []

    # ignore bot msgs
    if msg.author == client.user:
        return

    # scoreboard
    if msg.content == '!scoreboard':
        try:
            # TODO: validate sql inputs
            qry = "SELECT name, SUM(score) FROM discord_scores GROUP BY name;"
            cursor = database.cursor()
            cursor.execute(qry)
            scoreboard = cursor.fetchall()
            await msg.channel.send(scoreboard)
        except Error as e:
            print(e)
        return

    # get msg score
    x = msg.content
    chn = msg.channel
    athr = msg.author

    for i in x:
        if i == " ":
            continue
        else:
            scr = scr + ord(i)

    # upload to db
    try:
        # TODO: validate sql input
        qry = """INSERT INTO discord_scores(name, score) VALUES("{}", "{}");""".format(athr, scr)
        cursor = database.cursor()
        cursor.execute(qry)
        database.commit()
        print(scr)
    except Error as e:
        print(e)


# run bot program
client.run(TOKEN)
