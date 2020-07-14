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

def get_user_tweets(username,search,analyse):
    c = twint.Config()    
    c.Username = username
    c.Search = search
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
    
    # with HiddenPrints():
    #     print(twint.run.Search(c))
    #     return twint.output.panda.Tweets_df[["username","tweet"]]

def get_user_bio(username,search):
    c = twint.Config()
    # a = input("Enter username: ")
    c.Username = username
    save_result(c,username + "_user_bio")
    twint.run.Lookup(c)
    # df = pd.read_csv (r'user_bio')
    # get_user_followers(username,search)
    get_user_tweets(username,search,True)

sentiment_analysis
word cloud
def get_user_followers(username,search):
    c = twint.Config()
    c.Username = username
    save_result(c,username + "user_followers")
    twint.run.Followers(c)
    # save_result(c,username + "user_followers")
    get_user_following(username,search)
    
def get_user_following(username,search):
    c = twint.Config()
    c.Username = username
    save_result(c,username + "user_following")
    twint.run.Following(c)
    get_user_tweets(username,search,True)

def save_result(c, filename):
    # timestr = time.strftime("%Y%m%d-%H%M%S")
    
    os.chdir('Python_Scripts')
    retval = os.getcwd()
    if not os.path.exists('result'):
        os.makedirs('result')
    os.chdir(retval + '/result/twitterUser/')

    c.Store_csv = True
    # 
    c.Output = os.getcwd()+ filename + ".csv"
    return True

def available_columns():
    return twint.output.panda.Tweets_df.columns

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]

def display_analysis_result(twets_df,username):
    sentiment_analysis.analysis(twets_df,username)

# if __name__ == "__main__":
#     c = twint.Config()
#     get_user_tweets(c,'kaustubhsh_','',False)
