#!/usr/bin/env python3
from xlwt import Workbook
from services import userage
from googlesearch import search
import time



class Dorks():

    def __init__(self, domain):
        self.domain = domain
        self.create = Workbook()
        self.all_files = self.create.add_sheet(self.domain)


    def create_file(self):
        create = self.create
        sheet = self.all_files


        def pptx():
            time.sleep(25)
            query = f"ext:ppt OR ext:pptx OR ext:key {self.domain}"
            pptx_list = []
            for j in search(query, start=0, num=25, stop=30, pause=20, user_agent=userage.useragents()):
                pptx_list.append(j)
            # print(pptx_list)
            self.all_files.write(0, 0, 'PPTX')
            row = 1
            column = 0
            pptx_to_excel = pptx_list
            # print(pptx_to_excel)
            for file in pptx_to_excel:
                self.all_files.write(row, column, file)
                row += 1
            # print("finished pptx loop")


        def pdf():
            time.sleep(25)
            query = f"ext:pdf {self.domain}"
            pdf_list = []
            for j in search(query, start=0, num=25, stop=30, pause=20, user_agent=userage.useragents()):
                pdf_list.append(j)
            # print(pdf_list)
            self.all_files.write(0, 1, 'PDF')
            row = 1
            column = 1
            pdf_to_excel = pdf_list
            # print(pdf_to_excel)
            for file in pdf_to_excel:
                self.all_files.write(row, column, file)
                row += 1
            # print("finished pdf loop")

        def docx():
            time.sleep(25)
            query = f"ext:doc OR ext:docx {self.domain}"
            docx_list = []
            for j in search(query, start=0, num=25, stop=30, pause=20, user_agent=userage.useragents()):
                docx_list.append(j)
            # print(docx_list)
            self.all_files.write(0, 2, 'DOCX')
            row = 1
            column = 2
            docx_to_excel = docx_list
            # print(docx_to_excel)
            for file in docx_to_excel:
                self.all_files.write(row, column, file)
                row += 1
            # print("finished docx loop")

        def xlsx_csv():
            time.sleep(25)
            query = f"ext:xls OR ext:xlsx OR ext:csv {self.domain}"
            xlsx_csv_list = []
            for j in search(query, start=0, num=25, stop=30, pause=20, user_agent=userage.useragents()):
                xlsx_csv_list.append(j)
            # print(xlsx_csv_list)
            self.all_files.write(0, 3, 'XLSX/CSV')
            row = 1
            column = 3
            xlsx_csv_to_excel = xlsx_csv_list
            # print(xlsx_csv_to_excel)
            for file in xlsx_csv_to_excel:
                self.all_files.write(row, column, file)
                row += 1
            # print("finished xlsx_csv loop")


        def save_file():
            print(f"[*] Creating {self.domain} - google_files.xls [*]")
            self.create.save(f'{self.domain} - google_files.xls')

        print("extra/dorks Module running...")
        pptx()
        pdf()
        docx()
        xlsx_csv()
        save_file()



# test = Dorks("domain.com")
# test.create_file()