#!/usr/bin/env python3
import re
import requests
import json


class Pwndb:

    def __init__(self, domain):

        self.__url = "http://pwndb2am4tzkvold.onion/"
        self.__data = {"domain": domain, "luseropr": 1, "domainopr": 1, "submitform": "em"}
        self.__session = requests.session()
        self.__session.proxies = {
            "http": "socks5h://localhost:9050",
            "https": "socks5h://localhost:9050"
        }

    def response_parser(self):
        try:
            print("extra/onion Module running...")
            resp = self.__session.post(self.__url, data=self.__data, timeout=(15, None))

            if resp.status_code == 200:
                respons = resp.text
            else:
                print("[*] pwndb2am4tzkvold.onion can not be reached [*]")
                return None

            resp = re.findall(r"\[(.*)", respons)
            resp = [resp[n: n + 4] for n in range(0, len(resp), 4)]
            results = {}
            getinfo = lambda s: s.split("=>")[1].strip()
            for item in resp:
                results[getinfo(item[0])] = {
                    "email": f"{getinfo(item[1])}@{getinfo(item[2])}",
                    "passw": getinfo(item[3])
                }
            results = {k: v for k, v in results.items() if v['email'] != 'donate@btc.thx'}
            to_file = json.loads(results)
            with open('passwords.txt', 'a') as f:
                f.write(to_file)
            f.close()
            print("[*] Creating passwords.txt file [*]")

        except Exception as err:
            raise err

# test = Pwndb("domain.com")
# test.response_parser()