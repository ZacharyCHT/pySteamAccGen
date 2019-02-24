#Thanks to https://github.com/tax1driver for having https://github.com/tax1driver/steamaccgen/blob/master/app.js as a reference for me to look at
#
#
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
    return(gid)    
    
def forgeCaptchaURL(gid):
    return('https://store.steampowered.com/login/rendercaptcha?gid=' + gid) 
    
def getNewEmail():
    inbox = requests.get('https://burner.kiwi/api/v1/inbox')
    if (inbox.status_code == 200):
        print("Get request succeeded! here is the response: "+"\n")
        inbox = inbox.json()
        print(json.dumps(inbox, indent=4,)+'\n')
        inboxToken = inbox['result']['token']
        inboxEmail = inbox['result']['email']['address']
        inboxId = inbox['result']['email']['id']
        #print("Inbox token = "+inboxToken, "Inbox address = "+inboxEmail, "Inbox id = "+inboxId, sep='\n')
    else:
        print("Get request failed, maybe trying again will work")
    return(inboxToken,inboxEmail,inboxId)

def main():
    #print(randString(10))
    #print(getCaptchaGid())
    #print(forgeCaptchaURL(getCaptchaGid()))
    getNewEmail()
    print("Inbox token = "+inboxToken, "Inbox address = "+inboxEmail, "Inbox id = "+inboxId, sep='\n')
    


    
    
    
main()


