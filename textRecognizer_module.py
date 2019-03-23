import cv2
import numpy as np
import pytesseract


def do_recognition(image, language):
    #changes img
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(image, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.resize(img, (0, 0), fx=2, fy=2)
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.imwrite("selected.png", img)  # for debuging
    result = pytesseract.image_to_string(img, lang=language, config='--psm 6')
    print(result)
    return result


def get_text(img, lang):
    return do_recognition(img, lang)



