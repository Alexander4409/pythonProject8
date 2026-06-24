#pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

import cv2
from numpy.ma.core import count


#rgb(255,255,255) белый цвет

def start_computer_vision():
    #Загрузка предобученной модели для поиска лиц
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # подключение камеры
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()

        if not success:
            print("Не удалось получить изображение с камеры")
            break

        frame = cv2.flip(frame,1)
        #переводим изображение в серый цвет
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ищем лица в кадре
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
        # рисуем рамку вокруг найденных лиц

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x + w, y + h), (0,255,0),4)

        object_count = f'Object detected {len(faces)}'
        cv2.putText(frame, object_count, (20,50), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)

        #кнопка выключения
        cv2.imshow("Summer_FM_9",frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break


    #освобождение ресурсов и выключение камеры
    camera.release()
    cv2.destroyAllWindows()

start_computer_vision()






















