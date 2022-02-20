from threading import Thread, Event
from turtle import Screen


class Updater(Thread):
    def __init__(self, screen: Screen):
        super().__init__()
        self.setDaemon(True)
        self._screen = screen
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def run(self):
        while not self._stop.is_set():
            self._screen.update()
