#!/usr/bin/python3
import hashlib
import random

def mkacc(n):
    with open('readme.txt', 'w') as f:
        for i in range(1,n):
            pref = random.randint(1,4)
            if pref == 1:
                prefstr = 'guest'
            if pref == 2:
                prefstr = 'client'
            if pref == 3:
                prefstr = 'student'
            if pref == 4:
                prefstr = 'host'
            acc = prefstr +'-0'+str(random.randint(1,9))+'-'+hashlib.sha1(str(random.randint(1,n)).encode('utf-8')).hexdigest()[1:10]
            f.write(acc)
            f.write('\n')


def mkpass():
    return True

def writefile():
    return True
mkacc(20)