import Python_Scripts.instagram.insta_heighlight as insta_heighlight
import Python_Scripts.instagram.user_info as user_info

username = input()

private = user_info.Username(username)
if private == False:
    insta_heighlight.main()