#SERVER

import cv2
import socket
import sys
import pickle
import struct

HOST=''
PORT=8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b'' 
payload_size = struct.calcsize("L")
while True:
    # Retrieve message size
##    while len(data) < payload_size:
##        data += conn.recv(4096)
    data = conn.recv(4096)
    print(data.decode())

    #data=conn.recv(4096)
##    print(data)
##    packed_msg_size = data[:payload_size]
##    data = data[payload_size:]
##    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
##    while len(data) < msg_size:
##        data += conn.recv(4096)
##
##    frame_data = data[:msg_size]
##    data = data[msg_size:]
##
##    # Extract frame
##    frame = pickle.loads(frame_data)
##    print(type(frame))
##
##    # Display
##    cv2.imshow('frame', frame)
##    
##    cv2.waitKey(1)
