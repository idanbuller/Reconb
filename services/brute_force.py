#!/usr/bin/env python3
import dns.resolver
import mysql.connector
import concurrent.futures
import keys

def a_lookup(record):
    try:
        answers = dns.resolver.query(record, 'A')
        for ip in answers:
            return ip
    except Exception as e:
        return "0.0.0.0"


def main(domain, table):
    with open("subs.txt", "r") as f:
     file = f.read().split()
     subdomains = []
    for line in file:
        subdomains.append(line.strip() + "." + domain)

    records = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_ip = {executor.submit(a_lookup, record): record for record in subdomains}
        for future in concurrent.futures.as_completed(future_to_ip):
            record = future_to_ip[future]
            try:
                records[record] = future.result()
            except Exception as e:
                print("[!] ERROR: %s" % e)

    actual_records = {}
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=f"{keys.mysql_username}",
            passwd=f"{keys.mysql_password}",
            database="reconb"
        )
        mycursor = mydb.cursor()
        for key, value in records.items():
            if "0.0.0.0" in str(value):
                continue
            else:
                actual_records[key] = str(value)
            sql = f"INSERT INTO {table}_services (Subdomain, Ip, ModuleName) VALUES (%s, %s, %s)"
            val = (key, value, 'Bruteforce')
            mycursor.execute(sql, val)
            mydb.commit()
    except mysql.connector.errors.Error as e:
        print(f"Mysql Error: {e}")
    finally:
        print(f"bruteforce added to table")


# main("domain.com", "table")