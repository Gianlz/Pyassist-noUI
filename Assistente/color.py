import cv2
import dxcam
import numpy as np
from win32api import GetAsyncKeyState
import serial
import threading

fov = 38
lower = np.array([150, 110, 200])
upper = np.array([150, 255, 255])
xspd = 0.37
yspd = 0.22
center = fov/2
arduino = serial.Serial('COM3', 115200)

camera = dxcam.create(device_idx= 0, output_color= "BGRA")
left, top = (1920 - fov) // 2, (1080 - fov) // 2
right, bottom = left + fov, top + fov
region = (left, top, right, bottom)

camera.start(region=(region), target_fps=400)

def get_frames(camera):
    while True:
        global img
        img = camera.get_latest_frame()

def mousemove(x,y):
    if GetAsyncKeyState(0x02) < 0:
        data = f"{int(x)}:{int(y)}"
        arduino.write(data.encode())

def move_mouse():
    while True:
        global img
        img = camera.get_latest_frame()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower,upper)
        kernel = np.ones((3,3), np.uint8)
        dilated = cv2.dilate(mask,kernel,iterations= 5)
        thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            M = cv2.moments(thresh)
            point_to_aim = (int(M["m10"] / M["m00"]), (int(M["m01"] / M["m00"])))
            closestX = int(point_to_aim[0] - center) * xspd
            closestY = int(point_to_aim[1] - center/0.727) * yspd

            mousemove(closestX, closestY)

camera_thread = threading.Thread(target=get_frames, args=(camera,))
camera_thread.start()

move_mouse_thread = threading.Thread(target=move_mouse)
move_mouse_thread.start()
