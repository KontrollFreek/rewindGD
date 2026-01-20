import webbrowser
import pyautogui
import time

pyautogui.alert(text='This script will run commands that may look suspicious, but no harmful activity will occur.', title='Warning!', button='I Understand')

webbrowser.open('steam://nav/console')

while True:
    time.sleep(0.5)
    try:
        steam_window = pyautogui.getWindowsWithTitle("Steam")
    except:
        continue

    if len(steam_window) > 0:
        steam_window = steam_window[0]
        steam_window.restore()
        steam_window.activate()

        centerX = steam_window.left + (steam_window.width / 2)
        bottomY = steam_window.top + steam_window.height

        pyautogui.leftClick(centerX, bottomY - 80)

        break
    
pyautogui.typewrite('download_depot 322170 322171 7678373534998244044')
pyautogui.press('enter')
webbrowser.open('steam://nav/library')

pyautogui.alert(text='Geometry Dash version 2.2074 has been successfully installed! Please wait for the download to finish, and then you can run Geometry Dash with Offline Mode ON.', title='Success!', button='OK')