import json

def print_text():
    fh = open('political_tweets.json.2018-05-05_filtered','r')
    for line in fh:
        try:
            tweet = json.loads(line)
            print '[' + tweet['location'] + ']: ' + tweet['text']
        except:
            continue

print_text()