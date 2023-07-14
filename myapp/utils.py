import cv2 as cv
import numpy as np
def util(image_path):
    image = cv.imread(image_path)
    edge_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge_image = cv.dilate(edge_image,cv.getStructuringElement(cv.MORPH_RECT, (5, 5)),iterations=2)
    edge_image = cv.erode(edge_image,cv.getStructuringElement(cv.MORPH_RECT, (5, 5)),iterations=2)
    _,edge_image=cv.threshold(edge_image,100,255,cv.THRESH_BINARY)
    edge_image = cv.dilate(edge_image,cv.getStructuringElement(cv.MORPH_RECT, (5, 5)),iterations=1)
    edge_image=cv.Laplacian(edge_image,cv.CV_8UC1,ksize=1)
    lines=cv.HoughLinesP(edge_image,1,np.pi/180,100,minLineLength=1,maxLineGap=1)
    wallCoordinates=[]
    for line in lines:
        x1,y1,x2,y2=line[0]
        wallCoordinates.append({"x1":str(x1),"y1":str(y1),"x2":str(x2),"y2":str(y2)})
    data={"wallCoordinates":wallCoordinates,"dimensions":{"width":str(image.shape[1]),"height":str(image.shape[0])}}
    return data