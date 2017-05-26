#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import turtle

class Application(Tkinter.Frame):
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.pack()
		self.cav = Tkinter.Canvas(self)
		self.cav.pack({"side": "left"})
		self.cav.pack(expand = 1)
		self.tus = turtle.TurtleScreen(self.cav)
		tur = turtle.RawTurtle(self.tus)
		tur.forward(150)

if __name__ == '__main__':
	root = Tkinter.Tk()
	app = Application(master=root)
	app.mainloop()

