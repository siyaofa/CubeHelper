from svm import *
from svmutil import *
import numpy as np
import cv2

##y,x=[1,-1],[{1:1,2:-1},{1:1,2:-1}]
y,x=svm_read_problem('color_set_bgr.txt')
prob=svm_problem(y,x)
param=svm_parameter('-t 0 -c 4 -b 1')
model=svm_train(prob,param)
##yt=[1]
##xt=[{1:0,2:0,3:1}]
##p_label,p_acc,p_val=svm_predict(y,x,model)

def get_image_map(img):
    #img=cv2.GaussianBlur(img,(5,5),0)
    img_map=np.zeros((img.shape[0],img.shape[1]),img.dtype)
    img_recognised=img
    row=range(0,img.shape[0])
    col=range(0,img.shape[1])
    yt=[]
    xt=[]
    for i in row:
        for j in col:
            yt.append(2)
            xt.append({1:img[i,j,0],2:img[i,j,1],3:img[i,j,2]})
    ##cv2.imshow("1",img)        
    p_label,p_acc,p_val=svm_predict(yt,xt,model)
    ##map[i,j]=p_label[0]
    ##cv2.imshow("2",img)

    n=0
    for i in row:
        for j in col:
            value= p_label[n]
            n=n+1
            if value ==1:
              img_recognised[i,j,:]=[0,0,0]
            elif value==2:
                img_recognised[i,j,:]=[255,255,255]
            elif value==3:
                img_recognised[i,j,:]=[0,0,255]
            elif value==4:
                img_recognised[i,j,:]=[0,128,255]
            elif value==5:
                img_recognised[i,j,:]=[0,255,0]
            elif value==6:
                img_recognised[i,j,:]=[255,0,0]
            else:
                img_recognised[i,j,:]=[0,255,255]
	    img_map[i,j]=value
	
    return img_recognised,img_map




