import threading
import time as t

class Stopwatch:
    def __init__(self, time, chess):
        self.time = time
        self.wTime = time
        self.bTime = time
        self.running = False
        self.c = chess

    def setTime(self, time):
        self.wTime = time
        self.bTime = time

    def start(self):
        if not self.running and self.wTime > 0 and self.bTime > 0:
            self.running = True
            self.thread = threading.Thread(target=self.update_time)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False

    def update_time(self):
        while self.running:
            t.sleep(1)
            if(self.c.white_turn):
                self.wTime -= 1
            else:
                self.bTime -= 1
            self.c.board.updateClocks()

            if(self.c.gameEnd):
                self.stop()
