#!/usr/bin/python3
import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import string
import os
import warnings 
# from nltk.stem.porter import *
from wordcloud import WordCloud
from textblob import TextBlob
from wordcloud import WordCloud
plt.style.use('fivethirtyeight')
warnings.filterwarnings("ignore", category=DeprecationWarning)

# def remove_pattern(input_txt, pattern):
#     r = re.findall(pattern, input_txt)
#     for i in r:
#         input_txt = re.sub(i, '', input_txt)
        
#     return input_txt
def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
    return text

# Create a function to get the subjectivity
def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
  return  TextBlob(text).sentiment.polarity


def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


def analysis(tweets_df,username):
    # train  = pd.read_csv('user_tweets.csv')   # training on the data 
    # test = pd.read_csv('test_data.csv')

    # combi = train.append(test, ignore_index=True)
    combi = tweets_df 
    combi['tweet'] = combi['tweet'].apply(cleanTxt)
    # Create two new columns 'Subjectivity' & 'Polarity'
    combi['Subjectivity'] = combi['tweet'].apply(getSubjectivity)
    combi['Polarity'] = combi['tweet'].apply(getPolarity)
    # Show the new dataframe with columns 'Subjectivity' & 'Polarity'
    combi['Analysis'] = combi['Polarity'].apply(getAnalysis)
    print_values(combi,username)
    print_wordcloud(combi,username)
    # print_values(combi,username)
    plotting(combi,username)

def print_wordcloud(combi,username):
    # Creation of wordcloud
    allWords = ' '.join([twts for twts in combi['tweet']])
    wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(allWords)


    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis('off')
    # plt.show()
    # os.chdir(os.getcwd()+'/Python_Scripts')
    currentDirectory = os.getcwd()
    # if not os.path.exists('result'):
    #     os.makedirs('result')
    # os.chdir(currentDirectory + '/result/twitterUser/')
    # os.chdir(currentDirectory + '/Python_Scripts/result/twitterUser/')

    plt.savefig(os.getcwd()+'/Python_Scripts/result/twitterUser/'+'wordcloud_' + username + '.png', bbox_inches='tight')
    plt.close()
    
# Show the dataframe
#print(combi)
def print_positive_tweets(combi):
    print('Printing positive tweets:\n')
    j=1
    sortedDF = combi.sort_values(by=['Polarity']) #Sort the tweets
    for i in range(0, sortedDF.shape[0] ):
        if( sortedDF['Analysis'][i] == 'Positive'):
            print(str(j) + ') '+ sortedDF['tweet'][i])
            print()
            j= j+1


def print_negative_tweets(combi):
    print('Printing negative tweets:\n')
    j=1
    sortedDF = combi.sort_values(by=['Polarity'],ascending=False) #Sort the tweets
    for i in range(0, sortedDF.shape[0] ):
        if( sortedDF['Analysis'][i] == 'Negative'):
            print(str(j) + ') '+sortedDF['tweet'][i])
            print()
            j=j+1


# Plotting 
def plotting(combi,username):
    df = combi
    plt.figure(figsize=(8,6)) 
    for i in range(0, df.shape[0]):
        plt.scatter(df["Polarity"][i], df["Subjectivity"][i], color='Blue') 
    # plt.scatter(x,y,color)   
    plt.title('Sentiment Analysis') 
    plt.xlabel('Polarity') 
    plt.ylabel('Subjectivity') 
    # plt.show()
    # os.chdir(os.getcwd()+'/Python_Scripts')
    currentDirectory = os.getcwd()
    # if not os.path.exists('result'):
    #     os.makedirs('result')
    # os.chdir(currentDirectory + '/result/twitterUser/')
    # os.chdir(currentDirectory + '/Python_Scripts/result/twitterUser/')
    plt.savefig(os.getcwd()+'/Python_Scripts/result/twitterUser/'+'tweet_analysis_' + username + '.png', bbox_inches='tight')


def print_values(combi,username):
    df = combi
    # Print the percentage of positive tweets
    ptweets = df[df.Analysis == 'Positive']
    ptweets = ptweets['tweet']
    # ptweets
    round( (ptweets.shape[0] / df.shape[0]) * 100 , 1)

    ntweets = df[df.Analysis == 'Negative']
    ntweets = ntweets['tweet']
    # print(ntweets)

    round( (ntweets.shape[0] / df.shape[0]) * 100, 1)
    # Show the value counts
    # print(df['Analysis'].value_counts())
    # Plotting and visualizing the counts
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Counts')
    df['Analysis'].value_counts().plot(kind = 'bar')
    # plt.show()
    try:
        os.mkdir(os.getcwd()+'/Python_Scripts/result/twitterUser/')
    except:
        pass
    plt.savefig(os.getcwd()+'/Python_Scripts/result/twitterUser/'+'sentiments_plot_' + username + '.png', bbox_inches='tight')
    plt.close()