#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tweepy
import csv


# In[11]:


c_key="kqEGmgAt3WNava7BNq9loZNNX"
c_sec="dcELgyinahrFM3GE6HPk1VcTT99GAOzN6HZQGA1apJ1kj4BmjW"
a_key="276375321-YX0Au6SyRczoe2tiOjchRbhANOMs1bjAsMOr1nmW"
a_sec="xEoT9B36t9XA8pidcUrGELidVC8VBsewjRN0m8CMJAlq3"


# In[12]:


auth=tweepy.OAuthHandler(c_key,c_sec)
auth.set_access_token(a_key,a_sec)
api=tweepy.API(auth)


# In[13]:


x=5 #no of tweets to be extracted
keyword="cwc"
csvFile = open('cw.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


# In[ ]:


for tweet in tweepy.Cursor(api.search,q=keyword,count=50,lang="en",since="2019-06-14").items():
    print (tweet.created_at, tweet.text)
csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


# In[ ]:




