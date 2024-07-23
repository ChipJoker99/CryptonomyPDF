from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def encrypt_pdf(inputPdf, outputPdf, key):
    pdfWriter = pdfFileWriter()
    pdfReader = pdfFileReader(inputPdf)
    
    for pageNum in range (pdfReader.getNumPages()):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt(userPwd=key, ownerPwd=None, use128bit=True)

    with open(outputPdf, 'wb') as f:
        pdfWriter.write(f)

def generateKey():
    return getRandomBytes(16)

def saveKey(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def loadKey(filename):
    with open(filename, 'rb') as f:
        return f.read()

if __name__ == '__main__':
    inputPdf = 'input.pdf'
    outputPdf = 'encrypted_output.pdf'
    keyFile = 'encryption_key.key'

    key = generate_key()
    save_key(key, keyFile)

    encrypt_pdf(inputPdf, outputPdf, key)

    print(f'PDF encrypted and saved as {outputPdf}')
    print(f'Encryption key saved as {keyFile}')
