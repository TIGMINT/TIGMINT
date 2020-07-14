import twint
import heapq
import matplotlib.pyplot as plt
import os

def get_similar_hashtags(seed_hashtag, limit=500):
  c = twint.Config()
  c.Hide_output = True  # hides command line verbose output
  c.Limit = limit  # maximum number of tweets to pull
  c.Store_object = True
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
  os.chdir('Python_Scripts')
  currentDirectory = os.getcwd()
  if not os.path.exists('result'):
        os.makedirs('result')
  os.chdir(currentDirectory + '/result/twitter/')

  plt.savefig(os.getcwd() + 'twitter_'+seed_hashtag + '.png', bbox_inches='tight') # saves the visualization as png
  #plt.savefig(seed_hashtag + '.pdf', bbox_inches='tight')
  # plt.show()
  #print("List of most related hashtags to "+ seed_hashtag + " :")
  #print(top_hashtags) # displays the top 15 hashtags as a list.
  plt.close()
  twint.output.tweets_list = []

# def main():
#   seed_hashtags =["#tiktok", "#blacklivesmatter", "#google", "#covid19", "#carryminati"]
#   limit = 500  # limits the number of tweets to pull
  # for seed_hashtag in seed_hashtags:
  #   get_similar_hashtags(seed_hashtag, limit)
# main()
