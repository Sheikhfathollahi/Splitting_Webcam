import cv2

def Cartoon_Transform(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray,3)
    edges = cv2.adaptiveThreshold(gray_blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3,3)
    Color = cv2.bilateralFilter(gray , 8 , 250,250)
    Cartoon = cv2.bitwise_and(Color , Color , mask = edges)
    return Cartoon
