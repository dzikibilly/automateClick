import time
import pyautogui
import datetime


def sleepTo(string):
    #2017/10/25_11:28
    year = int(string[0:4])
    month = int(string[5:7])
    day = int(string[8:10])
    hour = int(string[11:13])
    minute = int(string[14:16])

    # print("%r" % year)
    # print("%r" % month)
    # print("%r" % day)
    # print("%r" % hour)
    # print("%r" % minute)
    while datetime.datetime.now().timestamp() <= datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute).timestamp():
        # pyautogui.moveTo(x=100 , y=100,duration=2,pause=1)
        # pyautogui.moveTo(x=200 , y=200,duration=2)
        # pyautogui.press('h')
        pyautogui.press('enter',interval=10)
        print("{} enter pressed".format(datetime.datetime.now()))


def findObroty():
    toClick = pyautogui.locateCenterOnScreen('do_klikniecia.png')
    pyautogui.click(toClick)
    pyautogui.typewrite('10')

if __name__ == "__main__":

    sleepTime = input("Podaj czas przykladowo 2017/10/25_11:28 = ")
    time.sleep(2)
    sleepTo(sleepTime)
    findObroty()

    print("KONIEC")

