#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter

class Application(Tkinter.Frame):
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.pack()
		#self.createWidgets()

if __name__ == '__main__':
	root = Tkinter.Tk()
	app = Application(master=root)
	app.mainloop()

