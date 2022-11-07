import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://github.com/KHALID-404')
 
        from RANDOM import khld
 
        khld()
 
 
 
elif bit == "32bit":
 
        os.system('python Random.py')
