#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import turtle

class Application(Tkinter.Frame):
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.pack()

		width = self.winfo_screenwidth()
		height = self.winfo_screenheight()

		self.cav = Tkinter.Canvas(self, bg = 'white', width = width/3*2, height = height)
		self.cav.pack(side = "left")
		self.tus = turtle.TurtleScreen(self.cav)
		self.tur = turtle.RawTurtle(self.tus)

		self.text = Tkinter.Text(self, width = width/3, height = height)
		self.text.config(state = Tkinter.DISABLED)
		self.text.pack(side = "right")
		# self.code = Tkinter.StringVar()
		# self.text["textvariable"] = self.code
		self.text.insert(Tkinter.END, "Just a text Widget\nin two lines\n")
		self.text.delete("2.0", Tkinter.END)

		self.bind_all("<KeyPress-Up>", self.get_key)
		self.bind_all("<KeyPress-Down>", self.get_key)
		self.bind_all("<KeyPress-Left>", self.get_key)
		self.bind_all("<KeyPress-Right>", self.get_key)

	def get_key(self, event):
		if event.keysym == "Up":
			self.tur.forward(5)
		elif event.keysym == "Down":
			self.tur.backward(5)
		elif event.keysym == "Left":
			self.tur.left(5)
		elif event.keysym == "Right":
			self.tur.right(5)

if __name__ == '__main__':
	root = Tkinter.Tk()
	root.wm_state('zoomed')
	root.resizable(0,0)
	app = Application(master=root)
	app.mainloop()
