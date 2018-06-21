#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zbar
from PIL import Image
import cv2


"""
Realiza a leitura do QR CODE
Baseado no código disponível em:
https://github.com/allenywang/Real-Time-QR-Recognizer-Reader-and-Decoder
"""

def qr_cam():
    """Realiza a leitura do qr-code pela camera."""
    capture = cv2.VideoCapture(0)
    try:
        while True:
            # To quit this program press q.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Breaks down the video into frames
            ret, frame = capture.read()

            # Displays the current frame
            cv2.imshow('Leitor de Voto', frame)

            # Converts image to grayscale.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
            image = Image.fromarray(gray)
            width, height = image.size
            zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

            # Scans the zbar image.
            scanner = zbar.ImageScanner()
            scanner.scan(zbar_image)

            # Prints data from image.
            for decoded in zbar_image:
                retorno=decoded.data.replace("[","").replace("]","").replace(" ","").split(",")
                cv2.destroyAllWindows()
                return retorno
    except Exception as e:
        print("funcionando")
