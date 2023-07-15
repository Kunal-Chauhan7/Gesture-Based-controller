import serial
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key , Controller 

s = serial.Serial('COM7',9600)

keyboard = Controller()
mouse = pynput.mouse.Controller()

while True:
    data = s.readline()

    if(data.decode().strip()=="up"):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        print("up")
    if(data.decode().strip()=="down"):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        print("down")
    if(data.decode().strip()=="left"):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        print("left")
    if(data.decode().strip()=="right"):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        print("right")
    if(data.decode().strip()=="leftClick"):
        mouse.click(Button.left)
        print("leftClick")
    if(data.decode().strip()=="rightClick"):
        mouse.click(Button.right)
        print("rightClick")
        