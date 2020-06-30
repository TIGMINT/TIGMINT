import twint
import sys,os


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def get_user_tweets(username,search):
    c.Username = username
    c.Search = search
    c.Pandas = True
    c.Pandas_clean = True
    c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet} | Hashtags: {hashtags} "
    save_result(c,"user_tweets.csv")
    c.Custom["tweet"] = ["id","tweet",]
    twint.run.Search(c)


def get_tweets(search, limit=100):
    c.Search = search
    if limit != 0:
        c.Limit = limit
    c.Pandas = True
    c.Pandas_clean = True
    save_result(c,"tweets.csv")
    c.Custom["tweet"] = ["id","username","tweet"]
    with HiddenPrints():
        print(twint.run.Search(c))
        return twint.output.panda.Tweets_df[["username","tweet"]]

def save_result(c, filename):
    c.Store_csv = True
    c.Output = filename
    return True

def available_columns():
    return twint.output.panda.Tweets_df.columns

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]



if __name__ == "__main__":
    c = twint.Config()
    username = input("enter username")
    string = input("Enter string to be searched or leave blank for all tweets")
    get_user_tweets(username,string)
    # string = input("Enter string to be searched")
    # limit = int(input("Enter limit"))
    # get_tweets(string,limit)
    print(available_columns())
    df_pd = twint_to_pandas(["date", "username", "tweet", "hashtags", "nlikes"])
    print(df_pd)