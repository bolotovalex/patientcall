from tkinter import *
import time
import pygame
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/patientcall/ff-bell.wav")
pygame.mixer.music.play()
play_state = True

def task():
    global play_state
    check_state(7,l1)
    win.after(100, task)

def check_state(pin, label):
    global play_state
    time.sleep(0.4)
    state = GPIO.input(pin)
    if state == 0:
        label.config(text='СВОБОДНО')
        if play_state == True:
            pygame.mixer.music.play()
            play_state = False
    elif state == 1:
        label.config(text='ЗАНЯТО')
        play_state = True

win = Tk()
win.title("Терминал вызова")
win.geometry('1280x720')
win.configure(background='black')

l1 = Label(width=14, height=4, bg='red', text="СВОБОДНО", fg='white', font='Arial 140 bold')
l1.pack(side=TOP)


win.after(50, task)
win.mainloop()