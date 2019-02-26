#Thanks to https://github.com/tax1driver for having https://github.com/tax1driver/steamaccgen/blob/master/app.js as a reference for me to look at
#
#
#Abandoning this because I can't find an email service that steam doesn't ban and has an api
#
#
import os
import secrets
import requests
import json
import webbrowser
import string
import time

def randString(strLen):
    randString = []
    for i in range(strLen):
        randString.append(chr(int(secrets.choice(range(33, 126)))))
    randString = ''.join(randString)
    return str(randString)
    
def randStringLegal(strLen):
    legalChars = string.ascii_letters + string.digits
    randString = []
    for i in range(strLen):
        randString.append(secrets.choice(legalChars))
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
    
def getEmails(inbox):
    print(json.dumps(inbox, indent=4,)+'\n')
    inboxToken = inbox['result']['token']
    inboxAddress = inbox['result']['email']['address']
    inboxId = inbox['result']['email']['id']
    headers = {"X-Burner-Key": inboxToken}
    emails = requests.get('https://burner.kiwi/api/v1/inbox/'+inboxId+'/messages', headers=headers)
    emails = emails.json()
    emails = emails['result']
    print("Emails:"+'\n')
    print(json.dumps(emails, indent=4,)+'\n')
    return(emails)
    
def verifyEmail(emails):
    if (emails != "null"):
        for msg in emails:
            print(json.dumps(['sender'], indent=4,)+'\n')
    else:
        print("No emails are in this inbox")
    
def createAccount():
    with requests.Session() as session:
        inbox = getNewEmail()
        inbox = inbox.json()
        inboxEmail = inbox['result']['email']['address']
        captchaGid = getCaptchaGid()
        accountName = randStringLegal(10)
        password = randString(10)
        print("account name: "+accountName,"password: "+password, sep='\n')
        print(forgeCaptchaURL(captchaGid))
        captchaText = input("Please input the characters from this captcha: ")
        payload = {'email': inboxEmail,'captchagid': captchaGid,'captcha_text': captchaText}
        accResponse = session.post('https://store.steampowered.com/join/ajaxverifyemail', data=payload)
        #check and verify email
        emails = getEmails(inbox)
        verifyEmail(emails)
        # #############################
        accResponse = accResponse.json()
        sessionId = accResponse['sessionid']
        payload = {'count': 1,'lt': 0,'accountname': accountName,'password': password,'creation_sessionid': sessionId}
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        accResponse = session.post('https://store.steampowered.com/join/createaccount', data=payload, headers=headers)
        print(json.dumps(accResponse.text, indent=4,)+'\n')
        #main()
    
        
def main():
    #print(randString(10))
    #print(getCaptchaGid())
    #print(forgeCaptchaURL(getCaptchaGid()))
    #print(getNewEmail())
    #startAccCreation()
    #finishAccCreation()
    createAccount()
    
    
main()
    

