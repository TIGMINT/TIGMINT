import twint
import heapq
import matplotlib.pyplot as plt

""" This script is used to generate top 10 mentions and hashtags for a particular username."""
def get_top_mentions_hashtags(username, limit):
    twint.output.tweets_list = []
    c = twint.Config()
    c.Username = username
    c.Hide_output = True  # hides command line verbose output
    c.Limit = limit  # maximum number of tweets to pull
    c.Store_object = True
    twint.run.Search(c)
    tweets = twint.output.tweets_list
    mentions_dict = {}
    hashtags_dict = {}
    for tweet in tweets:
        for mention in tweet.mentions:
            if mention in mentions_dict:
                mentions_dict[mention] += 1
            else:
                mentions_dict[mention] = 1
        for hashtag in tweet.hashtags:
            if hashtag in hashtags_dict:
                hashtags_dict[hashtag] += 1
            else:
                hashtags_dict[hashtag] = 1
    top_mentions = heapq.nlargest(10, mentions_dict, key=mentions_dict.get)  # gets highest mentions
    top_hashtags = heapq.nlargest(10, hashtags_dict, key=hashtags_dict.get)  # gets highest hashtags

    # makes dictionary of just highest ones
    mentions_ranked = {}
    hashtags_ranked = {}
    for mention in top_mentions:
        mentions_ranked[mention] = mentions_dict[mention]
    for hashtag in top_hashtags:
        hashtags_ranked[hashtag] = hashtags_dict[hashtag]
    plt.barh(range(len(mentions_ranked)), list(mentions_ranked.values()), align='center', color='maroon')
    plt.yticks(range(len(mentions_ranked)), list(mentions_ranked.keys()))
    plt.gca().invert_yaxis()  # just to have the highest bar at the top
    plt.title("Most Mentions of username: " + username)
    plt.savefig(username + '-mentions.png', bbox_inches='tight')  # saves the visualization as png
    # plt.savefig(seed_hashtag + '.pdf', bbox_inches='tight')
    plt.show()
    plt.close()
    plt.barh(range(len(hashtags_ranked)), list(hashtags_ranked.values()), align='center', color='maroon')
    plt.yticks(range(len(hashtags_ranked)), list(hashtags_ranked.keys()))
    plt.gca().invert_yaxis()  # just to have the highest bar at the top
    plt.title("Top 10 Hashtags of " + username)
    plt.savefig(username + '-hashtags.png', bbox_inches='tight')  # saves the visualization as png
    # plt.savefig(seed_hashtag + '.pdf', bbox_inches='tight')
    plt.show()
    plt.close()

    print("List of Top 10 mentions by " + username + " :")
    print(top_mentions)  # displays the top 10 hashtags as a list.
    print("List of Top 10 hashtags hashtags by " + username + " :")
    print(top_hashtags)  # displays the top 15 hashtags as a list.


def main():
    seed_usernames = ["kiranbabumuddam", "iamvkohli", "twitter"]
    limit = 500  # limits the number of tweets to pull
    for username in seed_usernames:
        get_top_mentions_hashtags(username, limit)

main()