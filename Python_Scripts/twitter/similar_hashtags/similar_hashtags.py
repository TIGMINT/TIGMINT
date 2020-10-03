import twint
import heapq
import matplotlib.pyplot as plt
import os
import sys

def get_similar_hashtags(seed_hashtag, limit=500):
  os.chdir("Python_Scripts")
  currentDir = os.getcwd() + "/result/twitter/"

  try:
    os.mkdir(currentDir)
  except:
    pass
  os.chdir(currentDir)
  c = twint.Config()
  c.Hide_output = True  # hides command line verbose output
  c.Limit = 100  # maximum number of tweets to pull
  c.Store_object = True
  c.Store_csv = True
  c.Output = f"twitter-hashtag_{seed_hashtag[1::]}-tweets.csv"
  c.Search = seed_hashtag
  twint.run.Search(c)
  tweets = twint.output.tweets_list
  # counts occurrence of hashtags in the tweets
  hashtags_dict = {}
  for tweet in tweets:
    for hashtag in tweet.hashtags:
      if hashtag in hashtags_dict:
        hashtags_dict[hashtag] += 1
      else:
        hashtags_dict[hashtag] = 1
  # del hashtags_dict[seed_hashtag] #gets rid of seed hashta
  top_hashtags = heapq.nlargest(10, hashtags_dict, key=hashtags_dict.get)  # gets highest hashtags

  # makes dictionary of just highest ones
  hashtags_ranked = {}
  for hashtag in top_hashtags:
    hashtags_ranked[hashtag] = hashtags_dict[hashtag]
  plt.barh(range(len(hashtags_ranked)), list(hashtags_ranked.values()), align='center', color='maroon')
  plt.yticks(range(len(hashtags_ranked)), list(hashtags_ranked.keys()))
  plt.gca().invert_yaxis()  # just to have the highest bar at the top
  plt.title("Most Related Hashtags to " + seed_hashtag)
  os.chdir(currentDir)
  seed_hashtag = seed_hashtag.replace("#", "")
  plt.savefig('twitter-hashtag_'+seed_hashtag + '.png', bbox_inches='tight') # saves the visualization as png
  
  plt.close()
  twint.output.tweets_list = []

def main():
  limit = 500  # limits the number of tweets to pull
  inputHashtag = sys.argv[1]
  get_similar_hashtags(inputHashtag)

if __name__ == "__main__":
	main()

