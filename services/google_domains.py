#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import socket
import mysql.connector
import keys


class Google():

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


    def get_subs(self):
        print("services/google_domains Module running...")
        sdomains = []
        for start in range(0,50):
            try:
                url = f"http://www.google.com/search?q=site:{self.domain} -www.{self.domain}"
                html = requests.get(url, headers=self.headers)
                if html.status_code == 429:
                    print("To many requests!")
                    print("Exiting...")
                    pass
                soup = BeautifulSoup(html.text, 'html.parser')
                links = soup.findAll('div', {'class' : 'BNeawe UPmit AP7Wnd'})
                for link in links:
                    link = link.text.split('://')
                    if link not in sdomains:
                        sdomains.append(link[-1])
                        url += f"-site:'{link}'"
            except requests.exceptions.ConnectionError as e:
                print(f"Connection refused: {e}")

        try:
            google_dict = {}
            for sub in sdomains:
                try:
                    addr = socket.gethostbyname(sub)
                    google_dict[sub] = addr
                except socket.error as e:
                    print(f"socket error: {e}")
            mydb = mysql.connector.connect(
                host="localhost",
                user=f"{keys.mysql_username}",
                passwd=f"{keys.mysql_password}",
                database="reconb"
            )
            mycursor = mydb.cursor()
            for key, value in google_dict.items():
                sql = f"INSERT INTO {self.table}_services (Subdomain, Ip, ModuleName) VALUES (%s, %s, %s)"
                val = (key, value, 'Google')
                mycursor.execute(sql, val)
                mydb.commit()
        except Exception as e:
            print(f'Cannot resovle: {e}\nConsider change your cookies')
        finally:
            print(f"Google added to table")


# test = Google("domain.com")
# test.get_subs()