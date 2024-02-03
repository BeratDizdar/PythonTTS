from bs4 import BeautifulSoup
from tkinter.messagebox import * 
from tkinter import filedialog as fd
from tkinter import *
from gtts import gTTS
import requests
import os


class TTSApp:
    def __init__(self, window):
        self.window = window
        pgen = 500
        pyuk = 140
        ekrangen = window.winfo_screenwidth()
        ekranyuk = window.winfo_screenheight()
        x = (ekrangen-pgen)/2
        y = (ekranyuk-pyuk)/2
        self.window.geometry("%dx%d+%d+%d"%(pgen,pyuk,x,y))
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.tk_setPalette('#28B463')
        self.window.title("SpeechBot")

        self.langselect = Listbox(bg='#D5F5E3',fg='#000000')
        self.langselect.insert(1, "Türkçe")
        self.langselect.insert(2, "İngilizce")
        self.langselect.insert(3, "Japonca")
        self.langselect.pack(side=RIGHT, padx=8, pady=10)

        self.entry = Entry(width=140, bg='#D5F5E3',fg='#000000',font=("Courier New", 10, "bold"))
        self.entry.insert(1,"Buraya yazı veya link yazınız!")
        self.entry.pack(pady=12, padx=15)

        aframe = Frame()
        aframe.pack(pady=12)

        self.speak_button = Button(text="Seslendir", command=self.text_speech,bg='#229954',fg='#000000',font=("Courier New", 8, "bold"))
        self.speak_button.pack(padx=15, pady=5, side=LEFT) 

        self.link_speak_button = Button(text="Linkten Seslendir", command=self.link_speech,bg='#229954',fg='#000000',font=("Courier New", 8, "bold"))
        self.link_speak_button.pack(padx=15, pady=5, side=RIGHT)

        self.window.mainloop()

    def getLang(self):
        selected_lang = self.langselect.get(self.langselect.curselection())
        if selected_lang == "Türkçe":
            self.lang = 'tr'
        elif selected_lang == "İngilizce":
            self.lang = 'en'
        elif selected_lang == "Japonca":
            self.lang = 'ja'
        else:
            self.lang = 'tr' 

    def text_speech(self):

        self.getLang()
        self.text = self.entry.get()
        self.tts = gTTS(self.text, lang=self.lang)
        self.tts.save("audio.mp3")
        os.system("audio.mp3")
    
    def link_speech(self):
        

        self.getURL()
        self.getLang()
        self.tts = gTTS(self.text, lang=self.lang)
        self.tts.save("audio.mp3")
        os.system("audio.mp3")

    def getURL(self):
        self.url = self.entry.get()
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.page_content = self.response.text
            self.soup = BeautifulSoup(self.page_content, 'html.parser')
            self.all_paragraphs = self.soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            self.text = ''
            for tag in self.all_paragraphs:
                self.text += tag.get_text() + '\n'

def main():
    window = Tk()
    global myapp
    myapp = TTSApp(window)

if __name__ == "__main__":
    main()
