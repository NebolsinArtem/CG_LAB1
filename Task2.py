import numpy as np
from PIL import Image
import math

def bresenham_line(img_mat, x0, y0, x1, y1, color):

    xchange = False
    if(abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2*abs(y1 - y0)
    derror = 0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):

        if(xchange):
            img_mat[x, y] = color
        else:
            img_mat[y, x] = color
        
        derror += dy
        if(derror > (x1 - x0)):
            derror -= 2*(x1 - x0)
            y += y_update

def parsedotsobj(file):
    arr = []
    for s in open(file):
        sp = s.split()
        if(sp[0] == 'v'):
          x = sp[1]
          y = sp[2]
          z = sp[3]
          arr.append([x, y, z])
    return arr

def parsepolysobj(file):
    arr = []
    for s in open(file):
        sp = s.split()
        if(sp[0] == 'f'):
            point1 = sp[1].split('/')[0]
            point2 = sp[2].split('/')[0]
            point3 = sp[3].split('/')[0]
            arr.append([point1, point2, point3])
          
    return arr

        
img_mat = np.zeros((2000,2000,3), dtype=np.uint8)


arrdots = parsedotsobj("C:\model_1.obj")
arrindexes = parsepolysobj("C:\model_1.obj")

for cords in arrdots:
    x = int(float(cords[0])*5000 + 1000)
    y = int(float(cords[1])*5000 + 1000)
    img_mat[y, x] = 255


for indexes in arrindexes:
    x0 = int(float(arrdots[int(indexes[0]) - 1][0]) * 5000 + 1000)
    y0 = int(float(arrdots[int(indexes[0]) - 1][1]) * 5000 + 1000)
    x1 = int(float(arrdots[int(indexes[1]) - 1][0]) * 5000 + 1000)
    y1 = int(float(arrdots[int(indexes[1]) - 1][1]) * 5000 + 1000)
    x2 = int(float(arrdots[int(indexes[2]) - 1][0]) * 5000 + 1000)
    y2 = int(float(arrdots[int(indexes[2]) - 1][1]) * 5000 + 1000)
    bresenham_line(img_mat, x0, y0, x1, y1, 255)
    bresenham_line(img_mat, x0, y0, x2, y2, 255)
    bresenham_line(img_mat, x2, y2, x1, y1, 255)

img = Image.fromarray(img_mat, mode = 'RGB')
img.show()

img.save('img.png')
