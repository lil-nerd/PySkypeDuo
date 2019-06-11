import cv2 as cv

'''
VALUES:
	-camera --- device to get video from
	-window ---


'''

class MyVideoCapture:

	def __init__(self, window, video_source):
		self.camera = cv.VideoCapture(video_source)
		self.window = window

		if not self.camera.isOpened():
			print("Unable to connect to camera ", video_source)

		self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
		self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)


	def get_frame(self):
		if self.camera.isOpened():
			ret, frame = self.camera.read()
			if ret:
				return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (False, None)


	def __del__(self):
		if self.camera.isOpened():
			self.camera.release()
		self.window.mainloop()
