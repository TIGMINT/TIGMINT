import requests
import json

items= {}
def save(service_name,url):
    # items[service_name]= url
    # if url != None:
    global items
    items[service_name]= url
    # items = dict(service = service_name, profile = url)
    
def instagram(username):
    service_name = "Instagram"
    url  = "https://instagram.com/" + username
    response = requests.get(url + '/')
    # print(response)
    if (response.status_code == 200 ):
        # a+
        # sys.stdout = open("userpresent.txt", "a+")
        print("*[INSTAGRAM] " + url)
        save(service_name,url)
        # sys.stdout.close()
        return service_name, url
    else:
        return None



def github(username):
    service_name = "Github"
    url  = "https://github.com/" + username
    response = requests.get(url+'/')
    if(response.status_code == 200):
        print("*[Github] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None



def twitter(username):
    service_name = "Twitter"
    url = "https://mobile.twitter.com/" + username
    response = requests.get(url)
    #response_text = response.text
    #print(response_text)
    if(response.status_code == 200):
        url = url.replace("mobile.","")
        print("*[Twitter] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None


def reddit(username):
    service_name = "Reddit"
    url = "https://www.reddit.com/user/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Reddit] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None

def facebook(username):
    service_name = "Facebook"
    url = "https://www.facebook.com/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Facebook] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None

def youtube(username):
    service_name = "Youtube"
    url = "https://www.youtube.com/user/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Youtube] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None

def medium(username):
    service_name = "Medium"
    url = "https://medium.com/@" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Medium] " + url)
        save(service_name,url)
        return service_name, url
    else:
        return None

def check(username):
    instagram(username)
    github(username)
    twitter(username)
    reddit(username)
    facebook(username)
    youtube(username)
    # print(items)
    return items