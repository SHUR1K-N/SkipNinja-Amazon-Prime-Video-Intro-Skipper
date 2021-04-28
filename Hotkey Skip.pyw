import pyautogui
import keyboard
import time; import os


def skipIntro():
    buttonLocation = pyautogui.locateCenterOnScreen("Button.ref")
    if buttonLocation is None:
        skippedFlag = False
        pass
    else:
        pyautogui.click(buttonLocation)
        skippedFlag = True
    buttonLocation = None
    return(skippedFlag)


if __name__ == '__main__':
    displaySize = pyautogui.size()
    while True:
        if keyboard.is_pressed("\\"):
            os.exit()
        if keyboard.is_pressed('ctrl'):
            skippedFlag = skipIntro()
            time.sleep(0.4)
            if skippedFlag is True:
                pyautogui.click(x=(displaySize.width - 20), y=(displaySize.height // 2), clicks=2, interval=0.4)
        time.sleep(0.0001)
