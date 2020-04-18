#!/usr/bin/env python3
import requests


class Dirbuster():

    def __init__(self, domain):
        self.domain = domain
        self.file = 'web-services.txt'


    def wordlist(self):
        print("extra/dirbuster Module running...")
        l = ['ServiceDefinition', 'admin', 'atom', 'axis', 'context', 'default', 'disco', 'extwsdl', 'index', 'inquire', 'inquiryapi', 'inspection', 'interface', 'interfaces', 'jboss-net', 'jbossws', 'juddi', 'manual', 'methods', 'name', 'names', 'operation', 'operations', 'oracle', 'proxy', 'publish', 'publishing', 'query', 'rss', 'service', 'services', 'svce', 'uddi', 'uddiexplorer', 'uddigui', 'uddilistener', 'uddisoap', 'webservice', 'webserviceclient', 'webserviceclient+ssl', 'webservices', 'ws', 'ws4ee', 'wsatom', 'wsdl', 'wsgw', 'wsil', 'xmethods\n']
        dirs = []
        for i in l:
            try:
                response = requests.get('http://' + self.domain + '/' + i).status_code
                if response == 200:
                    # print('[*] Valid Path Found: /%s' % (i))
                    dirs.append(i)
                else:
                    pass

            except Exception as err:
                print(f'[!] Error: An Unexpected Error Occured! We might got blocked...- {err}')
                break

        with open(self.file, 'a') as f:
            for i in dirs:
                full = f"http://{self.domain}.{i}"
                f.write("%s\n" % full)
        f.close()
        print(f"[*] Creating {self.file} file [*]")

# test = Dirbuster("domain.com")
# test.wordlist()