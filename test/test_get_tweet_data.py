from src.tweet_data import get_tweet_data
# 1 return empty dictionary 
def test_get_empty_dictionary_tweet_data():
    # Assemble
    input_tweet = ''

    # Act
    output = get_tweet_data(input_tweet)

    expected_output = { 
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 0
        }
    
    assert output == expected_output

# 2 return length of tweet
def test_get_my_tweet_length():

    # Assemble
    input_tweet = "My Awesome tweet NOT SWEET"

    # Act
    output = get_tweet_data(input_tweet)

    expected_output = { 
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 26
        }
    
    # Assert
    assert output == expected_output

# 3. return mentions and mentions count in tweet
def test_get_my_tweet_mentions_count_length():

    # Assemble 
    input_tweet = "My Awesome tweet NOT SWEET @QualityStreet"

    # Act
    output = get_tweet_data(input_tweet)

    expected_output = {
        'tags': [], 
        'mentions': ['@QualityStreet'], 
        'tag_count': 0, 
        'mention_count': 1, 
        'length': 41
        }
    
    # Assert
    assert output == expected_output

# 4. tweet about coding tweetfails 

def test_get_my_tweet_tag_count_length():

    # Assemble
    input_tweet = "Rememeber rememeber to read read and type accurately #codingfails"

    # Act
    output = get_tweet_data(input_tweet)

    expected_output = {
        'tags': ['#codingfails'], 
        'mentions': [], 
        'tag_count': 1, 
        'mention_count': 0, 
        'length': 65
        }
    
    # Assert
    assert output == expected_output