import os, sys
from win32 import win32print
import win32con
import win32ui

PRINT_WIDTH = 48
#
# X:Y
# 20:1.5
#
LETTER_HEIGHT_RATIO = 20
LETTER_WIDTH_RATIO = 1.5

def generate_font(size, underline):
    return win32ui.CreateFont({
    "name": "Lucida Console",
    "height": int(LETTER_HEIGHT_RATIO*(size/100)),
    "underline": underline,
})

def process_text(text, size):
    arr = []
    char_per_line = int(PRINT_WIDTH/(LETTER_WIDTH_RATIO*(size/100)))
    pages = int(len(text)/char_per_line)
    for page in range(pages+1):
        start = char_per_line*page
        end = char_per_line*(page+1)
        if end > len(text):
            end = None
            
        arr.append(text[start:end])

    return arr

text = ["09277803004","Carlyn L."]
underline = [True, False]
text_size = 280

p = win32ui.CreateDC()
printer_name = win32print.GetDefaultPrinter()
p.CreatePrinterDC(printer_name)

p.SetMapMode(win32con.MM_TEXT)

print('Printer using: {2}\nNumber of Lines: {0}\nPrint Content: {1}'.format(
    str(len(text)),
    text,
    printer_name
    ))

p.StartDoc('test doc')
p.StartPage()
    
text = process_text(text, text_size)

for line in range(len(text)):
    p.SelectObject(generate_font(text_size, underline[line]))
    for i in range(len(text[line])):
        p.TextOut(0,i*int(LETTER_HEIGHT_RATIO*(text_size/100)),text[line][i])
    p.EndPage()
    
p.EndDoc()
