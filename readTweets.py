
#Prints basic information about tweets in console
#Usage:
## prints text of first 10 tweets
#python print-tweets.py -o text -f tweets.json -k 10  
## prints coordinates and text of first 10 geolocated tweets
#python print-tweets.py -o geo -f tweets.json -k 10 


import sys
import json
import argparse

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True,
    help = 'name of file with tweets in json format')
parser.add_argument('-o', '--output', default='text',
    help = 'type of output to be printed in console', choices=['text', 'geo', 'loc', 'filter'])
parser.add_argument('-k', '--count', default=20, type=int,
    help = 'number of results to display in console')
args = parser.parse_args()

output = args.output
tweetfile = args.file
k = args.count

def print_text(tweetfile, k):
    i = 1
    fh = open(tweetfile,'r')
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        if 'text' not in tweet:
            continue
        print '[' + tweet['user']['screen_name'] + ']: ' + tweet['text']
        i += 1
        if i == k:
            break

def print_geo(tweetfile, k):
    i = 1
    fh = open(tweetfile,'r')
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        try:
            coord = tweet['geo']['coordinates']
        except:
            continue
        print '[' + str(coord[0]) + ',' + str(coord[1]) + ']: ' + tweet['text']
        i += 1
        if i == k:
            break

def print_loc(tweetfile, k):
    i = 1
    fh = open(tweetfile,'r')
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        try:
            location = tweet['user']['location']
	    if str(location) != 'None':
		    print '[' + str(location) + ']: ' + tweet['text']
        except:
            continue
        i += 1
        if i == k:
            break


def filter_data(tweetfile):
    filtered_data=open(tweetfile+'_filtered', 'w+')

    result_tweet = {}
    location = 0
    zeros = 0
    ones = 0
    skipped = 0
    i = 1
    fh = open(tweetfile,'r')
    # print len(fh) + ' total lines'
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        try:
            underlinedTweet = tweet['text'].lower()
            if underlinedTweet.find('work') > -1 or underlinedTweet.find('job') > -1 or underlinedTweet.find('hiring') > -1:
                raise RuntimeError('work advertisment')
       	    coord = tweet['geo']['coordinates']
            location = 1
            result_tweet['location'] = coord
        except RuntimeError:
            # print 'skip work advertisment tweet'
            skipped += 1
            continue
        except:
            # print 'dif exception'
            try:
                loc = tweet['user']['location']
                if str(loc) != 'None': 
                    location = 1
                    result_tweet['location'] = loc
            except:
                print 'no location'
        finally:
            try:
                result_tweet['text'] = tweet['extended_tweet']['full_text']
            except:
                result_tweet['text'] = tweet['text']
            if location == 1:
                # print '[' + str(result_tweet['our_location']) + ']' + result_tweet['text']
                json.dump(result_tweet, filtered_data)
                filtered_data.write('\n')
                ones += 1
            else:
                # print result_tweet['text']
                zeros += 1
        location = 0
        i += 1
        if i % 1000 == 0:
            print i
    print 'with location ' + str(ones)
    print 'without location ' + str(zeros)
    print 'skipped tweets ' + str(skipped)
    filtered_data.close()


if output == 'text':
    print_text(tweetfile, k)

if output == 'geo':
    print_geo(tweetfile, k)

if output == 'loc':
    print_loc(tweetfile, k)

if output == 'filter':
    filter_data(tweetfile)
