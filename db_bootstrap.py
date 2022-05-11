# mysql db shenanigans

# imports
from getpass import getpass
from mysql.connector import connect, Error
from connect.db_connect import db_connect


def main():
    # connect to mysql, create db if it does not exist
    try:
        with connect(
                host="localhost",
                user=input("Enter username: "),
        ) as connection:
            with connection.cursor(buffered=True) as cursor:
                show_db_query = "SHOW DATABASES"
                cursor.execute(show_db_query)
                for db in cursor:
                    db_str = str(db)
                    test = "('discord_user_scores',)"
                    if db_str == test:
                        nuke_db = "DROP DATABASE discord_user_scores"
                        cursor.execute(nuke_db)
                        print("Purging old database...")
                        break
                create_db = "CREATE DATABASE discord_user_scores"
                cursor.execute(create_db)
                use_db = "USE discord_user_scores"
                cursor.execute(use_db)
                print("New database created")
                create_score_table = """
                    CREATE TABLE discord_scores(
                    name CHAR(20),
                    score INT, 
                    time DATETIME
                  )
                """
                cursor.execute(create_score_table)
                connection.commit()
                print("Bootstrap complete")

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
