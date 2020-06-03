print('''

    +++++++++++++++++++++
    |                   |
    |    PDF            |
    |       To          |
    |         MP3       |
    |     Converter     |
    |                   |
    +++++++++++++++++++++


''')

from tkinter import *
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS


Tk().withdraw()
filelocation = askopenfilename()


with open(filelocation, "rb") as red:
    pdf = pdftotext.PDF(red)

string_of_text=""
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='en')

uname_file = input("\n\nPlease ! Enter the File Name: ")
final_file.save(uname_file)
 Print("Thank You" + uname_file + "has been converted!!")
