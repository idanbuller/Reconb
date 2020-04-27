#!/usr/bin/env python3
from services import hacker_target, google_domains, banner, brute_force
from people import hunter_io, mail_builder, linkedin
from extra import dorks, vt, pastebin, web_services, robots, admin_panels
from bonus import wappalyzer, reverse, webalayzer
import mysql.connector, csv, validators
from prettytable import PrettyTable
from tabulate import tabulate
import keys


class Reconb():

    def __init__(self):
        self.domain = user_input

    def create_db_services(self):
        print(f"[*] Creating table {table_name1}_services [*]")
        mycursor.execute(
            f"CREATE TABLE {table_name1}_services (id INT AUTO_INCREMENT PRIMARY KEY, Subdomain VARCHAR(255), ip VARCHAR(255), Oports VARCHAR(255), ModuleName VARCHAR(255))")

    def hackertarget(self):
        hacker_target.Hackertarget(self.domain).get_subs()

    def brute_force(self):
        brute_force.main(self.domain, table_name1)

    def google(self):
        google_domains.Google(self.domain).get_subs()

    def reverse(self):
        reverse.Reverse(self.domain).main()

    def create_db_workers(self):
        print(f"[*] Creating table {table_name2}_workers [*]")
        mycursor.execute(
            f"CREATE TABLE {table_name2}_workers (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), JobTitle VARCHAR(255), Email VARCHAR(255), EmailVerify VARCHAR(255), PossiblEmail VARCHAR(255), ModuleName VARCHAR(225))")

    def linkedin(self):
        linkedin.Linkedin(self.domain)

    def hunter(self):
        hunter_io.Mails(self.domain, keys.hunter).mail_hunter()
        hunter_io.Mails(self.domain, keys.hunter).google_mail()
        # Can be separated

    def pattern(self):
        mail_builder.Mail_builder(self.domain).builder()

    def wappalyzer(self):
        webalayzer.Webalayzer(self.domain).web()
        wappalyzer.Wappalyzer(self.domain).wap()

    def extra(self):
        vt.VirusTotal(self.domain, keys.virus_total).fileSearch()
        pastebin.Pastes(self.domain).searcher()
        robots.Robots(self.domain).get_robots()
        # onion.Pwndb(self.domain).response_parser() only with tor service open! Not imported
        busting = str(input(">> Would you like Reconb to bust for web-services & admin-panels on site? This is very active... [Y/n]"))
        if busting.lower() == "y":
            web_services.Dirbuster(self.domain).wordlist()
            admin_panels.Panels(self.domain).wordlist()
        elif busting.lower() == "n":
                pass
        else:
            print("Unknown option, Please choose again!")
        dorker = str(input(">> Would you like Reconb to dork for files? It might take some time... [Y/n]"))
        if dorker.lower() == "y":
            dorks.Dorks(self.domain).create_file()
        elif dorker.lower() == "n":
            pass
        else:
            print("Unknown option, Please choose again!")


preT = PrettyTable()
print(banner.banner)
preT.field_names = ["[*] We1c0me T0 Reconb [*]", "No."]
preT.add_row(["Domain-Subdomain-Ip search", "1"])
preT.add_row(["People Search", "2"])
preT.add_row(["Files & Leaks & Busting", "3"])
preT.add_row(["Open ports for Oports", "4"])
preT.add_row(["Wappalyzer", "5"])
preT.add_row(["Show all past scannings", "6"])
preT.add_row(["Show table results", "7"])
preT.add_row(["Export data to (csv)", "8"])
preT.add_row(["Exit", "q"])
print(preT)


while True:
    mydb = mysql.connector.connect(
        host="localhost",
        user=f"{keys.mysql_username}",
        passwd=f"{keys.mysql_password}",
        database="reconb"
    )
    mycursor = mydb.cursor()
    user_choice = str(input(">>  m = menu\n\tb = back\nEnter your choise:"))

    if user_choice == '1':
        user_input = str(input(">> Enter Domain Name here: "))
        if user_input.lower() == "b":
            continue
        elif validators.url(f"http://{user_input}"):
            table_name1 = user_input.replace(".", "")
            test = Reconb()
            test.create_db_services()
            test.hackertarget()
            test.brute_force()
            test.google()
            test.reverse()
        else:
            print("[*] Domain Not Valid! Come on, you can do better... [*]")

    if user_choice == "2":
       user_input = str(input(">> Enter Domain Name here: "))
       if user_input.lower() == "b":
           continue
       elif validators.url(f"http://{user_input}"):
           table_name2 = user_input.replace(".", "")
           test = Reconb()
           test.create_db_workers()
           test.linkedin()
           test.hunter()
           pattern = str(input(f">> Reconb manged to detect the mail pattern of {user_input}\n Would you like to use it for all the company workers? [Y/n]"))
           if pattern.lower() == "y":
               test.pattern()
           elif pattern.lower() == "n":
               pass
       else:
            print("[*] Domain Not Valid! Come on, you can do better... [*]")

    elif user_choice == "3":
        user_input = str(input(">> Enter Domain Name here: "))
        if user_input.lower() == "b":
            continue
        elif validators.url(f"http://{user_input}"):
            test = Reconb()
            test.extra()
        else:
            print("Domain Not Valid! Come on, you can do better...")

    elif user_choice == "4":
        from services import port_scanner

    elif user_choice == "5":
        user_input = str(input(">> Enter Domain Name here: "))
        if user_input.lower() == "b":
            continue
        elif validators.url(f"http://{user_input}"):
            test = Reconb()
            test.wappalyzer()
        else:
            print("Domain Not Valid! Come on, you can do better...")


    elif user_choice == '6':
        try:
            mycursor.execute("SHOW TABLES")
            myresult = mycursor.fetchall()
            t = PrettyTable()
            t.field_names = ["[*] Tables [*]"]
            for x in myresult:
                a = str(x).strip("('),")
                a.strip("")
                t.add_row([a])
            print(t)
        except mysql.connector.errors.Error as e:
            print(f"Mysql Error: {e}")
        finally:
            pass

    elif user_choice == '7':
        table = str(input(">> Enter table name: "))
        if table.lower() == "b":
            continue
        try:
            sql = f"SELECT * FROM {table}"
            mycursor.execute(sql)
            results = mycursor.fetchall()
            print(tabulate(results, tablefmt='psql'))
        except mysql.connector.errors.Error as e:
            print(f"Mysql Error: {e}")
        finally:
            pass

    elif user_choice == "8":
        export = str(input(">> Enter table name: "))
        if export.lower() == "b":
            continue
        try:
            mycursor.execute(f"SELECT * FROM reconb.{export}")
            with open(f"{export}.csv", "w") as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(col[0] for col in mycursor.description)
                for row in mycursor:
                    writer.writerow(row)
        except mysql.connector.errors.Error as e:
            print(f"Mysql Error: {e}")
        finally:
            print(f"File {export}.csv created!")
            pass

    elif user_choice.lower() == "q":
        quit()

    elif user_choice.lower() == "m":
        print(preT)

    else:
        print("Unknown module, Please choose again!")
