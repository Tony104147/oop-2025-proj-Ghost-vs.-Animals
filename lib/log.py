# -*- coding: utf-8 -*-

class Log:
    data = []

    def __init__(self, msg: str, echo: bool = True):
        Log.data.append(msg)
        if echo: print('LOG msg> ', msg)