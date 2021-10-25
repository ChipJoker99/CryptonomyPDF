from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt(input_file, password):
    pdf = PdfFileReader(input_file)
    writer = PdfFileFileWriter()
    for n in range (pdf.getNumPages()):
        page = pdf.getPage(n)
        writer.addPage(page)

    writer.encrypt(password)

    with open('encrypted_' + input_file, 'wb') as output_file:
        writer.write(output_file)

encrypt('file.pdf', 'password')
