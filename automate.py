import time
from selenium import webdriver
import pyautogui as pyg
import os

# Delaying for Positioning the Mouse in the Right Place ==> If the code after it is the same this delay has no mean
time.sleep(10)
# Opens Chrome With OS
os.system('start chrome "https://pyautogui.readthedocs.io/en/latest/keyboard.html"')
# Opens Os with selenium 
# browser = webdriver.Chrome()
# browser.get('https://pyautogui.readthedocs.io/en/latest/keyboard.html')
time.sleep(2) # Delaying By 2 secs
pyg.click()
pyg.scroll(-150) # Scrolling ( DOWN ) for About 150 Clicks By Mouse
time.sleep(1)
pyg.scroll(-150) # Scrolling ( DOWN ) for About 150 Clicks By Mouse
time.sleep(1)
pyg.scroll(-50) # Scrolling ( DOWN ) for About 50 Clicks By Mouse
time.sleep(1)
pyg.scroll(200) # Scrolling ( UP ) for About 150 Clicks By Mouse
time.sleep(2)
pyg.hotkey('ctrl','t') # Openning a New Tab in the Program Opening like the most hotkeys in most gui programs