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
	root.geometry("+%d+%d" % (w/2 - 300, h/2 - 25))

root = Tk()
center(root)
root.title("Screen Brightness")
root.minsize(width=600, height=50)
scalevar = IntVar()
frame=Frame(root,width=600, height=50)
scale = Scale(frame, from_=0, to=100, variable=scalevar, orient="horizontal", command=get_scale_value)

root.update_idletasks()
scalevar.set(get_current_brightness(None)*100)

root.update()
scale.pack(side="top", fill="x", expand=True)

frame.pack(expand=True, fill='both')
frame.pack_propagate(0)

root.mainloop()

