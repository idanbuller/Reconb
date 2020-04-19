#!/usr/bin/env python3
import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from validate_email import validate_email
import mysql.connector
import keys

class Mail_scrap():

    def __init__(self, domain):
        self.domain = domain
        self.table = self.domain.replace(".", "")
        self.headers = {
                        'Host': 'www.google.com',
                        'User-Agent': 'Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like Gecko',
                        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Referer': 'https://www.google.com/',
                        'Cookie': 'CGIC=CgtmaXJlZm94LWItZSI_dGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksKi8qO3E9MC44; 1P_JAR=2020-03-29-15; NID=198=qZ0LFNCNIKv7I93QnRy1OTPWf4Nf1yl26mJ2eIj0w9mVmc1Paq6ZXazwmbMjyA_cjDDZSgN1IiDZiuogFzQe3Ndgt1Cn3V-UWhyAt'
                        }

    def google_mail(self):
        try:
            url = f"http://www.google.com/search?q=intext:@{self.domain}"

            unprocessed_urls = deque([url])

            processed_urls = set()

            emails = set()

            print("people/google_intext Module running...")
            while len(unprocessed_urls):

                url = unprocessed_urls.popleft()
                processed_urls.add(url)

                parts = urlsplit(url)
                base_url = "{0.scheme}://{0.netloc}".format(parts)
                path = url[:url.rfind('/') + 1] if '/' in parts.path else url

                try:
                    response = requests.get(url, headers=self.headers)
                except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                    continue


                new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
                # print(new_emails)
                mydb = mysql.connector.connect(
                    host="localhost",
                    user=f"{keys.mysql_username}",
                    passwd=f"{keys.mysql_password}",
                    database="reconb"
                )
                mycursor = mydb.cursor()
                if len(new_emails) != 0:
                    for email in new_emails:
                        name = email.split("@")[0]
                        re_name = name.replace("." or "_", " ")
                        if validate_email(email):
                            sql = f"INSERT INTO {self.table}_workers (Name, Email, EmailVerify, ModuleName) VALUES (%s, %s, %s, %s)"
                            val = (f"*possible* - {re_name}", email, "Verifyed", "google_intext")
                            mycursor.execute(sql, val)
                            mydb.commit()
                        else:
                            sql = f"INSERT INTO {self.table}_workers (Name, Email, EmailVerify, ModuleName) VALUES (%s, %s, %s, %s)"
                            val = (f"*possible* - {re_name}", email, "Not verified", "google_intext")
                            mycursor.execute(sql, val)
                            mydb.commit()
                emails.update(new_emails)
                soup = BeautifulSoup(response.text, 'lxml')

                for anchor in soup.find_all("a"):
                    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                    if link.startswith('/'):
                        link = base_url + link
                    elif not link.startswith('http'):
                        link = path + link
                    if not link in unprocessed_urls and not link in processed_urls:
                        unprocessed_urls.append(link)

        except Exception as err:
            while err == requests.exceptions.TooManyRedirects:
                break



# test = Mail_scrap("domain.com")
# test.google_mail()
