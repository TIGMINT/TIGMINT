import base_func as base
import twint


if __name__ == "__main__":
    c = twint.Config()
    username = input("enter username")
    string = input("Enter string to be searched or leave blank for all tweets")
    base.get_user_tweets(c,username,string)