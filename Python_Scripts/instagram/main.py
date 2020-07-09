import insta_heighlight
import user_info

username = input()

private = user_info.Username(username)
if private == False:
    insta_heighlight.main()