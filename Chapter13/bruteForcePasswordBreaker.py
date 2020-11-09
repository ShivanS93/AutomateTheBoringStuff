#! python3
# bruteForcePasswordBreaker.py - decryptes pdf by bruteforce using the english language

import PyPDF2

file = 'Chapter13\\combinedminutes_encrypted.pdf'

# access words from dictionary
wordsFile = open('Chapter13\\dictionary.txt', 'r')
words = wordsFile.read().splitlines()
words = [word.lower() for word in words]

# try passwords to decrypt pdf
pdfFile = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
if pdfReader.isEncrypted:
    for word in words:
        if pdfReader.decrypt(word) == 1:
            print("Hacked with %s"%word)
            pdfReader.decrypt(word)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                decryptedPdf = open(file + '_hacked.pdf', 'wb')
                pdfWriter.write(decryptedPdf)
                decryptedPdf.close()
                exit()
        else:
            print('failed hack with %s'%word)