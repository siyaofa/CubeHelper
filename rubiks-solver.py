import numpy as np
import os
import cv2
from cv2 import *
import sys
import time
import json
import cubex
import getMap
from collections import Counter
from visual import *


def extractFaceFromCam(face):
	#color_ind=['black','white','red','orange','green','blue','yellow']
	#color_ind=['0','1','2','3','4','5','6','7']
	color_ind=['0','7','3','6','1','4','2','5']
	cam_num=0
	cam=cv2.VideoCapture(cam_num)
	while True:
			success,frame=cam.read()
			#frame=cv2.flip(frame,1)
			cut_frame=frame[:,:frame.shape[0],:]
			alpha=10
			small_frame = cv2.resize(cut_frame, (0,0), fx=1.0/alpha, fy=1.0/alpha)
##			small_frame = cv2.resize(cut_frame, (4, 3))
			img_recognized,img_map=getMap.get_image_map(small_frame)
			#cv2.imshow('real '+face,cv2.flip(cut_frame,1))
			big_img_recognized = cv2.resize(img_recognized, (0,0), fx=alpha, fy=alpha)
			#cv2.imshow(face,big_img_recognized)
			if cam_num==1:
				vis = np.concatenate((cut_frame, big_img_recognized), axis=1)
			else:
				vis = np.concatenate((cv2.flip(cut_frame,1), cv2.flip(big_img_recognized,1)), axis=1)
			
			cv2.imshow(face,vis)
			if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			elif cv2.waitKey(1) & 0xFF == ord('r'):
					cv2.imwrite(face+'.jpg',frame)
					position = {}
					#color_ind=['else','black','white','red','orange','green','blue','yellow']
					
					rowPixls=img_map.shape[0]/3
					colPixls=img_map.shape[1]/3
			
					A1=img_map[0:rowPixls-1,0:rowPixls-1]
					[(most_ind,most_num)]=Counter(A1.flat).most_common(1)
					position[face+'1'] = color_ind[most_ind]

					A4=img_map[0:rowPixls-1,rowPixls:2*rowPixls-1]
					[(most_ind,most_num)]=Counter(A4.flat).most_common(1)
					position[face+'2'] = color_ind[most_ind]

					A7=img_map[0:rowPixls-1,2*rowPixls:img_map.shape[1]]
					[(most_ind,most_num)]=Counter(A7.flat).most_common(1)
					position[face+'3'] = color_ind[most_ind]

					A2=img_map[rowPixls:2*rowPixls-1,0:rowPixls-1]
					[(most_ind,most_num)]=Counter(A2.flat).most_common(1)
					position[face+'4'] = color_ind[most_ind]

					A5=img_map[rowPixls:2*rowPixls-1,rowPixls:2*rowPixls-1]
					[(most_ind,most_num)]=Counter(A5.flat).most_common(1)
					position[face+'5'] = color_ind[most_ind]

					A8=img_map[rowPixls:2*rowPixls-1,2*rowPixls:img_map.shape[1]]
					[(most_ind,most_num)]=Counter(A8.flat).most_common(1)
					position[face+'6'] = color_ind[most_ind]

					A3=img_map[2*rowPixls:img_map.shape[0],0:rowPixls-1]
					[(most_ind,most_num)]=Counter(A3.flat).most_common(1)
					position[face+'7'] = color_ind[most_ind]

					A6=img_map[2*rowPixls:img_map.shape[0],rowPixls:2*rowPixls-1]
					[(most_ind,most_num)]=Counter(A6.flat).most_common(1)
					position[face+'8'] = color_ind[most_ind]

					A9=img_map[2*rowPixls:img_map.shape[0],2*rowPixls:img_map.shape[1]]
					[(most_ind,most_num)]=Counter(A9.flat).most_common(1)
					position[face+'9'] = color_ind[most_ind]	

					print position
					break
					

	cam.release()
	cv2.destroyAllWindows()
	#return front,right,back,left,top,bottom
	return position

	

front = extractFaceFromCam(face='f')
right = extractFaceFromCam(face='r')
back= extractFaceFromCam(face='b')
left= extractFaceFromCam(face='l')
top= extractFaceFromCam(face='t')
bottom= extractFaceFromCam(face='bo')


front_str=front.get('f1')+front.get('f2')+front.get('f3')+front.get('f4')+front.get('f5')+front.get('f6')+front.get('f7')+front.get('f8')+front.get('f9')
right_str=right.get('r1')+right.get('r2')+right.get('r3')+right.get('r4')+right.get('r5')+right.get('r6')+right.get('r7')+right.get('r8')+right.get('r9')
back_str=back.get('b1')+back.get('b2')+back.get('b3')+back.get('b4')+back.get('b5')+back.get('b6')+back.get('b7')+back.get('b8')+back.get('b9')
left_str=left.get('l1')+left.get('l2')+left.get('l3')+left.get('l4')+left.get('l5')+left.get('l6')+left.get('l7')+left.get('l8')+left.get('l9')
bottom_str=bottom.get('bo1')+bottom.get('bo2')+bottom.get('bo3')+bottom.get('bo4')+bottom.get('bo5')+bottom.get('bo6')+bottom.get('bo7')+bottom.get('bo8')+bottom.get('bo9')
top_str=top.get('t1')+top.get('t2')+top.get('t3')+top.get('t4')+top.get('t5')+top.get('t6')+top.get('t7')+top.get('t8')+top.get('t9')
#[ULFRBD]
#cube_str=top_str+front_str+left_str+back_str+right_str+bottom_str
cube_str=top_str+left_str+front_str+right_str+back_str+bottom_str
print(cube_str)
solution_str=cubex.slove(cube_str)
print(solution_str)


solution_str.strip().strip(',')
# print(solution_str)
solution=[]
for i in range(0,len(solution_str)/4):
	solution.append(solution_str[4*i:4*i+2])


color_ind={'0':color.black,'1':color.orange,'2':color.blue,'3':color.white,'4':color.green,'5':color.yellow,'6':color.red}
pyr_color=[]
for num_str in cube_str:
	pyramid_color=color_ind.get(num_str)
	pyr_color.append(pyramid_color)



cubelet_size=0.9
pyr_size=(cubelet_size*0.5,cubelet_size*1,cubelet_size*1)
cube=[]
#dimention of cube
N=3

#initial the cube with colors
for i in range(-1,N-1):
	for j in range(-1,N-1):
		for k in range(-1,N-1):
			cubelet=frame()
			#bottom
			if j==-1:
				pyramid(frame=cubelet,pos=(0,-0.5*cubelet_size,0),size=pyr_size,axis=(0,1,0),color=pyr_color[45+(-k+1)*3+i+1])
				
			else:
				pyramid(frame=cubelet,pos=(0,-0.5*cubelet_size,0),size=pyr_size,axis=(0,1,0),color=color.black)
				
			#top
			if j==1:
				pyramid(frame=cubelet,pos=(0,0.5*cubelet_size,0),size=pyr_size,axis=(0,-1,0),color=pyr_color[(k+1)*3+i+1])
				
			else:
				pyramid(frame=cubelet,pos=(0,0.5*cubelet_size,0),size=pyr_size,axis=(0,-1,0),color=color.black)
				
			#left
			if i==-1:
				pyramid(frame=cubelet,pos=(-0.5*cubelet_size,0,0),size=pyr_size,axis=(1,0,0),color=pyr_color[9+(-j+1)*3+k+1])
			else:
				pyramid(frame=cubelet,pos=(-0.5*cubelet_size,0,0),size=pyr_size,axis=(1,0,0),color=color.black)	
				
			#right
			if i==1:
				pyramid(frame=cubelet,pos=(0.5*cubelet_size,0,0),size=pyr_size,axis=(-1,0,0),color=pyr_color[27+(-k+1)+(-j+1)*3])
				
			else:
				pyramid(frame=cubelet,pos=(0.5*cubelet_size,0,0),size=pyr_size,axis=(-1,0,0),color=color.black)

				
			#front
			if k==1:
				pyramid(frame=cubelet,pos=(0,0,0.5*cubelet_size),size=pyr_size,axis=(0,0,-1),color=pyr_color[18+(i+1)+3*(1-j)])
				
			else:
				pyramid(frame=cubelet,pos=(0,0,0.5*cubelet_size),size=pyr_size,axis=(0,0,-1),color=color.black)
				
			#back
			if k==-1:
				pyramid(frame=cubelet,pos=(0,0,-0.5*cubelet_size),size=pyr_size,axis=(0,0,1),color=pyr_color[36+(1-i)+3*(1-j)])
				
			else:
				pyramid(frame=cubelet,pos=(0,0,-0.5*cubelet_size),size=pyr_size,axis=(0,0,1),color=color.black)
				
			cubelet.pos=(i,j,k)
			cubelet.material=materials.plastic
			cube.append(cubelet)
			




#rotate_face is the face which will turn late, direct=1 is underclockwise
def face_rotate(rotate_face,direct):
	deltat=0.05
	theta=0
	rotating_face=frame()
	while theta<pi/2:
		sleep(deltat)
		for cubelet in cube:			
			if rotate_face=='R':
				rotating_axis=(-direct,0,0)
				if cubelet.x==1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			elif rotate_face=='L':
				rotating_axis=(direct,0,0)
				if cubelet.x==-1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			elif rotate_face=='U':
				rotating_axis=(0,-direct,0)
				if cubelet.y==1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			elif rotate_face=='D':
				rotating_axis=(0,direct,0)
				if cubelet.y==-1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			elif rotate_face=='F':
				rotating_axis=(0,0,-direct)
				if cubelet.z==1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			elif rotate_face=='B':
				rotating_axis=(0,0,direct)
				if cubelet.z==-1:
					cubelet.rotate(angle=pi/2*deltat,axis=rotating_axis,origin=(0,0,0))
			
		theta+=pi/2*deltat
	#it would lost precise after rotate
	for cubelet in cube:
		cubelet.x=round(cubelet.x,1)
		cubelet.y=round(cubelet.y,1)
		cubelet.z=round(cubelet.z,1)


sleep(10)
		
print(len(solution))
for move in solution:
	if move=='LD':
		face_rotate('L',1)
	elif move=='LU':
		face_rotate('L',-1)
	elif move=='RD':
		face_rotate('R',-1)
	elif move=='RU':
		face_rotate('R',1)
	elif move=='UL':
		face_rotate('U',1)
	elif move=='UR':
		face_rotate('U',-1)
	elif move=='DL':
		face_rotate('D',-1)
	elif move=='DR':
		face_rotate('D',1)
	elif move=='FA':
		face_rotate('F',-1)
	elif move=='FC':
		face_rotate('F',1)
	elif move=='BA':
		face_rotate('B',1)
	elif move=='BC':
		face_rotate('B',-1)
	else:
		print('done!')
		



