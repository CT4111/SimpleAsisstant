from datetime import datetime
import webbrowser
import os


def Abilatie_One():
    print("doing shit")
def OpenWebsite(url):
    webbrowser.open(url)
def SearchWebsite(url):
    print(url)
    webbrowser.open("https://www.google.com/search?q="+ url)
def StartFile(path):
    os.startfile(path)