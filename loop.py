import numpy as np
import cv2, time
for x in range(3):
	for y in range(2):
		video=cv2.VideoCapture(1)

 	#i <= 5


		check,frame = video.read()
		print(check)
		print(frame)
		cv2.imshow("capturing",frame)
		cv2.imwrite("image.jpg",frame) 



		cv2.waitKey(0)
		video.release()
	#i += i + 1
	
cv2.destroyAllWindows()

