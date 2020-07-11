#! /usr/bin/python3

#Version 1
#https://github.com/momen84


import subprocess
from tkinter import *
	

def get_display_name():

	display=subprocess.check_output('xrandr | grep -w connected',stderr=subprocess.STDOUT,shell=True)

	return display.split()[0].decode('utf-8')

def apply(scale_value):

	subprocess.call(['xrandr' ,'--output' ,'{}'.format(get_display_name()), '--brightness', '{}'.format(scale_value)])


def get_scale_value(event):
	frame.focus_set()
	apply(scale.get()/100)

def get_current_brightness(event):

	current=subprocess.check_output('xrandr --verbose | grep -m  1  -i brightness',stderr=subprocess.STDOUT,shell=True)
	current=current.decode('utf-8').strip().split(':')[1].strip()
	return float(current)

def center(root):
	h=root.winfo_screenheight()
	w=root.winfo_screenwidth()
	root.geometry("+%d+%d" % (w/2, h/2))

root = Tk()
center(root)
root.title("Screen Brightness")
scalevar = IntVar()
frame=Frame(root,width=50, height=50)
scale = Scale(frame, from_=0, to=100, variable=scalevar, orient="horizontal")
button=Button(frame,text='Apply',width=50)

root.update_idletasks()
scalevar.set(get_current_brightness(None)*100)

root.update()
scale.pack(side="top", fill="x", expand=True)
button.pack(side="bottom", fill="x", expand=True)

button.bind("<Button-1>",get_scale_value)
frame.pack()

root.mainloop()