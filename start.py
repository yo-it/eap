#!/usr/bin/env python
import subprocess, signal
import time

def main():
    
    while True:
        p = subprocess.Popen(['python', 'netattack2.py'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        print out
        print "Start : %s" % time.ctime()
        time.sleep(10)
        print "Start1 : %s" % time.ctime()
    
    
    
if __name__ == "__main__":
    main()
