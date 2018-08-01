#!/usr/bin/env python
import subprocess, signal

def main():
    p = subprocess.Popen(['python', 'netattack2.py'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    print out
    
if __name__ == "__main__":
    main()
