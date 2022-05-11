# connect to local db

import os

import mysql.connector
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('DISCORD_HOST')
USER = os.getenv('DISCORD_USER')
DB = os.getenv('DISCORD_DB')


def db_connect():

    try:
        db_con = mysql.connector.connect(
            user=USER,
            host=HOST,
            db=DB
        )
        return db_con
    except Error as e:
        print(e)

    return

