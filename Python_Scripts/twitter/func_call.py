import sys
import Python_Scripts.twitter.base_func as base
import twint
from similar_hashtags import similar_hashtags 
from top_mentions_hashtags import top_mentions_hashtags as mentions

def basic(c,username,search):
    base.get_user_bio(c,username,search)

def get_keyword(c,key,limit=100):
    base.get_tweets(c,key,limit)

def top_mention():
    key_val = int(input('no of users'))
    seed_user = list(map(str,input('Enter usernames').strip().split()))[:key_val]
    limit = int(input('No of tweets to be pulled'))     # default limit = 500
    for username in seed_user:
        mentions.get_top_mentions_hashtags(username)

def similar_hashtag():
    key_val = int(input('no of hastags'))
    seed_hash = list(map(str,input('Enter hashtags').strip().split()))[:key_val]
    limit = int(input('No of tweets to be pulled'))     # default limit = 500
    for seed_hashtag in seed_hash:
       similar_hashtags.get_similar_hashtags(seed_hashtag, limit)


if __name__ == "__main__":
    c = twint.Config()
    username = input("enter username")
    string = input("Enter string to be searched or leave blank for all tweets")
    # analysis = input('Enter yes/no for analysis of tweets ')
    # if analysis == 'yes':
    #     analysis = True
    # elif analysis == 'no':
    #     analysis = False
    # else:
    #     print(NameError)
    #     exit()
    # # calling = input()
    # basic(c,username,string)
    # get_keyword(c,string,limit=100)
