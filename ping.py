import os
import time

try:
    while(True):

        with open("ipFile.txt", "r") as f:
            l = f.readlines()

            for line in l:
                os.system("ping %s" % line)
        
        with open("configFile.txt", "r") as f:
            time.sleep(int(f.read()))
        
        os.system("cls")

except e as Exception:
    print e