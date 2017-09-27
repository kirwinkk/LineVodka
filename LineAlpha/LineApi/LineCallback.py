# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Enter PinCode '" + pin + "' to your mobile phone in 2 minutes")

    def QrUrl(self, url):
        self.callback("請在2分鐘內登陸戦神所發行的網址\n" + url)

    def default(self, str):
        self.callback(str)
