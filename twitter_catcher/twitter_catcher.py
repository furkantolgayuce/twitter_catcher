#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 2019

@author: Furkan Tolga Yüce
"""

# Kütüphaneler
import tweepy
import pandas as pd
import sqlite3 as sql #sql

class twitter_catcher:
    def __init__(self):
        pass
    def login(self):
        # Read File Keys and Tokens
        with open("key_token.txt") as f: 
            liste = [line for line in f]
            consumer_key = liste[0][:-1]
            consumer_secret = liste[1][:-1]
            access_token = liste[2][:-1]
            access_token_secret = liste[3][:-1]
        # Login
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    def search(self,api,search_key,max_tweets = 200):
        # Max tweets
        return [status for status in tweepy.Cursor(api.search,
                                                       q=search_key,
                                                       lang = "tr",
                                                       result_type = "recent",
                                                       tweet_mode='extended').items(max_tweets)], search_key
    

    def dataframe(self,search_all):
        tweetler,search_key = search_all[0],search_all[1]
        id_list = [tweet.id for tweet  in tweetler]
        df = pd.DataFrame(id_list, columns = ["id"])
        
        #df["text"] = [tweet.full_text for tweet in tweetler]
        df["text"] = [i.retweeted_status.full_text if ("retweeted_status" in dir(i)) else i.full_text for i in tweetler]
        df["truncated"] = [tweet.truncated for tweet in tweetler]
        df["rt_text"] = [1 if ("retweeted_status" in dir(i)) else 0 for i in tweetler]
        df["created_at"] = [tweet.created_at for tweet in tweetler]
        df["retweeted"] = [tweet.retweeted for tweet in tweetler]
        df["retweet_count"] = [tweet.retweet_count for tweet in tweetler]
        df["favorite_count"] = [tweet.favorite_count for tweet in tweetler]
        df["user_id"] = [tweet.user.id for tweet in tweetler]
        df["rt_text_id"] = [i.retweeted_status.id if ("retweeted_status" in dir(i)) else 0 for i in tweetler]
        df["rt_text_userid"] = [i.retweeted_status.user.id if ("retweeted_status" in dir(i)) else 0 for i in tweetler]
        df["user_screen_name"] = [tweet.author.screen_name for tweet in tweetler]    
        df["user_followers_count"] = [tweet.author.followers_count for tweet in tweetler]
        df["user_verified"] = [tweet.user.verified for tweet in tweetler]
        df["user_location"] = [tweet.author.location for tweet in tweetler]
        df["Hashtags"] = [tweet.entities.get('hashtags') for tweet in tweetler]
        df["search_key"] = [search_key for tweet in tweetler]
        
        return df
    
    def to_sql(self,df):
        # Tarih Al
        from datetime import datetime
        an = datetime.now()
        tarih = datetime.strftime(an, '%Y-%U')
        
        df = df.astype('str')
        
        conn = sql.connect((tarih+".db"))
        
        df.to_sql(name = df["search_key"][0],
          con = conn,
          if_exists = "append",
          index = False)
    def to_excel(self,df):        
        df = df.astype('str')
        name = df["search_key"][0] +".xlsx"
        df.to_excel(name)
