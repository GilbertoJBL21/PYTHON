import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import cam
import os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import threading as tr

name = "Charlot"
listerner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

main_window= Tk()
main_window.title("Charlot IA")
main_window.geometry("900x500")
main_window.resizable(0,0)
main_window.configure(bg='#283048')

comandos= """ 
                Comandos que puedes usar:
                - Reproduce..(canción)
                - Busca...(algo)
                - Abre...(página web o app)
                - Alarma..(hora en 24H)
                - Escribe
                - Termina
"""


label_title= Label(main_window, text="Charlot IA",bg="#283048",fg="#EAEAEA",font=("Arial", 30, "bold"))
label_title.pack(pady=10)

canvas_comandos=Canvas(bg="#283048",height=140,width=200)
canvas_comandos.place(x=0,y=0)
canvas_comandos.create_text(70,65,text=comandos,fill="#EAEAEA",font='Arial 11')

text_info=Text(main_window, bg="#283048",fg="#EAEAEA")
text_info.place(x=0,y=169,height=310,width=205)


charlot_foto= ImageTk.PhotoImage(Image.open("PORTADA.jpg"))
windows_foto= Label(main_window, image=charlot_foto)
windows_foto.pack(pady=5)

def mexican_voice():
    change_voice(0)
def spanish_voice():
    change_voice(2)
def english_voice():
    change_voice(1)    
def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("hola soy charlot")



sites = dict()

programs = dict()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()

def read_and_talk():
    text=text_info.get("1.0","end")
    talk(text)

def write_text(text_wiki):
    text_info.insert(INSERT,text_wiki)

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def clock(rec):
    num  = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activada a las  "+ num +"horas")
    if num [0] =='0'and len (num) < 5:
        num = '0' + num
    print(num)
    while True:
        if datetime.datetime.now().strftime("%H:%M") == num:
            print("DESPIERTA!!!!")
            mixer.init()
            mixer.music.load("auronplay_alarma.mp3")
            mixer.music.play()
        else:
            continue
        if keyboard.read_key() == "s":
            mixer.music.stop()
            break

def iniciar_charlot():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            talk("No te entendi")
            continue
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            talk(wiki)
            write_text(search + ":" + wiki)
            break
        elif 'alarm' in rec:
            t = tr.Thread(target=clock, args=(rec,))
            t.start()
        elif 'colores'in rec:
            talk("Enseguida")
            cam.capture()
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f'Abriendo{app}')
                    os.startfile(programs[app])
        elif 'escribe' in rec:
            try:
                with open('nota.txt', 'a')as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'w')
                write(file)
        elif 'termina' in rec:
            talk("Adiós!")
            break


def write(f):
    talk("Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("Nota.txt", shell=True)

def open_sites():
    pass
def open_programs():
    pass

Button_voice_mx= Button(main_window,text="Voz Mexico",fg="white",bg="green yellow",font=("Arial",18,"bold"),command=mexican_voice)
Button_voice_mx.place(x=720,y=80,width=150,height=45)

Button_voice_es= Button(main_window,text="Voz España",fg="white",bg="gold",font=("Arial",18,"bold"),command=spanish_voice)
Button_voice_es.place(x=720,y=140,width=150,height=45)

Button_voice_us= Button(main_window,text="Voz EEUU",fg="white",bg="red",font=("Arial",18,"bold"),command=english_voice)
Button_voice_us.place(x=720,y=200,width=150,height=45)

Button_lisen= Button(main_window,text="Escuchar",fg="white",bg="DodgerBlue2",font=("Arial",34,"roman"),command=iniciar_charlot)
Button_lisen.pack(pady=18)

Button_speak= Button(main_window,text="hablar",fg="white",bg="gray",font=("Arial",18,"bold"),command=read_and_talk)
Button_speak.place(x=720,y=260,width=150,height=45)

Button_add_sites= Button(main_window,text="Agregar archivos",fg="white",bg="royal blue",font=("Arial",18,"bold"),command=open_sites)
Button_add_sites.place(x=720,y=320,width=150,height=45)

Button_add_programs= Button(main_window,text="Agregar apps",fg="white",bg="royal blue",font=("Arial",18,"bold"),command=open_programs)
Button_add_programs.place(x=720,y=380,width=150,height=45)



main_window.mainloop()