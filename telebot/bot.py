#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:19:50 2020

@author: bharat
"""
def get_reply(text):
    if text == "/help":
        msg = "Under Construction"
        return msg
    
    elif text == "/start":
        msg = "At your service for some RED PILL content"
        return msg
    elif text == "/introduceme":
        msg = "https://bookofpook.com/ \n https://therationalmale.com/ \n https://www.youtube.com/channel/UC8eLDzfH6YfZRDbDuMsNWiA \n https://www.youtube.com/user/EntrepreneursInCars"
        return msg
    else:
        msg = ""
        return msg
