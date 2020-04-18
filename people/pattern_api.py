#!/usr/bin/env python3
import requests
import json

class Pattern():

  def __init__(self, domain):
    self.domain = domain
    self.table = self.domain.replace(".", "")


  def pattern(self):
      try:
          url = f'https://hunter.io/trial/v2/domain-search?limit=10&offset=0&domain={self.domain}&format=json'
          html = requests.get(url)
          con = json.loads(html.content)
          pattern = con['data']['pattern']
          return pattern
      except Exception as e:
          print(f'hunter.io API is not responding. \n Error: {e}')

# test = Pattern("domain.com")
# test.pattern()
