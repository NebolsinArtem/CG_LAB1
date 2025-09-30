import numpy as np
from PIL import Image
import math
def draw_line(img_mat, x0, y0, x1, y1, count, color):
    step = 1.0 / count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t)*x0 + t*x1)
        y = round((1.0 - t)*y0 + t*y1)
        img_mat[y, x] = color

def draw_line_fix1(img_mat, x0, y0, x1, y1, color):
    count = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    step = 1.0 / count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t)*x0 + t*x1)
        y = round((1.0 - t)*y0 + t*y1)
        img_mat[y, x] = color

def x_loop_line(img_mat, x0, y0, x1, y1, color):
    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round ((1.0 - t)*y0 + t*y1)
        img_mat[y, x] = color

def x_loop_line_fix1(img_mat, x0, y0, x1, y1, color):
    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round ((1.0 - t)*y0 + t*y1)
        img_mat[y, x] = color

def x_loop_line_fix2(img_mat, x0, y0, x1, y1, color):

    xchange = False
    if(abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True


    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round ((1.0 - t)*y0 + t*y1)
        if(xchange):
            img_mat[x, y] = color
        else:
            img_mat[y, x] = color



def x_loop_line_fixes(img_mat, x0, y0, x1, y1, color):

    xchange = False
    if(abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round ((1.0 - t)*y0 + t*y1)
        if(xchange):
            img_mat[x, y] = color
        else:
            img_mat[y, x] = color
def x_loop_line_no_y_calc(img_mat, x0, y0, x1, y1, color):

    xchange = False
    if(abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = abs(y1 - y0) / (x1 - x0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):
        
        derror += dy
        if(derror > 0.5):
            derror -= 1.0
            y += y_update
        
        if(xchange):
            img_mat[x, y] = color
        else:
            img_mat[y, x] = color





def x_loop_line_v2_no_y_calc(img_mat, x0, y0, x1, y1, color):

    xchange = False
    if(abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2.0*(x1 - x0)*abs(y1 - y0) /(x1 - x0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):
        
        derror += dy
        if(derror > 2.0*(x1 - x0)*0.5):
            derror -= 2.0*(x1 - x0)*1.0
            y += y_update
        
        if(xchange):
            img_mat[x, y] = color
        else:
            img_mat[y, x] = color


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
    derror = 0.0
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
        



img_mat = np.zeros((200, 200, 3), dtype = np.uint8)
for k in range(13):
    x0, y0 = 100, 100
    x1 = 100 + int(math.cos(2*math.pi*k/13) *95)
    y1 = 100 + int(math.sin(2*math.pi*k/13) *95)
    #draw_line(img_mat, x0, y0, x1, y1, 200, [128, 0, 128])
    #draw_line_fix1(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #x_loop_line(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #x_loop_line_fix1(img_mat, x0, y0, x1, y1, [128, 0, 128])
    x_loop_line_fix2(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #x_loop_line_fixes(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #x_loop_line_no_y_calc(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #x_loop_line_v2_no_y_calc(img_mat, x0, y0, x1, y1, [128, 0, 128])
    #bresenham_line(img_mat, x0, y0, x1, y1, [128, 0, 128])

    


















img = Image.fromarray(img_mat, mode = 'RGB')
img.show()
img.save('img.png')