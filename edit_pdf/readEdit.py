import PyPDF2
import os

os.chdir('/home/lenny/portofolio')

pdfFile = open('investigacion_ANN_lol.pdf', 'rb')

reader = PyPDF2.PdfReader(pdfFile)

print(len(reader.pages)) #Getting the number of pages of a pdf requires the use of len() function

#We can use this functionality in a for loop in order of getting the whole text in a pdf 

page = reader.pages[0]

#print(page.extract_text())


#In order of writting pages in a pdf...
pdfFile2 = open('Neutral Minimalist Professional Resume.pdf' , 'rb')
reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader.pages)):
    page = reader.pages[pageNum]
    writer.add_page(page)

outputFile = open('combinedPDF.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFile2.close()
