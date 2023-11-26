import os, sys
import win32gui, win32print, win32ui, win32con


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

printer_name = win32print.GetDefaultPrinter()
hprinter = win32print.OpenPrinter(printer_name)
devmode = win32print.GetPrinter(hprinter, 8)["pDevMode"]

hdc = win32gui.CreateDC("WINSPOOL", printer_name, devmode)
dc = win32ui.CreateDCFromHandle(hdc)

dc.SetMapMode(win32con.MM_TEXT)

print('Printer using: {2}\nNumber of Lines: {0}\nPrint Content: {1}'.format(
    str(len(text)),
    text,
    printer_name
    ))

dc.StartDoc('test doc')
dc.StartPage()
    
text = process_text(text, text_size)

for line in range(len(text)):
    dc.SelectObject(generate_font (text_size, underline[line]))
    for i in range(len(text[line])):
        dc.TextOut(0,i*int(LETTER_HEIGHT_RATIO*(text_size/100)),text[line][i])
    dc.EndPage()
    
dc.EndDoc()
