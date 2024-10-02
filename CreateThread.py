import threading
import time

class CreateT(threading.Thread):
    def __init__(self, target=None, args=()):
        super().__init__()
        self.can_run = threading.Event()
        self.thing_done = threading.Event()
        self.thing_done.set()
        self.can_run.set()    
        self.func = target
        self.args = args
        self.cond = True

    def run(self):
        while True:
            self.can_run.wait()
            try:
                self.thing_done.clear()
                self.func(self, *self.args)
                time.sleep(1)
            finally:
                self.thing_done.set()

    def pause(self):
        self.can_run.clear()
        self.thing_done.wait()
        self.cond = False

    def resume(self):
        self.can_run.set()
        self.cond = True