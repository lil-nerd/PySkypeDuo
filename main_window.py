import tkinter as tk
from PIL import Image
from PIL import ImageTk

from video import MyVideoCapture
from save_png import *
from draw import *
#help_functions

def mouse_left_click(event):
	left_click_x, left_click_y  = event.x, event.y
	return left_click_x, left_click_y


class MainWindow:


	def __init__(self, window, window_title):
		#var for Photo
		self.snapshot = False
		#var for pause
		self.video_on_pause = False
		#vars for left clicks
		self.left_click_x, self.left_click_y = 0, 0
		#window geometry and init
		self.window = window
		self.window_title = window_title
		self.video = MyVideoCapture(window, 0)
		self.canvas = tk.Canvas(window, width  = self.video.width,
										height = self.video.height + 100)
		#pause button
		self.canvas.create_rectangle(20, self.video.height + 20,
									 100, self.video.height + 50,
									 fill = "white")
		self.canvas.create_text(60, self.video.height + 35, text = "pause")
		#pause button
		self.canvas.create_rectangle(200, self.video.height + 20,
									 280, self.video.height + 50,
									 fill = "white")
		self.canvas.create_text(240, self.video.height + 35, text = "take photo")

		self.canvas.pack()
		#help functions
		def mouse_left_click(event):
			self.left_click_x, self.left_click_y  = event.x, event.y
			self.on_pause()
			self.take_photo()

		#binds
		self.canvas.bind("<Button 1>", mouse_left_click)

		self.on_air()

	def take_photo(self):
		if (self.left_click_y < self.video.height + 50 and self.left_click_y > self.video.height + 20):
			if (self.left_click_x < 280 and self.left_click_x > 200):
				print("snap!")
				self.snapshot = not self.snapshot






	def on_pause(self):
		pause_btn_color = ["white", "green"]
		if (self.left_click_y < self.video.height + 50 and self.left_click_y > self.video.height + 20):
			if (self.left_click_x < 100 and self.left_click_x > 20):
				if(self.video_on_pause):
					print("ON AIR!")
				else:
					print("PAUSED!")
				self.video_on_pause = not self.video_on_pause
				self.canvas.create_rectangle(20, self.video.height + 20,
											 100, self.video.height + 50,
											 fill = pause_btn_color[int(self.video_on_pause)])
				self.canvas.create_text(60, self.video.height + 35, text = "pause")

	def on_air(self):

		self.delay = 15
		self.update()


		self.window.mainloop()


	def update(self):
		ret, frame = self.video.get_frame()
		image = Image.fromarray(frame)
		if ret and not self.video_on_pause:
			self.photo = ImageTk.PhotoImage(image  = image)
			self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
		if self.snapshot:
			save_png(self.window, image)
			self.snapshot = not self.snapshot


		self.window.after(self.delay, self.update)
