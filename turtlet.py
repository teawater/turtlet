#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import tkFileDialog
import turtle

step = 5
tail = "\nturtle.Screen().exitonclick()\n"

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

		self.code_count = 0
		self.prev_line_num = 0
		self.prev_keysym = None
		self.step_count = 0

		self.handle_tail = False
		self.first_code = False
		self.text = Tkinter.Text(self, width = width/3, height = height)
		self.text.pack(side = "right")
		self.text.config(state = Tkinter.DISABLED)
		self.text_insert("#!/usr/bin/python\n")
		self.text_insert("# -*- coding: UTF-8 -*-\n\n", line_num = 2)
		self.text_insert("import turtle\n", line_num = 1)
		self.text_insert(tail, 2)
		self.handle_tail = True
		self.first_code = True

		self.bind_all("<KeyPress-Up>", self.get_key)
		self.bind_all("<KeyPress-Down>", self.get_key)
		self.bind_all("<KeyPress-Left>", self.get_key)
		self.bind_all("<KeyPress-Right>", self.get_key)

	def text_insert(self, s, line_num = 1, overwrite_prev = False):
		self.text.config(state = Tkinter.NORMAL)
		real_count = self.code_count
		if overwrite_prev:
			real_count = self.code_count - self.prev_line_num
			self.text.delete(str(real_count + 1) + ".0", Tkinter.END)
		elif self.handle_tail:
			self.text.delete(str(self.code_count) + ".0", Tkinter.END)
			self.code_count -= 2
			real_count -= 2

		if self.first_code:
			self.text.insert(Tkinter.END, "\n")
			self.code_count += 1
			self.first_code = False

		if real_count != 0 and overwrite_prev:
			s = "\n" + s

		self.text.insert(Tkinter.END, s)
		if self.handle_tail:
			self.text.insert(Tkinter.END, tail)
			line_num += 2
		if not overwrite_prev:
			self.code_count += line_num
		self.prev_line_num = line_num
		self.text.config(state = Tkinter.DISABLED)

	def get_key(self, event):
		if event.keysym == self.prev_keysym:
			self.step_count += step
			overwrite = True
		else:
			self.step_count = step
			overwrite = False

		if event.keysym == "Up":
			self.tur.forward(step)
			self.text_insert("turtle.forward(" + str(self.step_count) + ")\n", overwrite_prev = overwrite)
		elif event.keysym == "Down":
			self.tur.backward(step)
			self.text_insert("turtle.backward(" + str(self.step_count) + ")\n", overwrite_prev = overwrite)
		elif event.keysym == "Left":
			self.tur.left(step)
			self.text_insert("turtle.left(" + str(self.step_count) + ")\n", overwrite_prev = overwrite)
		elif event.keysym == "Right":
			self.tur.right(step)
			self.text_insert("turtle.right(" + str(self.step_count) + ")\n", overwrite_prev = overwrite)

		self.prev_keysym = event.keysym

def save():
	options = {}
	options['initialfile'] = '1.py'
	options['filetypes'] = [('python files', '.py')]
	name = tkFileDialog.asksaveasfilename(**options)
	if name.rfind(".py") + 3 != len(name):
		name += ".py"
	open(name, "w").write(app.text.get("0.0", Tkinter.END))

if __name__ == '__main__':
	root = Tkinter.Tk()
	root.wm_state('zoomed')
	root.resizable(0,0)

	app = Application(master=root)

	menubar = Tkinter.Menu(root)
	menubar.add_command(label="保存", command=save)
	root.config(menu=menubar)

	app.mainloop()
