#! python3
# pdfParanoia.py - searches for all PDFs and encryptes the pdffiles
# pdf files should be added to the original file location

import PyPDF2, os.path, logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

location = '.\\Chapter13\\pdfFiles\\'
# walk through file to locate all PDFs
pdf_list = []

switch = 'decrypt'

if switch == 'encrypt':
    for folders, subfolders, files in os.walk(location):
        for file in files:
            if file.endswith(".pdf"):
                location = os.path.join(folders, file)
                # encrypt PDF files '_encrypted'
                pdfFile = open(location, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if not pdfReader.isEncrypted:
                    print('Encrypting PDF... %s' % location)
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    pdfWriter.encrypt('test')
                    # file name _encrypted
                    encryptedLocation = os.path.join(folders, file.replace('.pdf', '') + '_encrypted.pdf')
                    encryptedPdf = open(encryptedLocation, 'wb')
                    pdfWriter.write(encryptedPdf)
                    encryptedPdf.close()

elif switch == 'decrypt':
    for folders, subfolders, files in os.walk(location):
        for file in files:
            if file.endswith('.pdf'):
                location = os.path.join(folders, file)
                pdfFile = open(location, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted:
                    pdfReader.decrypt('test')
                    pdfWriter = PyPDF2.PdfFileWriter()
                    try:
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                            decryptedLocation = os.path.join(folders, file.replace('_encrypted.pdf', '') + '_decrypted.pdf')
                            decryptedPdf = open(decryptedLocation, 'wb')
                            pdfWriter.write(decryptedPdf)
                            decryptedPdf.close()
                        print('Decrypting PDF... %s' % location)
                    except:
                        logging.critical('Decrypting FAILED... %s' % location)
                        break
