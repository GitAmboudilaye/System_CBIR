import cv2

def read_img(image):
    # read image uplaod
    img_gray = cv2.imread(image, 0)
    return img_gray