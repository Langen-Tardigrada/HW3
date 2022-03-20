import math as m
import cmath
import numpy as np

def padding(img, width, height, size):
    # -------------------------------------------------------------------------------------------------
    # this function used for pad image to center 
    # with add row of above, row of bottom, column of right and column of left side.
    # then return with 2D list
    # -------------------------------------------------------------------------------------------------
    add_row = 0
    add_col = 0
    row = True
    while(add_row < size-width or add_col < size-height):
        if(row and add_row%2 == 0): # above
            elem = [[]]
            for j in range(len(img[0])):
                elem[0].append(img[0][j])
            img[0:0] = elem
            add_row+=1
            row = True
        elif(row and add_row%2 == 1): # bottom 
            elem = [[]]
            for j in range(len(img[0])):
                elem[0].append(img[len(img)-1][j])
            img.extend(elem)
            add_row+=1
            row = False
        elif((not row) and add_col%2 == 0 ):
            for i in range(len(img)): # right
                img[i].append(img[i][len(img[i])-1])
            add_col+=1
            row = False
        elif((not row) and add_col%2 == 1 ):
            for i in range(len(img)): # left
                img[i][0:0] = [img[i][0]]
            add_col+=1
            row = True

    return img

def amplitude(img, width, height):
    elem = []
    for i in range(height):
        l = []
        for j in range(width):
            l.append((abs(img[i][j])))
        elem.extend([l])
    return elem

def phase(img,width,height):
    elem = []
    try:
        for i in range(height):
            l = []
            for j in range(width):
                l.append(cmath.phase(img[i][j]))
            elem.extend([l])
    except Exception as e: 
        print(len(elem))
        raise e
    return elem

def find_max_min(color):
    max_value = color[0][0]
    min_value = color[0][0]
    try: 
        for i in range(len(color)):
            for j in range(len(color[0])):
                if color[i][j] > max_value:
                    max_value = color[i][j]
                if color[i][j] < min_value:
                    min_value = color[i][j]
    except Exception as e: raise e
    
    return max_value, min_value

def normalize_color(color):
    # normalize between 0 - 255
    list_color = []
    max_color, min_color = find_max_min(color)
    try:
        for i in range(len(color)):
            _list = []
            for j in range(len(color[0])):
                z = (color[i][j]-min_color)/(max_color-min_color) * 255
                _list.append(int(z))
            list_color.extend([_list])
            # print(list_color[i])
    except Exception as e: raise e
    
    return list_color

def norm_pos(pos,length):
    # normalize between 0 - 255
    list_p = []
    max_, min_ = find_max_min(pos)
    try:
        for i in range(len(pos)):
            _list = []
            for j in range(len(pos[0])):
                z = (pos[i][j]-min_)/(max_-min_) * length
                _list.append(int(z))
            list_p.extend([_list])
            # print(list_color[i])
    except Exception as e: raise e
    
    return list_p

def rotate(img,width,height,deg,bg):
    # elem = [[bg]*width]*height
    elem_x = []
    elem_y = []
    for i in range(height):
        l_x = []
        l_y = []
        for j in range(width):
            x = (i*m.cos(m.pi*deg/180))+(j*m.sin(m.pi*deg/180))
            y = -(i*m.sin(m.pi*deg/180))+(j*m.cos(m.pi*deg/180))
            # if(x < width and y < height):
            #     elem[int(y)][int(x)] = img[i][j]
            l_x.append(int(x))
            l_y.append(int(y))
        elem_x.extend([l_x])
        elem_y.extend([l_y])
        
    max_x, min_x = find_max_min(elem_x)
    max_y, min_y = find_max_min(elem_y)
    # elem = [[255]*(abs(max_x)+abs(min_x)+1)]*(abs(max_y)+abs(min_y)+1)
    for i in range(height):
        for j in range(width):
            # if(img[i][j] == 0):
            #     elem[elem_y[i][j]+abs(min_y)][elem_x[i][j]+abs(min_x)] = img[i][j]
            if(elem_x[i][j]+abs(min_x)-36 >= 0 and elem_x[i][j]+abs(min_x)-36 <200 and elem_y[i][j]+64 >=0 and elem_y[i][j]+64 < 200 and img[elem_y[i][j]+64][elem_x[i][j]+abs(min_x)-36]==255):
                temp = img[elem_y[i][j]+64][elem_x[i][j]+abs(min_x)-36]
                img[elem_y[i][j]+64][elem_x[i][j]+abs(min_x)-36] = img[i][j]
                img[i][j] = temp
 
    return img

def mul_comp(comp_arr,width,height, ccomp):
    elem = []
    for i in range(height):
        l = []
        for j in range(width):
            mul = np.array([comp_arr[i][j]])
            mul2 = np.array([ccomp])
            z = np.vdot(mul, mul2)
            l.append(z)
        elem.extend([l])
    return elem
            
def tranx_pos(img,width,height):
    elem = []
    for i in range(height):
        l = []
        for j in range(width):
            if(i<30 and j<20):
                l.append(0)
            else:
                l.append(img[i-20][j-30])
        elem.extend([l])
    return elem
            
    





