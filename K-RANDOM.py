import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://youtube.com/c/KhaliDTechBd1?utm_source=EKLEiJECCKjOmKnC5IiRIQ')
 
        from RANDOM import khld
 
        khld()
 
 
 
elif bit == "32bit":

        os.system('xdg-open https://youtube.com/c/KhaliDTechBd1?utm_source=EKLEiJECCKjOmKnC5IiRIQ')
 
        os.system('python Random32.py')
