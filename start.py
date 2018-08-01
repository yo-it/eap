#!/usr/bin/env python
import subprocess, signal
import time

def main():
    
    while True:
        p = subprocess.Popen(['python', 'netattack2.py'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        time.sleep(100)
    
    
    
if __name__ == "__main__":
    main()
