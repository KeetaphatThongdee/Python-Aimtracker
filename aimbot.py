#Aimbot ver1 by Keetaphat
from pyautogui import *
import time
import keyboard
import pyautogui
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('p') == False:#press p to stop
    #for pos 1
    a = 508
    b = 660
    #for pos 2
    c = 625
    d = 649
    #for pos 3
    e = 723
    f = 648
    #for pos 4
    g = 826
    h = 649
    #pos 1
    if pyautogui.pixel(a, b)[1] == 0:
        click(a, b)
    #pos 2
    if pyautogui.pixel(c, d)[1] == 0:
        click(c, d)
    #pos 3
    if pyautogui.pixel(e, f)[1] == 0:
        click(e, f)
    #pos 4
    if pyautogui.pixel(g, h)[1] == 0:
        click(g, h)

