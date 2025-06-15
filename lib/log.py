# -*- coding: utf-8 -*-

class Log:
    data = []

    '''
    Log class, used to log messages.
    '''
    def __init__(self, msg: str, echo: bool = True):
        Log.data.append(msg)
        if echo: print('LOG msg> ', msg)
