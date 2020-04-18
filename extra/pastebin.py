#!/usr/bin/env python3
from random import randint
import googlesearch
from services import userage

class Pastes:

    def __init__(self, domain):
        self.__domain = domain
        self.__user_agent = userage.useragents()
        self.__delay = randint(3, 8)
        self.__search_max = 25
        self.file = f'pastebin.txt'


    def searcher(self):
        print("extra/pastebin Module running...")
        final = []
        query = f"inurl:pastebin.com AND intext:{self.__domain}"
        try:
            results = [url for url in googlesearch.search(
                query, num=self.__search_max, start=0,
                stop=self.__search_max, pause=self.__delay, extra_params={"filter": "0"}, user_agent=self.__user_agent)]
            final.extend(results)
        except Exception as err:
            raise err
        # print(final)
        with open(self.file, 'a') as f:
            print("[*] Creating pastebin.txt file [*]")
            for i in final:
                if "pastebin.com" in i:
                  f.write("%s\n" % i)
            f.close()



# test = Pastes("domain.com")
# test.searcher()