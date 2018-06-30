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

def filter_table_A(tweetfile):
    #aggregated_data_aggresive=open(tweetfile+'_aggregated_aggressive', 'w+')
    #aggregated_data_non_aggressive=open(tweetfile+'_aggregated_non_aggressive', 'w+')
    filtered_result_aggressive = {}
    filtered_result_non_aggressive = {}
    i = 0
    fh = open(tweetfile,'r')
    for line in fh:
        i +=1
        try:
            tweet = json.loads(line)
            location = tweet['location']
            if ' CA' in location or 'Canda' in location or 'CANDA' in location.lower() or 'toronto' in location.lower():
                location = 'Canda'
            if ' philadelphia' in location.lower() or 'PH' in location or 'philadelphia' in location.lower() or ' PA' in location or 'pennsylvania' in location.lower():
                location = 'Philadelphia'
            if ' TX' in location or 'houston' in location.lower() or 'dallas' in location.lower() or 'austin' in location.lower():
                location = 'TX'
            if 'new orleans' in location.lower() or 'louisiana' in location.lower() or 'New Orleans' in location or 'NEW ORLEANS' in location or 'Pelicans' in location.lower() or 'Smoothie King' in location.lower() or 'baton rouge' in location.lower():
                location = 'Louisiana'
            if ' WV' in location:
                location = 'WV'
            if ' NJ' in location or 'Bronx' in location or 'New York' in location:
                location = 'NJ'
            if ' AL' in location:
                location = 'AL'
            if 'ohio' in location.lower() or ' ohio' in location.lower() or 'OH' in location or 'cleveland' in location.lower() or 'Caves' in location:
                location = 'Ohio'
            if ' utah' in location.lower() or 'utah' in location.lower() or ' UT' in location or 'salt lake' in location.lower() or 'caves' in location.lower() or 'jazz' in location.lower():
                location = 'Utah'
            if ' CO' in location:
                location = 'CO'
            if ' VA' in location:
                location = 'VL'
            if ' FL' in location or ',FL' in location or 'MIAMI' in location:
                location = 'FL'
            if ' UK' in location or 'England' in location:
                location = 'England'
            if 'san francisco' in location.lower() or 'Cali' in location or 'california' in location.lower() or ' ca' in location or ' CA' in location or 'oakland' in location.lower() or 'Golden State Warriors' in location.lower() or 'los angeles' in location.lower() or 'san diego' in location.lower() or 'santa' in location.lower() or ' LA' in location:
                location = 'California'
            if 'boston' in location.lower() or 'massachusetts' in location.lower() or ' ma' in location or ' boston' in location.lower() or ' celtics' in location.lower():
                location = 'Massachusetts'

            if tweet['aggressive'] == 1:
                try:
                    filtered_result_aggressive[location] += 1
                except:
                    filtered_result_aggressive[location] = 1
            else:
                try:
                    filtered_result_non_aggressive[location] += 1 
                except:
                    filtered_result_non_aggressive[location] = 1

        except:
            continue

    
    print('NON - AGGRESSIVE table: ')       
    print "{:<8} {:<15}".format('Key','Label')
    for k, v in filtered_result_non_aggressive.iteritems():
        if k == 'Ohio' or k == 'Canda' or k =='Philadelphia' or k == 'Utah' or k == 'California' or k == 'Massachusetts' or k == 'TX' or k == 'Louisiana':
            print "{:<8} {:<15}".format(k, v)
    
    print('\n')
   
    print('AGGRESSIVE table: ')       
    print "{:<8} {:<15}".format('Key','Label')
    for k, v in filtered_result_aggressive.iteritems():
        if k == 'Ohio' or k == 'Canda' or k =='Philadelphia' or k == 'Utah' or k == 'California' or k == 'Massachusetts' or k == 'TX' or k == 'Louisiana':
            print "{:<8} {:<15}".format(k, v)
    print ('Total tweets are: ', i)

    #json.dump(filtered_result_aggressive, aggregated_data_aggresive)
    #json.dump(filtered_result_non_aggressive, aggregated_data_non_aggressive)
    #aggregated_data_aggresive.close()
    #aggregated_data_non_aggressive.close()

filter_table_A(tweetfile)