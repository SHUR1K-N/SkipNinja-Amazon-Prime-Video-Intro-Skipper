import pyautogui
import time


def skipIntro():
    buttonLocation = pyautogui.locateCenterOnScreen("Button.ref")
    if buttonLocation is None:
        skippedFlag = False
        pass
    else:
        pyautogui.click(buttonLocation)
        skippedFlag = True
    return(skippedFlag)


if __name__ == '__main__':
    displaySize = pyautogui.size()
    while True:
        try:
            skippedFlag = skipIntro()
            if skippedFlag is True:
                pyautogui.click(x=(displaySize.width - 20), y=(displaySize.height // 2), clicks=3, interval=0.4)
        except:
            continue
        time.sleep(1)
