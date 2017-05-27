#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import turtle

class Application(Tkinter.Frame):
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.pack()

		self.cav = Tkinter.Canvas(self, bg = 'white', width = self.winfo_screenwidth()/2, height = self.winfo_screenheight()/2)
		self.cav.pack()
		#self.bind("<Enter>", self.left)
		self.cav.bind_all("<KeyPress-Left>", self.left)
		self.cav.bind_all("<KeyRelease-Left>", self.left_release)

		self.tus = turtle.TurtleScreen(self.cav)
		self.tur = turtle.RawTurtle(self.tus)
		self.tur.forward(10)

	def left(self, event):
		print 1
		#self.cav.config(width = self.winfo_screenwidth(), height = self.winfo_screenheight())
		#self.cav.config(width = 100)
		self.tur.forward(10)

	def left_release(self, event):
		print 2

if __name__ == '__main__':
	root = Tkinter.Tk()	
	app = Application(master=root)
	app.mainloop()
