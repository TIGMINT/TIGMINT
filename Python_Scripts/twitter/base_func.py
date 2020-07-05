import twint
import sys,os
import time
import sentiment_analysis

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def get_user_tweets(c,username,search):
    c.Username = username
    c.Search = search
    c.Pandas = True
    c.Pandas_clean = True
    # c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet} | Hashtags: {hashtags} "
    save_result(c,"user_tweets")
    c.Custom["tweet"] = ["tweet"]
    twets = c.Custom["tweet"]
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    analyse = True
    if analyse == True:
        display_analysis_result(Tweets_df)



def get_tweets(c,search, limit=100):
    c.Search = search
    if limit != 0:
        c.Limit = limit
    c.Pandas = True
    c.Pandas_clean = True
    save_result(c,"tweets")
    c.Custom["tweet"] = ["id","username","tweet"]
    twets = c.Custom["tweet"]
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    # analyse = True
    # if analyse == True:
    #     display_analysis_result(Tweets_df)
    
    # with HiddenPrints():
    #     print(twint.run.Search(c))
    #     return twint.output.panda.Tweets_df[["username","tweet"]]

def get_user_bio(c,username):
    # a = input("Enter username: ")
    c.Username = username
    save_result(c,"user_bio")
    twint.run.Lookup(c)

def get_user_followers(c,username):
    c.Username = username
    save_result(c,"user_followers")
    twint.run.Followers(c)
    
def get_user_following(c,username):
    c,Username = username
    save_result(c,"user_following")
    twint.run.Following(c)

def save_result(c, filename):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    c.Store_csv = True
    c.Output = filename + timestr + ".csv"
    return True

def available_columns():
    return twint.output.panda.Tweets_df.columns

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]

def display_analysis_result(twets_df):
    sentiment_analysis.analysis(twets_df)

# if __name__ == "__main__":
#     c = twint.Config()
#     username = input("enter username")
#     string = input("Enter string to be searched or leave blank for all tweets")
#     get_user_tweets(username,string)
#     # string = input("Enter string to be searched")
#     # limit = int(input("Enter limit"))
#     # get_tweets(string,limit)
#     print(available_columns())
#     df_pd = twint_to_pandas(["date", "username", "tweet", "hashtags", "nlikes"])
#     print(df_pd)