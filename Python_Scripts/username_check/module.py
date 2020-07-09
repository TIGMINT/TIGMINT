import requests
def instagram(username):
    service_name = "Instagram"
    url  = "https://instagram.com/" + username
    response = requests.get(url + '/')
    # print(response)
    if (response.status_code == 200 ):
        print("*[INSTAGRAM] " + url)
        return service_name, url



def github(username):
    service_name = "Github"
    url  = "https://github.com/" + username
    response = requests.get(url+'/')
    if(response.status_code == 200):
        print("*[Github] " + url)
        return service_name, url



def twitter(username):
    service_name = "Twitter"
    url = "https://twitter.com/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Twitter] " + url)
        return service_name, url

def reddit(username):
    service_name = "Reddit"
    url = "https://www.reddit.com/user/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Reddit] " + url)
        return service_name, url
    else:
        return None

def facebook(username):
    service_name = "Facebook"
    url = "https://www.facebook.com/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Facebook] " + url)
        return service_name, url
    else:
        return None

def youtube(username):
    service_name = "Youtube"
    url = "https://www.youtube.com/user/" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Youtube] " + url)
        return service_name, url
    else:
        return None

def medium(username):
    service_name = "Medium"
    url = "https://medium.com/@" + username
    response = requests.get(url)
    if(response.status_code == 200):
        print("*[Medium] " + url)
        return service_name, url
    else:
        return None


        