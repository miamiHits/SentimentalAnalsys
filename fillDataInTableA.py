from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import pprint
 
import sys
import json
import argparse

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True,
    help = 'name of file with tweets in json format')
args = parser.parse_args()

tweetfile = args.file

aggressiveDictionary = [
        ('Anger' ),
        ('abuse' ),
        ('abusive' ),
        ('aggravat' ),
        ('aggress' ),
        ('agitat' ),
        ('anger' ),
        ('angr' ),
        ('annoy' ),
        ('antagoni' ),
        ('argu' ),
        ('arrogan' ),
        ('assault' ),
        ('bastard' ),
        ('beaten' ),
        ('bitch' ),
        ('bitter' ),
        ('blam' ),
        ('cheat' ),
        ('contradic' ),
        ('crap' ),
        ('critical' ),
        ('critici' ),
        ('cruel' ),
        ('cut' ),
        ('cynical' ),
        ('damn' ),
        ('danger' ),
        ('defens' ),
        ('despis' ),
        ('destroy' ),
        ('destruct' ),
        ('disgust' ),
        ('distrust' ),
        ('dominate' ),
        ('dread' ),
        ('dumb' ),
        ('dump' ),
        ('enem' ),
        ('enrag' ),
        ('evil' ),
        ('feud' ),
        ('fight' ),
        ('fighting' ),
        ('fights' ),
        ('fought' ),
        ('frustrat' ),
        ('fuck' ),
        ('furious' ),
        ('goddam' ),
        ('greed' ),
        ('harass' ),
        ('hate' ),
        ('hated' ),
        ('hateful' ),
        ('hates' ),
        ('hating' ),
        ('hatred' ),
        ('hostil' ),
        ('humiliat' ),
        ('insult' ),
        ('interrup' ),
        ('intimidat' ),
        ('jealous' ),
        ('jerk' ),
        ('jerked' ),
        ('jerks' ),
        ('kill' ),
        ('liar' ),
        ('lied' ),
        ('lous' ),
        ('ludicrous' ),
        ('mad' ),
        ('molest' ),
        ('nag' ),
        ('nast' ),
        ('obnoxious' ),
        ('offend' ),
        ('outrag' ),
        ('paranoi' ),
        ('piss' ),
        ('poison' ),
        ('prejudic' ),
        ('punish' ),
        ('rage' ),
        ('rape' ),
        ('rebel' ),
        ('resent' ),
        ('revenge' ),
        ('ridicul' ),
        ('rude' ),
        ('sarcas' ),
        ('screw' ),
        ('shit' ),
        ('sinister' ),
        ('skeptical' ),
        ('smother' ),
        ('snob' ),
        ('spite' ),
        ('stubborn' ),
        ('stupid' ),
        ('suck' ),
        ('sucked' ),
        ('sucking' ),
        ('sucks' ),
        ('suspicious' ),
        ('teas' ),
        ('temper' ),
        ('terrified' ),
        ('terrifying' ),
        ('terror' ),
        ('threaten' ),
        ('tick' ),
        ('ticked' ),
        ('torture' ),
        ('trick' ),
        ('ugly' ),
        ('vicious' ),
        ('victim' ),
        ('violent' ),
        ('wicked' )
    ]
def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def filter_data(tweetfile):
    filtered_data=open(tweetfile+'__withAgressionMapping', 'w+')
    result_tweet = {}
    fh = open(tweetfile,'r')
    # print len(fh) + ' total lines'
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        try:
            flag = 0 
            res = 0 
            text = tweet['text'].lower()
            
            if any(ext in text for ext in aggressiveDictionary):
                    res = 1
                    flag = 1
            if flag == 0 :
                if get_tweet_sentiment(text) == 'negative':
                    res = 1 
                else:
                    res = 0 
            print('res is: ', res)
            result_tweet['text'] = tweet['text']
            result_tweet['aggressive'] = res  
            result_tweet['location'] = tweet['location']
            filtered_data.write('\n')

            json.dump(result_tweet, filtered_data)
        except:
            continue

    filtered_data.close()

filter_data(tweetfile)