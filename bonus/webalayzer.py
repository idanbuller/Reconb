import webtech
from prettytable import PrettyTable

class Webalayzer():

    def __init__(self, domain):
        self.domain = domain
        self.url = f"https://{domain}"

    def web(self):
        try:
            x = PrettyTable()
            x.field_names = ["Name", "Version", "Module"]
            wt = webtech.WebTech(options={'json': True, 'random-user-agent': True})
            report = wt.start_from_url(self.url)
            for i in range(len(report['tech'])):
                x.add_row([f"{report['tech'][i]['name']}", f"{report['tech'][i]['version']}", "WebTech"])
            for i in range(len(report['headers'])):
                x.add_row([f"{report['headers'][i]['name']}", f"{report['headers'][i]['value']}", "WebTech"])
            print(x)

        except webtech.utils.ConnectionException:
          print("Connection error")

#
# test = Webalayzer("domain.com")
# test.web()
