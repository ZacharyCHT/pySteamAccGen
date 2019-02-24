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
        #print("Get request succeeded! here is the response: "+"\n")
        #inbox = inbox.json()
        #print(json.dumps(inbox, indent=4,)+'\n')
        #inboxToken = inbox['result']['token']
        #inboxEmail = inbox['result']['email']['address']
        #inboxId = inbox['result']['email']['id']
        return(inbox)
        #print("Inbox token = "+inboxToken, "Inbox address = "+inboxEmail, "Inbox id = "+inboxId, sep='\n')
        #return(print("Inbox token = "+inboxToken, "Inbox address = "+inboxEmail, "Inbox id = "+inboxId, sep='\n'))
        #print(inboxToken,inboxEmail,inboxId, sep='\n')
    else:
        print("Get request failed, maybe trying again will work")


def startAccCreation():
    inbox = getNewEmail()
    inbox = inbox.json()
    inboxEmail = inbox['result']['email']['address']
    captchaGid = getCaptchaGid()
    print("Inbox address = "+inboxEmail)
    print(forgeCaptchaURL(captchaGid))
    captchaText = input("Please input the characters from this captcha: ")
    payload = {'email': inboxEmail,'captchagid': captchaGid,'captcha_text': 'null'}
    accResponse = requests.post('https://store.steampowered.com/join/ajaxverifyemail', data=payload)
    accResponse = accResponse.json()
    print(json.dumps(accResponse, indent=4,)+'\n')
    
def finishAccCreation():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    accountName = randString(10)
    password = randString(10)
    payload = {'count': 10,'lt': 0,'accountname': accountName,'password': password,'creation_sessionid': 0}
    accFinished = requests.post('https://store.steampowered.com/join/createaccount', data=payload, headers=headers)
    
def main():
    #print(randString(10))
    #print(getCaptchaGid())
    #print(forgeCaptchaURL(getCaptchaGid()))
    #print(getNewEmail())
    startAccCreation()
    finishAccCreation()
    
main()
    

