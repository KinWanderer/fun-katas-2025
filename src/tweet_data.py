# 1. return empty dictionary 
# 2. return length of tweet 
# 3. return metions and mentions count
# 4. return 
# 5. return 

# 1 
def get_tweet_data(tweet):
   tweet_dictionary = { 
      'tags': [], 
      'mentions': [], 
      'tag_count': 0, 
      'mention_count': 0, 
      'length': 0
      }
   # 2
   tweet_dictionary['length'] = len(tweet)
   # 3
   tweet_dictionary['mentions'] = [word for word in tweet.split() if word.startswith('@')]
   tweet_dictionary['mention_count'] = len(tweet_dictionary['mentions'])
   # 4
   tweet_dictionary['tags'] = [word for word in tweet.split() if word.startswith('#')]  
   tweet_dictionary['tag_count'] = len(tweet_dictionary['tags'])  


   return tweet_dictionary