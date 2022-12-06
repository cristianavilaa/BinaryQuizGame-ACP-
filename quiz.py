import random
import time
import sqlite3

conn = sqlite3. connect( 'profile.db' )
c = conn.cursor()

def banner():
    a = print("""|---------------------------------------|
|                                       |
|                                       |
|              *BINARY QUIZ*            |
|                ~OMEYAA~               |
|                                       |
|---------------------------------------|

    [ 1 ] Login
    [ 2 ] Create Account
    [ 3 ] Leaderboard
    [ 4 ] Exit
    """)

banner()
while True:
    time.sleep(2)
    pick = input("Enter Number : ")
    if pick == '1':
        def login():
            time.sleep(1)
            while True:
                print("""\n|-----------------------------------------|
|                                         |
|                 LOGIN                   |
|                                         |
|-----------------------------------------|
                                """)
                uname = input("\nEnter Username : ")
                passw = input("Enter Password : ")

                log = "SELECT * FROM info WHERE username = ? and password = ?"
                c.execute(log,(uname,passw))
                if c.fetchall():
                    while True:
                        time.sleep(1)
 print("""\n|-----------------------------------------|
|                                         |
|                                         |
|           [ 1 ] Play                    |
|           [ 2 ] Profile                 |
|           [ 3 ] Exit                    |
|                                         |
|                                         |
|-----------------------------------------|
                    """)
                        pick1 = input("Enter Number : ")
                        if pick1 == '1':                       
