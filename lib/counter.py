# -*- coding utf-8 -*-

class Counter:
    counters = []

    def __init__(self, count_time = 0):
        Counter.counters.append(self)
        self.count_time = count_time
        self.countdown = 0
        self.is_pause = False
    
    def ok(self, reset = True):
        if self.countdown == 0:
            if reset: self.reset()
            return True
        return False
    
    def pause(self):
        self.is_pause = True
    
    def start(self):
        self.is_pause = False
    
    def switch(self):
        '''
        switch start/pause state of the counter
        '''
        self.is_pause = not self.is_pause
    
    def reset(self, count_time = 0):
        if count_time: self.count_time = count_time
        self.countdown = self.count_time
    
    def delete(self):
        Counter.counters.remove(self)
    
def tick():
    for counter in Counter.counters:
        if counter.countdown and not counter.is_pause:
            counter.countdown -= 1