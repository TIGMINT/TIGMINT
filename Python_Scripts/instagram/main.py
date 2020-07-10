import insta_heighlight
import user_info

username = input()

try:
    private = user_info.Username(username)
    if private == False:
        insta_heighlight.main(username)
    else:
        print('Account is private, cannot retrive')
except:
    print("An exception occurred")