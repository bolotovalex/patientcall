from tkinter import *
import time
import pygame
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pygame.mixer.init()
pygame.mixer.music.load("sound.wav")
pygame.mixer.music.play()



def task():
	check_state(7,l1)
	win.after(100, task)

def check_state(pin, label):
	state = GPIO.input(pin)
	if state == 0:
		label.config(text='ВХОДИТЕ', bg='green'); pygame.mixer.music.load("sound.wav"); pygame.mixer.music.play()
	elif state == 1:
		label.config(text='ОЖИДАЙТЕ', bg='#FF0000')
win = Tk()

win.title("Терминал вызова")
win.geometry('1280x720')
win.configure(background='black')

l1 = Label(width=15, height=2, bg='#3515B0', text="Проверка", fg='white', font='Arial 80 bold')
l1.pack(side=TOP)


win.after(50, task)
win.mainloop()