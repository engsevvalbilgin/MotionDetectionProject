
import cv2 as cv
import numpy as np
video=cv.VideoCapture('video')

background_substractor = cv.createBackgroundSubtractorMOG2(history=150, varThreshold=16, detectShadows=True)

flag = 0  # Hareket tespit edildi mi?
start_time = None  # Hareketin başlangıç zamanı
end_time = None  # Hareketin bitiş zamanı

while True:
    ret, frame = video.read()
    if not ret:
        break  # Video bittiğinde döngüden çık

    foreground = background_substractor.apply(frame)
    _, thresh = cv.threshold(foreground, 200, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    motion_found = False  # Bu çerçevede hareket var mı?

    # Hareketi tespit et
    for contour in contours:
        if cv.contourArea(contour) > 500:  # Küçük gürültüyü önlemek için
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_found = True

    # Hareket başladıysa ve daha önce hareket tespit edilmediyse, zaman kaydet
    if motion_found and flag == 0:
        start_time = video.get(cv.CAP_PROP_POS_MSEC)  # Başlangıç zamanını kaydet
        flag=1

    # Hareket bittiğinde, zaman kaydet
    if not motion_found and flag==1:
        end_time = video.get(cv.CAP_PROP_POS_MSEC)  # Bitiş zamanını kaydet
        print(f"Hareket Başlangıcı: {start_time / 1000:.2f}. saniye, Hareket Bitişi: {end_time / 1000:.2f}. saniye")


    cv.imshow('Motion Detection with Timestamps', frame)

    if cv.waitKey(100) & 0xFF == ord('q'):
        break
#
video.release()
cv.destroyAllWindows()