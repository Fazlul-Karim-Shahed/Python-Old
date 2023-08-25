import numpy as np
import urllib.request as rq
import cv2

url = 'http://192.168.0.103/'




# Initialize an OpenCV window
cv2.namedWindow('ESP32-CAM Stream for 299 Project', cv2.WINDOW_AUTOSIZE)

# Read the stream
while True:
    # Open the URL with the ESP32-CAM stream
    stream = rq.urlopen(url)
    # Read a frame from the stream
    img_array = np.array(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    # Show the frame in the OpenCV window
    cv2.imshow('ESP32-CAM Stream for 299 Project', img)

    # Capture an image and save it
    key = cv2.waitKey(5)
    if key == ord('c'):
        # cv2.imwrite('captured_image.jpg', img)
        # print('Image captured and saved!')
        break
    
    cv2.destroyAllWindows()


# Release the OpenCV window and the stream

# stream.close()