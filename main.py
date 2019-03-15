from tkinter import *
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def task():
	check_state(7,l3)
	check_state(11,l4)
	check_state(13,l7)
	check_state(15,l8)
	win.after(100, task)

def check_state(pin, label):
	state = GPIO.input(pin)
	if state == 0:
		label.config(text='ВХОДИТЕ', bg='green')
	elif state == 1:
		label.config(text='ОЖИДАЙТЕ', bg='#FF0000')
win = Tk()

win.title("Терминал вызова")
win.geometry('1280x720')
win.configure(background='black')
frame1=Frame(win, bg='white')
frame2=Frame(win)
frame3=Frame(win)
frame4=Frame(win)

l1 = Label(frame1, width=15, height=2, bg='#3515B0', text="ОКНО - 1", fg='white', font='Arial 56 bold')
l2 = Label(frame1, width=16, height=2, bg='#3515B0', text="ОКНО - 2", fg='white', font='Arial 56 bold')
l3 = Label(frame2, width=15, height=2, bg='black', text="ОЖИДАНИЕ", fg='yellow', font='Arial 56 bold', )
l4 = Label(frame2, width=16, height=2, bg='black', text="ОЖИДАНИЕ", fg='yellow', font='Arial 56 bold')
l5 = Label(frame3, width=15, height=2, bg='#3515B0', text="ОКНО - 3", fg='white', font='Arial 56 bold')
l6 = Label(frame3, width=16, height=2, bg='#3515B0', text="ОКНО - 4", fg='white', font='Arial 56 bold')
l7 = Label(frame4, width=15, height=2, bg='black', text="ОЖИДАНИЕ", fg='yellow', font='Arial 56 bold')
l8 = Label(frame4, width=16, height=2, bg='black', text="ОЖИДАНИЕ", fg='yellow', font='Arial 56 bold')
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
l1.pack(side=LEFT)
l2.pack(side=RIGHT)
l3.pack(side=LEFT)
l4.pack(side=RIGHT)
l5.pack(side=LEFT)
l6.pack(side=RIGHT)
l7.pack(side=LEFT)
l8.pack(side=RIGHT)

win.after(50, task)
win.mainloop()

