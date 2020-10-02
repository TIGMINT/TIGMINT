import sys
import base_func as base
import twint
from similar_hashtags import similar_hashtags 
from top_mentions_hashtags import top_mentions_hashtags as mentions

def basic(username,search):
    base.get_user_bio(username,search)
    base.get_user_tweets(username,search,True)

def get_keyword(key,limit=100):
    base.get_tweets(key,limit)

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
    username = sys.argv[1]
    string = sys.argv[2]
    basic(username,string)