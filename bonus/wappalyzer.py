#!usr/bin/env python3
import requests

class Wappalyzer():
    def __init__(self, domain):
        self.domain = domain


    def wap(self):
        try:
            url = f"https://whatcms.org/APIEndpoint/Technology?key=2827e2da9581dd1b2eee3fd987936ad7f5e582a6408a0e2150c32abd7ac2c424bab8a9&url={self.domain}"
            obj_urldata = requests.get(url)  # gets the url data
            obj_json = obj_urldata.json()  # data which in json format into compatibiliy for python
            res = obj_json['results']  # selecting a section of data

            res0 = res[0]  # selecting categories from the results data like name
            print("CMS name: " + res0['name'])
            if res0['version'] == "":  # if version data of version is not given
                print("version :" + "not provided")
            else:  # if given
                print("version: " + res0['version'])
            res1 = res[1]  # selecting categories onf the results data like programming
            print("programming technology: " + res1['name'])
            if res1['version'] == "":
                print("version :" + "not provided")
            else:
                print("verion: " + res1['version'])

            res2 = res[2]  # selecting categories onf the results data like server
            print("server: " + res2['name'])
            if res2['version'] == "":
                print("version :" + "not provided")
            else:

                print("version: " + res2['version'])

        except Exception as e:
            print(f'Cannot find {self.domain}')

