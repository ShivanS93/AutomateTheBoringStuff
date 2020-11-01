#! python3
# txtToSpeadsheet.py - makes txt files for this example
# Shivan Sivakumaran 22/06/2020

import openpyxl, logging, os

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s '
                                               '- %(message)s')
# logging.disable(logging.CRITICAL)

# get a list of all text files
files = os.listdir()
txt_files = []

path = 'Chapter12\\txtToSpreadsheet'

for file in files:
    if file.endswith('.txt'):
        txt_files.append(file)

logging.debug(txt_files)

wb = openpyxl.Workbook()
sheet = wb.active

# read text files using readlines()
for i in range(len(txt_files)):
    file_read = open(os.path.join(path, txt_files[i]), 'r')
    txt = file_read.readlines()

    # save into spreadsheet txt
    for j in range(len(txt)):
        sheet.cell(row=j+1, column=i+1).value = txt[j]

wb.save(os.path.join(path, 'txtToSpreadSheet.xlsx'))