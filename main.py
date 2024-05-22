import pynput
import keyboard
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Controller2
mouse = Controller()
keyboard2 = Controller2()

def press(key: str):
    keyboard2.press(key)
    time.sleep(0.1)
    keyboard2.release(key)

def type_message(message: str):
    for char in message:
      press(char)

message = "This message will be typed by your keyboard if you run this code"
type_message(message)
