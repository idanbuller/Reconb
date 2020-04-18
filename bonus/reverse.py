#!/usr/bin/env python3
import socket
import threading
from queue import Queue
import mysql.connector
import keys

class Reverse:
    def __init__(self, domain):
        print("people/reverse Module running...")
        self.domain = domain
        self.table = self.domain.replace(".", "")
        socket.setdefaulttimeout(0.25)
        self.print_lock = threading.Lock()
        self.nnet = []
        self.resolved = {}
        self.addrlist = []

    def gen_list(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user=f"{keys.mysql_username}",
            passwd=f"{keys.mysql_password}",
            database="reconb"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT Ip FROM {self.table}_services")
        myresults = mycursor.fetchall()
        ipaddreess = [row[0] for row in myresults]
        networks = {}
        for i in ipaddreess:
            i = i.split('.')
            subnet = f'{i[0]}.{i[1]}.{i[2]}.0'
            if subnet not in networks:
                networks[subnet] = 0
            elif subnet in networks:
                networks[subnet] += 1
        for sub in networks:
            if networks[sub] > 3:
                for i in range(1,255):
                    addr = (f'{sub[:-1]}{i}')
                    self.addrlist.append(str(addr))
        return self.addrlist

    def run(self, addr):
        try:
            self.resolve = socket.gethostbyaddr(addr)
            with self.print_lock:
                #if f"{self.domain}" in self.resolve[0]:
                    #print(self.resolve[0])
                # print('[*] Addr: {:<20} Host: {:<20}'.format(addr, self.resolve[0]))
                self.resolved[self.resolve[0]] = addr
        except Exception as e:
           pass


    def threader(self):
        while True:
            worker = self.q.get()
            self.run(worker)
            self.q.task_done()


    def to_db(self):
        name = self.domain.split('.')
        reverse_dict = {}
        for i in self.resolved:
            if f"{name[0]}" in f"{i}":
                addr = socket.gethostbyname(i)
                reverse_dict[i] = addr
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=f"{keys.mysql_username}",
                passwd=f"{keys.mysql_password}",
                database="reconb"
            )
            mycursor = mydb.cursor()
            for key, value in reverse_dict.items():
                sql = f"INSERT INTO {self.table}_services (Subdomain, Ip, Oports, ModuleName) VALUES (%s, %s, %s, %s)"
                val = (key, value, 'null', 'Reverse')
                mycursor.execute(sql, val)
                mydb.commit()
        except mysql.connector.Error as err:
            print(f'MySQL Error: {err}')

        finally:
            print(f"Reverse added to table")


    def main(self):
        self.addrlist = self.gen_list()
        self.q = Queue()

        for x in range(100):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()

        for l in self.addrlist:
            self.q.put(l)

        self.q.join()

        self.to_db()

# test = Reverse("domain.com")
# test.main()
