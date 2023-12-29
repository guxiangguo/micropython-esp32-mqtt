#-*-coding:utf-8-*-
import time
from mqtt import *

while (True):
    if run() == 'FAILED':
        print('FAILED,retry to connect')
        time.sleep(5)
        
