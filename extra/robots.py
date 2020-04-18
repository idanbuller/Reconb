#!/usr/bin/env python3
import requests


class Robots():

    def __init__(self, domain):
        self.domain = domain
        self.url = f"http://www.{self.domain}"
        self.robot = f"{self.url}/robots.txt"
        self.folders = []
        self.file = "robots.txt"


    def get_robots(self):
        print("extra/robots Module running...")
        folders = []
        resp = requests.get(f"{self.robot}").text.splitlines()
        for line in resp:
            if (line.startswith('Disallow') or line.startswith('allow')):
                line = list(filter(None, line.split(' ')))
                folders.append(line[-1])
        self.folders = folders
        with open(self.file, 'a') as f:
            print("[*] Creating robots.txt file [*]")
            for i in folders:
                if "/" in i:
                    f.write("%s\n" % i)

# test = Robots("domain.com")
# # test.get_robots()