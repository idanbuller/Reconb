#!/usr/bin/env python3
from queue import Queue
import socket
import threading
import mysql.connector
import keys


print("[*] Only for services table [*]")
table = str(input(">> Enter table name: "))
mydb = mysql.connector.connect(
    host="localhost",
    user=f"{keys.mysql_username}",
    passwd=f"{keys.mysql_password}",
    database="reconb"
)
mycursor = mydb.cursor()
mycursor.execute(f"SELECT ip FROM reconb.{table}")
myresult = mycursor.fetchall()
for x in myresult:
    a = str(x).strip("('),")
    a.strip("")

    target = a
    queue = Queue()
    open_ports = []

    def portscan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            return True
        except:
            return False

    def get_ports(mode):
        if mode == 1:
            for port in range(1, 1024):
                queue.put(port)
        elif mode == 2:
            for port in range(1, 49152):
                queue.put(port)
        elif mode == 3:
            ports = [20, 21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389]
            for port in ports:
                queue.put(port)
        elif mode == 4:
            ports = input("Enter your ports (seperate by blank):")
            ports = ports.split()
            ports = list(map(int, ports))
            for port in ports:
                queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            if portscan(port):
                open_ports.append(port)
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user=f"{keys.mysql_username}",
                    passwd=f"{keys.mysql_password}",
                    database="reconb"
                )
                mycursor = mydb.cursor()
                val = (str(open_ports))
                sql = f"UPDATE {table} SET Oports = '{val}' WHERE ip = '{a}'"
                mycursor.execute(sql)
                mydb.commit()
            except mysql.connector.errors.Error as e:
                print(f"Mysql Error: {e}")
            finally:
                pass


    def run_scanner(threads, mode):
        get_ports(mode)
        thread_list = []
        for t in range(threads):
            thread = threading.Thread(target=worker)
            thread_list.append(thread)
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        #print("Open ports are:", open_ports)

    run_scanner(100, 3)
print("Portscanner added to table")
