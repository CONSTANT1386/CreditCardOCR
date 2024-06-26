import cv2

def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts] #用一个最小的矩形，把找到的形状包起来x,y,h,w
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # what's zip() get is a list of tuple
    # key parameter is to get the value of the iterable, which the sorting depend on 
    # the key parameter is a function acting on every element in the first parameter of the sort() function, i.e. a iterablle object, it is a list of tuple generated by zip() here
    # Thus, the input of anonymous fuction lambda b, is the element of zip(cnt, boundingBoxes), i.e. a tuple like (countour, boundingBoxes)
    # Thus b[1] means the second element of tuple, i.e. the bounding box (x,y,w, h), and b[1][i] means sorting depend of the x(i=0), y(i=1)
    return cnts, boundingBoxes

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized