import pyautogui
import time

def GetRGB(x, y):
    res = pyautogui.pixel(int(x), int(y))
    print(res)

def GetTarget():
    # for pos in pyautogui.locateAllOnScreen('someButton.png')
    target_location = pyautogui.locateOnScreen('target.PNG', confidence=0.95)
    print(target_location)
    target_coordinate = pyautogui.center(target_location)

    x, y = target_coordinate
    print(x, y)

    # GetRGB(x, y)  

    # TODO :
    if pyautogui.pixelMatchesColor(int(x), int(y), (205, 236, 194), tolerance=300):
        pyautogui.press('space')     # press the space arrow key
        print("Press Space!")
    else:
        print("Wait...")


    # # pyautogui.click(x, y)

    # GetRGB(x, y)    

# Need to get target and move RGB and then through pixelMatchesColor to press space if move colser target
def main():
    GetTarget()


if __name__ == "__main__":
    main()