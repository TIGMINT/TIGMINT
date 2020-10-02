import twint
import sys,os
import time
import sentiment_analysis


def get_user_tweets(username,search,analyse):
    c = twint.Config()    
    c.Username = username
    c.Search = search
    c.Limit = 100
    c.Pandas = True
    c.Pandas_clean = True
    # c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet} | Hashtags: {hashtags} "
    save_result(c,username+"_tweets")
    c.Custom["tweet"] = ["tweet"]
    twets = c.Custom["tweet"]
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    # analyse = True
    if analyse == True:
        display_analysis_result(Tweets_df,username)



def get_tweets(key, limit=100):
    c = twint.Config()
    c.Search = key
    if limit != 0:
        c.Limit = limit
    c.Pandas = True
    c.Pandas_clean = True
    save_result(c,key + "_tweets")
    c.Custom["tweet"] = ["id","username","tweet"]
    twets = c.Custom["tweet"]
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    analyse = True
    if analyse == True:
        display_analysis_result(Tweets_df,key)
    
    

def get_user_bio(username,search):
    c = twint.Config()
    c.Username = username
    save_result(c,username + "_user_bio")
    twint.run.Lookup(c)
    # get_user_followers(username,search)
    get_user_tweets(username,search,True)

# sentiment_analysis
# word cloud
def get_user_followers(username,search):
    c = twint.Config()
    c.Username = username
    save_result(c,username + "user_followers")
    twint.run.Followers(c)
    get_user_following(username,search)
    
def get_user_following(username,search):
    c = twint.Config()
    c.Username = username
    save_result(c,username + "user_following")
    twint.run.Following(c)
    get_user_tweets(username,search,True)

def save_result(c, filename):

    c.Store_csv = True
    try:
        os.mkdir(os.getcwd()+'/Python_Scripts/result/twitterUser/')
    except:
        pass
    c.Output = os.getcwd()+'/Python_Scripts/result/twitterUser/'+ filename + ".csv"
    return True

def available_columns():
    return twint.output.panda.Tweets_df.columns

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]

def display_analysis_result(twets_df,username):
    sentiment_analysis.analysis(twets_df,username)
