import pyautogui
import os
import getpixelcolor

x, y = pyautogui.position()
print(x, y)
# print(os.system("ls"))
print(getpixelcolor.pixel(x, y))

#execute relative to this file
