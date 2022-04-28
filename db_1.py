# mysql db shenanigans

# imports
from getpass import getpass
from mysql.connector import connect, Error

# global
USER = "n1lla"
HOST = "localhost"

def main():
  # connect to mysql, create db if it does not exist 
  try:
    with connect(
      host="localhost",
      user=input("Enter username: "),
    ) as connection:
      with connection.cursor() as cursor:
        show_db_query = "SHOW DATABASES"
        cursor.execute(show_db_query)
        db_exists = False
        for db in cursor:
          db_str = str(db)
          test = "('discord_user_scores',)"
          if db_str == test:
            db_exists = True
        if db_exists != True:
          create_db = "CREATE DATABASE discord_user_scores"
          cursor.execute(create_db)
        else:
          DB = "discord_user_scores"
    connection.close()
  except Error as e:
    print(e)
  # reconnect to db, create table if it does not exist
  try:
    with connect(
      host = "localhost",
      user = USER,
      database = DB
    ) as connection:
      with connection.cursor() as cursor:
        show_db_tables = "SHOW TABLES"
        cursor.execute(show_db_tables)
        tbl_exists = False
        for db_table in cursor:
          db_tbl = str(db_table)
          test = "('discord_scores',)"
          if db_tbl == test:
            tbl_exists = True
        if tbl_exists != True:
          create_score_table = """
          CREATE TABLE discord_scores(
            name CHAR,
            score INT,
            PRIMARY KEY (score)
          )
          """
          cursor.execute(create_score_table)
          connection.commit()
  except Error as e:
    print(e)

if __name__ == '__main__':
    main()


