# -*- coding utf-8 -*-

class Counter:
    counters = []

    '''
    Counter class, used to count time.
    '''
    def __init__(self, count_time = 0):
        Counter.counters.append(self)
        self.count_time = count_time
        self.countdown = 0
        self.is_pause = False
    
    # check if the counter is in ok state
    # if reset is True, reset the counter when it's ok
    def ok(self, reset = True):
        if self.countdown == 0:
            if reset: self.reset()
            return True
        return False
    
    # set the counter to pause state
    def pause(self):
        self.is_pause = True
    
    # Set the counter to start counting state
    def start(self):
        self.is_pause = False
    
    # switch between start and pause state
    def switch(self):
        self.is_pause = not self.is_pause
    
    # reset the counter
    # if count_time is given, reset to that value
    def reset(self, count_time = 0):
        if count_time: self.count_time = count_time
        self.countdown = self.count_time
    
    # delete the counter from the list of counters
    def delete(self):
        Counter.counters.remove(self)
    
# tick function to be called every tick
def tick():
    for counter in Counter.counters:
        if counter.countdown and not counter.is_pause:
            counter.countdown -= 1
