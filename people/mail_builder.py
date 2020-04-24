#!/usr/bin/env python3
from people import pattern_api
import mysql.connector
import keys


class Mail_builder():

    def __init__(self, domain):
        self.domain = domain
        self.table = self.domain.replace(".", "")
        self.pattern = pattern_api.Pattern(self.domain).pattern()


    def builder(self):
        try:
            print("people/mail_builder Module running...")
            mydb = mysql.connector.connect(
                host="localhost",
                user=f"{keys.mysql_username}",
                passwd=f"{keys.mysql_password}",
                database="reconb"
            )
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT Name FROM {self.table}_workers")
            myresult = mycursor.fetchall()
            names = [row[0] for row in myresult]
            for name in names:
                if self.pattern == "{first}{last}":
                    first = name.split(" ")[0]
                    last = name.split(" ")[1:-1]
                    mail = f"{first}{last}@{self.domain}"

                elif self.pattern == "{first}.{last}":
                    first = name.split(" ")[0]
                    last = name.split(" ")[1:-1]
                    mail = f"{first}.{last}@{self.domain}"

                elif self.pattern == "{first}_{last}":
                    first = name.split(" ")[0]
                    last = name.split(" ")[1:-1]
                    mail = f"{first}_{last}@{self.domain}"

                elif self.pattern == "{last}{f}":
                    last = name.split(" ")[1:-1]
                    f = name[0]
                    mail = f"{last}{f}@{self.domain}"

                elif self.pattern == "{first}{l}":
                    first = name.split(" ")[0]
                    l = name.split(" ")[1:-1][0]
                    mail = f"{first}{l}@{self.domain}"

                elif self.pattern == "{last}{first}":
                    first = name.split(" ")[0]
                    last = name.split(" ")[1:-1]
                    mail = f"{last}{first}@{self.domain}"

                new_mail = mail.replace("[]", "")
                sql = f"UPDATE {self.table}_workers SET PossiblEmail = '{new_mail}' WHERE Name = '{name}'"
                mycursor.execute(sql)
                mydb.commit()
        except Exception as e:
            print(f"API Error: {e}")

        finally:
            pass


# test = Mail_builder("domain.com")
# test.builder()
