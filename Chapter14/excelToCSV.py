#! python3
# ExceltoCSV.py - converts Excel file to CSV

import os, openpyxl, csv

# os.makedirs('csvCreated', exists_ok=True)

path = ('Chapter14')

for excelFile in os.listdir('.\\Chapter14'):
    if excelFile.endswith('.xlsx'):# Skip non-xlsx files, load the workbook object
        wb = openpyxl.load_workbook(os.path.join(path, excelFile))

        for sheetName in range(len(wb.sheetnames)):
            wb.active = sheetName
            sheet = wb.active

            # Create the CSV filename from the Excel filename and sheet title
            csvFilename = os.path.basename(excelFile).replace(' ','-') + '_' + wb.sheetnames[sheetName].replace(' ','-') + '.csv'
            csvFile = open(os.path.join(path, csvFilename), 'w', newline='')
            csvWriter = csv.writer(csvFile) # Create the csv.writer object for the CSV file
            # Loop through every row in the sheet
            for rowNum in range(1, sheet.max_row+1):
                rowData = []    #append each cell to this list
                for colNum in range(1, sheet.max_column+1):
                    value = sheet.cell(row=rowNum,column=colNum).value
                    rowData.append(str(value)) #Append each cell's data to rowData.
                csvWriter.writerow(rowData)
            #write the rowData list to the CSV file.
            csvFile.close()