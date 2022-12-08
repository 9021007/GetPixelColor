# python module for getting the color of a pixel on screen

# import the necessary modules
from io import BytesIO
import os
import platform  
from PIL import Image
from sys import platform
import pyautogui
import numpy as np


def checkForIssues(num):
    if (type(num) != int):
        raise TypeError("x, y, width, and height must be integers")
    if (num < 0):
        raise ValueError("x, y, width, and height must be positive")


# the function takes 2 arguments, the x and y coordinates of the pixel
# returns a tuple of the RGBA values of the pixel
def pixel(x, y):
    checkForIssues(x)
    checkForIssues(y)
    if (platform == "darwin"):
        from pasteboard import TIFF, Pasteboard
        os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',1,1 -c')
        im = Pasteboard().get_contents(TIFF)
        im = Image.open(BytesIO(im))
        return (tuple(im.getpixel((0,0))))
        # return (tuple(os.popen("static/get-pixel-color " + str(x) + " " + str(y)).read()))
    elif (platform == "win32" or platform == "linux" or platform == "linux2"):
        # screenshot the area, saving to a temporary folder based on the OS
        if (platform == "win32"):
            import win32gui
            im = win32gui.GetPixel(win32gui.GetDC(win32gui.GetDesktopWindow()), x, y)
        elif (platform == "linux" or platform == "linux2"):
            im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, 1, 1))
        return (im.getpixel((0,0)))
    else:
        return ("Error: Unsupported operating system.")

def average(x, y, width, height):
    checkForIssues(x)
    checkForIssues(y)
    checkForIssues(width)
    checkForIssues(height)
    if (platform == "darwin"):
        from pasteboard import TIFF, Pasteboard
        os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',' + str(width) + ',' + str(height) + ' -c')
        im = Pasteboard().get_contents(TIFF)
        im = Image.open(BytesIO(im))
        return (tuple(np.average(np.array(im), axis=(0,1)).astype(int)))
    elif (platform == "win32" or platform == "linux" or platform == "linux2"):
        # screenshot the area, saving to a temporary folder based on the OS
        if (platform == "win32"):
            im = pyautogui.screenshot('C:\\Windows\\Temp\\screenshot.png', region=(x, y, width, height))
        elif (platform == "linux" or platform == "linux2"):
            im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, width, height))
        return (tuple(np.average(np.array(im), axis=(0,1)).astype(int)))
    else:
        return ("Error: Unsupported operating system.")

def area(x, y, width, height):
    checkForIssues(x)
    checkForIssues(y)
    checkForIssues(width)
    checkForIssues(height)
    if (platform == "darwin"):
        from pasteboard import TIFF, Pasteboard
        os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',' + str(width) + ',' + str(height) + ' -c')
        im = Pasteboard().get_contents(TIFF)
        im = Image.open(BytesIO(im))
        return (np.array(im).tolist())
    elif (platform == "win32" or platform == "linux" or platform == "linux2"):
        # screenshot the area, saving to a temporary folder based on the OS
        if (platform == "win32"):
            im = pyautogui.screenshot('C:\\Windows\\Temp\\screenshot.png', region=(x, y, width, height))
        elif (platform == "linux" or platform == "linux2"):
            im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, width, height))
        return (np.array(im).tolist())
    else:
        return ("Error: Unsupported operating system.")