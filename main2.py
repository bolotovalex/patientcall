from tkinter import *
import time
#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def task():
	check_state(7,l3)
	check_state(11,l4)
	check_state(13,l7)
	check_state(15,l8)
	win.after(100, task)

def check_state(pin, label):
	state = 0
	#state = GPIO.input(pin)
	if state == 0:
		label.config(text='ВХОДИТЕ', bg='green')
	elif state == 1:
		label.config(text='ОЖИДАЙТЕ', bg='#FF0000')
win = Tk()

win.title("Терминал вызова")
win.geometry('1280x720')
win.configure(background='black')
frame1=Frame(win, bg='black')
frame2=Frame(win, bg='black')
frame3=Frame(win, bg='black')
frame4=Frame(win, bg='black')
frame5=Frame(win, bg='black')


l1 = Label(frame1, width=20, height=1, bg='#1240AB', text="ВХОДИТЕ", fg='#00CC00', font='Arial 90 bold')
l2 = Label(frame1, width=20, height=1, bg='#269926', text="ЗАНЯТО", fg='#FF0000', font='Arial 90 bold')
l3 = Label(frame2, width=20, height=1, bg='#FFCD00', text="ВХОДИТЕ", fg='#00CC00', font='Arial 90 bold', )
l4 = Label(frame2, width=20, height=1, bg='red', text="ВХОДИТЕ", fg='#00CC00', font='Arial 90 bold')
l5 = Label(frame3, width=20, height=1, bg='#CD0074', text="ЗАНЯТО", fg='#FF0000', font='Arial 90 bold')


frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()

l1.pack(side=TOP)
l2.pack(side=TOP)
l3.pack(side=TOP)
l4.pack(side=TOP)
l5.pack(side=TOP)

#win.after(50, task)
win.mainloop()

