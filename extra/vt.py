#!/usr/bin/env python3
import requests


class VirusTotal:

    def __init__(self, domain, key):
        self.domain = domain
        self.url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        self.params = {'apikey': key, 'domain': self.domain}
        self.reuslt = []
        self.file = f'VirusTotal.txt'



    def fileSearch(self):
        try:
            print("extra/vt Module running...")
            # print(f"Searching for malicious files communicating with {self.domain}.\n")
            response = requests.get(self.url, params=self.params)
            parsed_response = response.json()
            try:
                for i in parsed_response['detected_downloaded_samples']:
                    tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                    self.reuslt.append(tmp)
            except BaseException:
                pass
            try:
                for i in parsed_response['detected_referrer_samples']:
                    tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                    self.reuslt.append(tmp)
            except BaseException:
                pass
            try:
                for i in parsed_response['detected_communicating_samples']:
                    tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                    self.reuslt.append(tmp)
            except:
                pass

            if len(self.reuslt) == 0:
                print("No related malicious files found.")
            # else:
            #     print(f"Found {len(self.reuslt)} related malicious files! \n")
            #     print(self.reuslt)
            try:
                with open(self.file, 'a') as f:
                    for i in self.reuslt:
                        f.write(str(i) + '\n')
                print("[*] Creating VirusTotal.txt file [*]")
                f.close()
            except Exception as err:
                print(err)
            finally:
                pass
        except Exception as e:
            print(f"API Error: {e}")


# test = VirusTotal("domain.com")
# test.fileSearch()