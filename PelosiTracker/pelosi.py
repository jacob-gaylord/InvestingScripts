import csv 
import json
import zipfile
import requests
import fitz
from Crypto.Cipher import AES
import tabula

zip_file_url = 'https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2022FD.ZIP'
pdf_file_url = 'https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2022/'

r = requests.get(zip_file_url)
zipfile_name = '2022.zip'

# with open(zipfile_name, 'wb') as f:
#     f.write(r.content)

# with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:
#     zip_ref.extractall('.')

# with open('2022FD.txt') as f:
#     for line in csv.reader(f, delimiter='\t'):
#         if line[1] == 'Pelosi':
#             date = line[7]
#             doc_id = line[8]

#             r = requests.get(f"{pdf_file_url}{doc_id}.pdf")

#             with open(f"{doc_id}.pdf", 'wb') as f:
#                 f.write(r.content)

doc = fitz.open('20021837.pdf')  #f"{doc_id}.pdf"
page = doc.load_page(0)
json_data = page.get_text("json")

print(json_data)