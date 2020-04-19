#!/usr/bin/env python3
import requests
import json
import mysql.connector
import keys

MAX = 100


class Linkedin():

    def __init__(self, domain):
        print("people/linkedin Module running...")
        self.domain = domain
        self.keyword = self.domain.split(".")[0]
        self.table = self.domain.replace(".", "")
        self.companies = []
        self.headers = {'Host': 'www.linkedin.com',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
                        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'x-li-lang': 'en_US',
                        'x-li-track': '{"clientVersion":"1.6.3249","osName":"web","timezoneOffset":-4,"deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1}',
                        'csrf-token': 'ajax:0806351021154881157',
                        'x-restli-protocol-version': '2.0.0',
                        'Cookie': 'JSESSIONID="ajax:0806351021154881157"; bcookie="v=2&e0c759d4-b9f5-43ae-8981-864668ec0c87"; bscookie="v=1&20200405144324f3eb1fb8-69c7-4bdd-8e91-10569808c472AQEtiEzDrg6Ri6UXNxOuaylt-KgEIeLe"; lissc=1; _ga=GA1.2.1490716457.1586097956; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18368%7CMCMID%7C35292929217058391900453018462971877923%7CMCAAMLH-1587562163%7C6%7CMCAAMB-1587562163%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1586964563s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-1890828461; aam_uuid=34738916383890661410470167496919558632; liap=true; li_at=AQEDASoC0I8Fv6yIAAABcX4IXakAAAFxohThqU4AY259oGlFPkUqR1SEI-7sweYaISjpCy3ZP5RLmQPTsdhFjzmzsZIL9QEkC3pOvL20p1ME3GgAE5lGAvQrjFkf_spZYR1RmKuJqcYrv1xs38C3vKFi; UserMatchHistory=AQIO1iAxWP3sMAAAAXF-CHIMWuObY7p3OEnmqFOc5HrWgqw6T_3MzOQuZdxCkhpUw7cmTssKt8DS4OuDmmspdaoD2adcpWOo9eZp2G-AQHZ6X7UnhwY3C2yp3ggPGHHEsD1ojB900VAfElD5LWEmICPsLXvc8KQOJZm7jBpxiQsd-yOtkUJ4qlP9dYXAYuwT2WyHbQ; li_sugr=bcb171e2-af51-429c-b101-730f33ce04d0; UserMatchHistory=AQL9GY3VJnjy5QAAAXF-CIAqwLI3eTyF0BJlwllGCxt1jBlMwPBh6eZHjRbbFIoExLPVS10mr2Y; li_oatml=AQH5KZj6cfAFpAAAAXF-CIL-J1mMDb0-qRWNfMJVVmISYj-UlDrTQxQwmhEgjUWGkLddXLMMhhV1VV56ICMJqA98vL67Ycwc; lidc="b=TB35:g=2889:u=154:i=1586957435:t=1587043754:s=AQFwllc01-lzo9-QObF60rpkw9mPweOI"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; lang=v=2&lang=en-us; _gat=1""")',
                        }
        self.search()

    def search(self):
        params = {
            'keywords': self.keyword,
            'origin': 'GLOBAL_SEARCH_HEADER',
            'q': 'blended'
        }
        req = requests.get('https://www.linkedin.com/voyager/api/typeahead/hitsV2', params=params, headers=self.headers)
        json_res = json.loads(req.text)

        try:
            for item in json_res['data']['elements']:
                if item['type'] == 'COMPANY':
                    self.companies.append({'Name': item['text']['text'], 'ID': item['objectUrn'].split(':')[-1]})
        except:
            pass

        if len(self.companies) > 1:
            print('Choose the correct company: ')
            i = 0
            for company in self.companies:
                print(f"[{i + 1}]  {company['Name']}")
                i += 1

            while True:
                user_choice = int(input('>> '))
                if 0 < user_choice <= len(self.companies):
                    self.collect_employees(self.companies[user_choice-1]['ID'])
                    break
                else:
                    print("Invalid option!")
        elif len(self.companies) == 1:
            self.collect_employees(self.companies[0]['ID'])
        else:
            print('Company not found.')

    def collect_employees(self, company_id):
        linkedin_dict = {}
        try:
            for page in range(0, MAX, 10):
                url = f'https://www.linkedin.com/voyager/api/search/blended?count=10&filters=List(currentCompany-%3E{company_id},resultType-%3EPEOPLE)&origin=OTHER&q=all&queryContext=List(spellCorrectionEnabled-%3Etrue,relatedSearchesEnabled-%3Etrue)&start={page}'
                req = requests.get(url, headers=self.headers)
                json_res = json.loads(req.text)
                max = json_res['data']['paging']['total']

                if page < max:
                    for item in json_res['data']['elements'][1 if page == 0 else 0]['elements']:
                        name_to_db = item['title']['text'].title()
                        job_title_to_db = item['headline']['text'].split(' at ')[0]
                        linkedin_dict[name_to_db] = job_title_to_db
                        #print(name_to_db, '-', job_title_to_db)
                else:
                    break

        except Exception as e:
            print('ERROR:', e, "Consider change your cookies")
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=f"{keys.mysql_username}",
                passwd=f"{keys.mysql_password}",
                database="reconb"
            )
            mycursor = mydb.cursor()
            for key, value in linkedin_dict.items():
                sql = f"INSERT INTO {self.table}_workers (Name, JobTitle, Email) VALUES (%s, %s, %s)"
                val = (key, value, "possible ->")
                mycursor.execute(sql, val)
                mydb.commit()
        except mysql.connector.Error as e:
            print(f"Mysql error: {e}")
        finally:
            print("linkedin module added to table")


# test = Linkedin("domain.com")
