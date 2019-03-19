import time
from tkinter import *
#import time
import mp3play

#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def task():
	check_state(7,l2)
	check_state(11,l4)
	check_state(13,l7)
	check_state(15,l8)
	check_state(15, l10)
	play
	win.after(100, task)

def check_state(pin, label):
	'''state = GPIO.input(pin)
	if state == 0:
		label.config(text='ВХОДИТЕ', bg='green')
	elif state == 1:
		label.config(text='ОЖИДАЙТЕ', bg='#FF0000')'''
win = Tk()
f=mp3play.load('sound.mp3'); play = lambda: f.play()

win.title("Терминал вызова")
win.geometry('1920x1080')
win.configure(background='black')
frame1=Frame(win, bg='white')
frame2=Frame(win)
frame3=Frame(win)
frame4=Frame(win)
frame5=Frame(win)


l1 = Label(frame1, width=9, height=1, bg='#1240AB', text="ОКНО-1 ◄", fg='white', font='Arial 82 bold')
l2 = Label(frame1, width=12, height=1, bg='#FF0000', text="ЗАНЯТО", fg='yellow', font='Arial 82 bold')
l3 = Label(frame2, width=9, height=1, bg='#269926', text="ОКНО-2 ▲", fg='white', font='Arial 82 bold', )
l4 = Label(frame2, width=12, height=1, bg='green', text="СВОБОДНО", fg='yellow', font='Arial 82 bold')
l5 = Label(frame3, width=9, height=1, bg='#FFCD00', text="ОКНО-3 ▲", fg='white', font='Arial 82 bold')
l6 = Label(frame3, width=12, height=1, bg='#FF0000', text="ЗАНЯТО", fg='yellow', font='Arial 82 bold')
l7 = Label(frame4, width=9, height=1, bg='red', text="ОКНО-4 ▲", fg='white', font='Arial 82 bold')
l8 = Label(frame4, width=12, height=1, bg='green', text="СВОБОДНО", fg='yellow', font='Arial 82 bold')
l9 = Label(frame5, width=9, height=1, bg='#CD0074', text="ОКНО-5 ►", fg='white', font='Arial 82 bold')
l10 = Label(frame5, width=12, height=1, bg='#FF0000', text="ЗАНЯТО", fg='yellow', font='Arial 82 bold')

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()

l1.pack(side=LEFT)
l2.pack(side=RIGHT)
l3.pack(side=LEFT)
l4.pack(side=RIGHT)
l5.pack(side=LEFT)
l6.pack(side=RIGHT)
l7.pack(side=LEFT)
l8.pack(side=RIGHT)
l9.pack(side=LEFT)
l10.pack(side=RIGHT)

win.after(50, task)
win.mainloop()

