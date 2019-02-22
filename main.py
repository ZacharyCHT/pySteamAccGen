import os
import secrets
import requests
import json

def randString(strLen):
    randString = []
    for i in range(strLen):
        randString.append(chr(int(secrets.choice(range(33, 126)))))
    randString = ''.join(randString)
    return str(randString)

def getCaptchaGid():
    gid = requests.post('https://store.steampowered.com/join/refreshcaptcha')
    gid = str(gid.text.strip('gid"{}:'))
    #print(gid)
    return(gid)    
    
def forgeCaptchaURL(gid):
    return('https://store.steampowered.com/login/rendercaptcha?gid=' + gid) 
    
    


def main():
    #print(randString(10))
    #print(getCaptchaGid())
    #print(forgeCaptchaURL(getCaptchaGid()))
    


    
    
    
main()
    












