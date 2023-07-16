import serial
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key , Controller 
import time

s = serial.Serial('COM7',9600)

keyboard = Controller()
mouse = pynput.mouse.Controller()

while True:
    data = s.readline()

    if(data.decode().strip()=="up"):
        keyboard.press(Key.up)
        time.sleep(0.4)
        keyboard.release(Key.up)
        print("up")
    if(data.decode().strip()=="down"):
        keyboard.press(Key.down)
        time.sleep(0.4)
        keyboard.release(Key.down)
        print("down")
    if(data.decode().strip()=="left"):
        keyboard.press(Key.left)
        time.sleep(0.4)
        keyboard.release(Key.left)
        print("left")
    if(data.decode().strip()=="right"):
        keyboard.press(Key.right)
        time.sleep(0.4)
        keyboard.release(Key.right)
        print("right")
    if(data.decode().strip()=="leftClick"):
        mouse.press(Button.left)
        time.sleep(1)
        mouse.release(Button.left)
        print("leftClick")
    if(data.decode().strip()=="rightClick"):
        mouse.press(Button.right)
        time.sleep(1)
        mouse.release(Button.right)
        print("rightClick")
        