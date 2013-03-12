from Tkinter import *

def callback():
	print 1

button = Button(None, text='button', command='callback')
button.pack()
mainloop()
