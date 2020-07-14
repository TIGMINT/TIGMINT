import insta_heighlight
import user_info
import sys

username = sys.argv[1]

private = user_info.Username(username)
insta_heighlight.main(username)