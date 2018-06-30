from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import pprint

tokenizer = None
tagger = None

def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    print (tokenized)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged

def end_word_extractor(document):
    tokens = document.split()
    first_word, last_word = tokens[0], tokens[-1]
    feats = {}
    feats["first({0})".format(first_word)] = True
    feats["last({0})".format(last_word)] = False
    return feats
 

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
 
 
def main():
    print(get_tweet_sentiment("Turnt up like who want it We pulled up on that dumb shit flexing on these niggas pockets full of blue hunnids niggas telling lies so i got to be honest ask me for to tell it You know that imma run shit"))
    


if __name__ == "__main__":
# calling main function
    main()