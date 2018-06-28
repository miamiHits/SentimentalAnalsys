import json

def filter_table_A():
    aggregated_data_aggresive=open('political_tweets.json.2018-05-05_filtered'+'_aggregated_aggressive', 'w+')
    aggregated_data_non_aggressive=open('political_tweets.json.2018-05-05_filtered'+'_aggregated_non_aggressive', 'w+')
    filtered_result_aggressive = {}
    filtered_result_non_aggressive = {}
 
    fh = open('political_tweets.json.2018-05-05_filtered','r')
    for line in fh:
        try:
            tweet = json.loads(line)
            location = tweet['location']
            if tweet['aggressive'] == 1:
                try:
                    filtered_result_aggressive[location] += filtered_result_aggressive[location]
                except:
                    filtered_result_aggressive[location] = 1
            else:
                try:
                    filtered_result_non_aggressive[location] += filtered_result_non_aggressive[location]
                except:
                    filtered_result_non_aggressive[location] = 1
        except:
            continue

    json.dump(filtered_result_aggressive, aggregated_data_aggresive)
    json.dump(filtered_result_non_aggressive, aggregated_data_non_aggressive)
    aggregated_data_aggresive.close()
    aggregated_data_non_aggressive.close()

filter_table_A()