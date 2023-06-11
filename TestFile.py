import threading

class ThreadTest:
    def __init__(self):
        self.Printing = "Hello"
        self.running = True
    def Threaded(self):
        while self.running:
            print(self.Printing)


