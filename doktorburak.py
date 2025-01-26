import tkinter as tk
from pygame import mixer
import time
import random
import webbrowser

main = tk.Tk()
main.title("Doktor Burak Harika")
main.geometry("500x400")

maindoktor = tk.PhotoImage(file="maindoktor.png")

maindre = tk.Label(main, image=maindoktor)
maindre.place(x=200, y=10, width=100, height=100)

maintext1 = tk.Label(main, text="dukdorburagın\nhaniggadunyası")
maintext1.place(x=50, y=10)

maintext2 = tk.Label(main, text="nicebombpilan\nmr.dukdorburag")
maintext2.place(x=350, y=10)

mixer.init()

def baslatgıral():
    mixer.music.load("efsanasarki.mp3")
    mixer.music.play()

def durdurgıral():
    mixer.music.stop()

oynatgıral = tk.Button(main, text="calgıralım", command=baslatgıral)
oynatgıral.place(x=200, y=200, width=100, height=50)

durlan = tk.Button(main, text="durdurlan\nsalak", command=durdurgıral)
durlan.place(x=200, y=250, width=100, height=50)

def sahtedukdor():
    webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxiQfimG5GN41DuBuBtve9gQIhknl66tBZBg&s")

sahtedukbudon = tk.Button(main, text="sahredukdor\ncukayıbbb", command=sahtedukdor)
sahtedukbudon.place(x=50, y=225)

def gercekdukdor():
    webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjdJngFwbBqDzcs__-8WEnkhJiUMsXogdmLQ&s")

gercekdukbudon = tk.Button(main, text="gercekdukdor\nhalalkeci", command=gercekdukdor)
gercekdukbudon.place(x=350, y=225)

main.mainloop()