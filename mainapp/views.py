from fileinput import FileInput
from django.shortcuts import render

# Create your views here.
import pytesseract # for OCR purpose to extract text from image 
                    # (Important- download pytesseract.exe and intall in the project root folder)

from PIL import Image # pil for image operation (open image,etc..)

import docx # for converting text to word-fle(docx)

from fpdf import FPDF # for converting text to pdf file(.pdf)


def index(request):
    # OCR scanning statement
    if request.method=='POST':
        fileimage=request.FILES['file-image']
        print(fileimage)

        # for OCR purpose to extract text from image 
        # (Important- download pytesseract.exe and intall in the project root folder)
        pytesseract.pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'
        img=Image.open(fileimage) # read user input image
        text=pytesseract.image_to_string(img) # convert input image to text using pytesseract library
        print(text)
        print('succes')

        if text == '' or len(text) == 0 : #check image scanned text is null and length is zero
            print('Invalid Image')
            return render(request,'index.html',{'invalid':'Invalid Image - Please Upload a valid image'})
        else:
            # creating docx file
            #2. ASCII-text to txt using python inbuilt file operation libraries
            file = open('static/output.txt','w') #reading file in writing mode
            file.write(str(text)) #writiing method to write that text
            file.close() #close method to save and close
            return render(request,'outputpage.html',{'success':text})
           
    return render(request,'index.html',{})

# word converter logic
def word_converter(request):

    #1. open docx file from static folder - for reading OCR converted text
    txt_file = open('static/output.txt','r')
    print(txt_file,'file text')

    #2. creating empty document
    doc=docx.Document() #creating empty document

    for line in txt_file: #got the line by line-text from output.txt file
        # print(txt_text,'file')
        # print(type(txt_text),'type')

        #2. converting docx file
        # text to docx coverting, library - pip install python-docx
        # import docx /////////////////////////////////////////////////
        doc.add_paragraph(line) #adding string paragrap
        doc.save('static/output.docx') # saving the document file
        # ////////////////////////////////////////////////

    print('word file created')

    return render(request,'outputpage.html',{'word':'word'})

# pdf converter logic
def pdf_converter(request):

    try:
        # 1. reading text file
        txt_file = open('static/output.txt','r') #opening text file from static folder

        # 2. assigning 
        # text to pdf coverting, library - pip install fpdf
        # from fpdf import FPDF //////////////////////////////////////////////
        pdf = FPDF() #creating object
        pdf.add_page() #adding page using object
        pdf.set_font('Arial', size=14) #setting fonts and size
        
        for line in txt_file: #got the line by line-text from output.txt file
            pdf.cell(200, 10, txt=line, ln=1, align='C') #creating pdf with parameters(width,line-height,etc...)

        pdf.output('static/output.pdf') #saving the pdf file
        print('PDF Created')
        return render(request,'outputpage.html',{'pdf':'pdf'})

    except:
        print('Could not create PDF')
        return render(request,'outputpage.html',{'try_exception':'none'})
