import pytesseract as ta

img_path = input("enter png path : \n")
output_path = input("enter output name (exclude .pdf) : \n")

config = ('-l kor+eng --oem 3 --psm 11')
pdf = ta.image_to_pdf_or_hocr(f'{img_path}', extension='pdf')
with open(f'{output_path}.pdf', 'w+b') as f:
    f.write(pdf)
    
