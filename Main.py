import cv2

def Cartoon_Transform(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray,3)
    edges = cv2.adaptiveThreshold(gray_blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3,3)
    Color = cv2.bilateralFilter(gray , 8 , 250,250)
    Cartoon = cv2.bitwise_and(Color , Color , mask = edges)
    return Cartoon


Video = cv2.VideoCapture(0)

while True:
    ret, frame0 = Video.read()
    r = cv2.selectROI("Image", frame0, fromCenter = False, showCrosshair = False)
    break

while True:
    ret, frame = Video.read()

    rect_img = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    Cartoon_rect = Cartoon_Transform(rect_img)

    sketcher_rect_rgb = cv2.cvtColor(Cartoon_rect, cv2.COLOR_GRAY2RGB)

    # Replacing the Cartoon image on ROI
    frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])] = sketcher_rect_rgb

    cv2.imshow("Cartoon ROI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Video.release()
cv2.destroyAllWindows()
