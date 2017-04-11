import cv2
import os
import os.path


# eye_haar = cv2.CascadeClassifier("haarcascade_eye.xml")
cube=cv2.CascadeClassifier("cube_cascade_2.xml")

n=0
if n==0:
	cam = cv2.VideoCapture(0)
	while True:
		_, img = cam.read()
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cubes = cube.detectMultiScale(gray_img, 1.3, 5)
		for cube_x,cube_y,cube_w,cube_h in cubes:
			cv2.rectangle(img, (cube_x, cube_y), (cube_x+cube_w, cube_y+cube_h), (0,255,0), 2)
			# roi_gray_img = gray_img[cube_y:cube_y+cube_h, cube_x:cube_x+cube_w]
			roi_img = img[cube_y:cube_y+cube_h, cube_x:cube_x+cube_w]
			cv2.imshow('roi',cv2.flip(roi_img,1))
			# eyes = eye_haar.detectMultiScale(roi_gray_img, 1.3, 5)
			# for eye_x,eye_y,eye_w,eye_h in eyes:
				# cv2.rectangle(roi_img, (eye_x,eye_y), (eye_x+eye_w, eye_y+eye_h), (255,0,0), 2)

		cv2.imshow('img', cv2.flip(img,1))			
		key = cv2.waitKey(30) & 0xff
		if key == 27:
			break

	cam.release()
	cv2.destroyAllWindows()
else:
	imgDir='test_img'
	alpha=10
	for parent,dirname,filenames in os.walk(imgDir):
		for filename in filenames:
			print(imgDir+'/'+filename)
			img=cv2.imread(imgDir+'/'+filename)
			res = cv2.resize(img, (0,0), fx=1.0/alpha, fy=1.0/alpha)
			gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cubes = cube_haar.detectMultiScale(gray_img, 1.3, 5)
			for cube_x,cube_y,cube_w,cube_h in cubes:
				cv2.rectangle(img, (cube_x, cube_y), (cube_x+cube_w, cube_y+cube_h), (0,255,0), 2)
				# roi_gray_img = gray_img[cube_y:cube_y+cube_h, cube_x:cube_x+cube_w]
				# roi_img = img[cube_y:cube_y+cube_h, cube_x:cube_x+cube_w]
			cv2.imshow(filename,res)
	while True:
		key = cv2.waitKey(30) & 0xff
		if key == 27:
			cv2.destroyAllWindows()
			break	
	