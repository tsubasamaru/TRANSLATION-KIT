import tkinter
from typing import Text
import gtts
import googletrans
import speech_recognition
import playsound



translator = googletrans.Translator()
input_lang = 'ja-JP'
output_lang = 'en'
def click_btn():
    text = entry_A.get()
    translated = translator.translate(text, dest = output_lang)
    entry_B.delete(0, tkinter.END)
    entry_B.insert(tkinter.END, translated.text)
    converted_audio = gtts.gTTS(translated.text, lang = output_lang)
    converted_audio.save('romantic.mp3')
    playsound.playsound('romantic.mp3')



root = tkinter.Tk()
root.title('TRANSLATION KIT')
root.geometry('500x500')
entry_A = tkinter.Entry(width = 32)
entry_A.place(x = 150, y = 150)
entry_B = tkinter.Entry(width = 32)
entry_B.place(x = 150, y = 380)
btn = tkinter.Button(text = 'TRANSLATION', font = ('Times New Roman', 20), bg = 'lightblue', command = click_btn)
btn.place(x = 150, y = 250)



root.mainloop()


