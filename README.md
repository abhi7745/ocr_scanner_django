# OCR Scanner Application
 
This application will helps to scan image easy.

## Features

* One click to scan image.

* The scanned text to convert into txt, docx, pdf.


# Dependencies

## Tesseract installer for Windows.

* Important- download pytesseract.exe and intall in the project root folder

* Tesseract at UB Mannheim OCR [download](https://github.com/UB-Mannheim/tesseract/wiki)

## Download Tesseract CLI into Virtual Environment.

* Make sure your virtual environment is activated.

```shell
pip install pytesseract
```

* Importing in views.py like.
```python
import pytesseract
```

# Example View.py.

```python
import pytesseract
from PIL import Image

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
```