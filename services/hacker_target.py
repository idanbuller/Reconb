#!/usr/bin/env python3
import mysql.connector
import requests
from queue import Queue
import keys


class Hackertarget():

    def __init__(self, domain):
        self.domain = domain
        self.table = self.domain.replace(".", "")
        self.url = 'https://api.hackertarget.com/hostsearch/?q=' + self.domain
        self.q = Queue()

    def get_subs(self):
        try:
            print("services/hacker_target Module running...")
            hackertarget_dict = {}
            req = requests.get(self.url)
            res = req.text
            res = res.split("\n")
            for s in res:
                to_db = s.split(",")
                to_subs = to_db[0]
                to_ip = to_db[1]
                hackertarget_dict[to_subs] = to_ip
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user=f"{keys.mysql_username}",
                    passwd=f"{keys.mysql_password}",
                    database="reconb"
                )
                mycursor = mydb.cursor()
                for key, value in hackertarget_dict.items():
                    sql = f"INSERT INTO {self.table}_services (Subdomain, Ip, Oports, ModuleName) VALUES (%s, %s, %s, %s)"
                    val = (key, value, 'null', 'HackerTarget')
                    mycursor.execute(sql, val)
                    mydb.commit()
            except mysql.connector.Error as e:
                print(f"MySQL Error: {e}")
        except requests.ConnectionError as err:
            print(f'hackertarget.com API is not responding. \n Error: {err}')
        finally:
            print(f"HackerTarget added to table")

# test = Hackertarget("domain.com")
# test.get_subs()

