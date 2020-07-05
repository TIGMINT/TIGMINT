import base_func as base
import twint
from similar_hashtags import similar_hashtags 
from top_mentions_hashtags import top_mentions_hashtags as mentions

if __name__ == "__main__":
    c = twint.Config()
    username = input("enter username")
    string = input("Enter string to be searched or leave blank for all tweets")
    analysis = input('Enter yes/no for analysis of tweets ')
    if analysis == 'yes':
        analysis = True
    elif analysis == 'no':
        analysis = False
    else:
        print(NameError)
        exit()
    base.get_user_tweets(c,username,string,analysis)
