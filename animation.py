from visual import *

test_input="442416133132335415514222445623354662663546311612265551"
solution_str='DL, DL, BA, BA, FA, RU, LU, DL, FA, DR, LU, DR, LD, DL, FC, DL, FA, DR, RD, DR, RU, BA, DL, BC, DL, LU, DR, LD, BC, DR, BA, DR, RU, DL, RD, DL, DL, RD, DR, RU, DR, FC, DL, FA, FA, DL, RD, DR, RU, FC, LU, DL, DL, LD, DR, LU, DR, LD, FA, DL, DL, FC, DR, FA, DR, FC, DR, LU, DR, RU, DL, LD, DR, RD, DL, FA, DR, BA, DL, FC, DR, BC, DL, BC, DL, DL, BA, DR, BC, DR, BA, FC, DR, DR, FA, DL, FC, DL, FA,'
solution_str.strip().strip(',')
solution=[]
for i in range(0,len(solution_str)/4):
	solution.append(solution_str[4*i:4*i+2])




color_ind={'0':color.black,'1':color.orange,'2':color.blue,'3':color.white,'4':color.green,'5':color.yellow,'6':color.red}
pyr_color=[]
for num_str in test_input:
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
			


sleep(5)

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
		


