#CLIENT
import cv2
import socket
import sys
import pickle
import struct

cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8089))

  
while(True):  
    # Capture the video frame by frame
    ret, frame = cap.read()
  
    # Display the resulting frame
    # cv2.imshow('frame', frame)
      
    # the 'q' button is set as the quitting button you may use any desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #cv2.imshow('frame', frame)
    data = pickle.dumps(frame)
    s.send("hello world".encode())
    #s.sendall(struct.pack("L", len(data))+data)
    #s.send("Hello World")

