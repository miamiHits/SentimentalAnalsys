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

    train = [
        ('Anger', 'pos'),
        ('abuse', 'pos'),
        ('abusive', 'pos'),
        ('aggravat', 'pos'),
        ('aggress', 'pos'),
        ('agitat', 'pos'),
        ('anger', 'pos'),
        ('angr', 'pos'),
        ('annoy', 'pos'),
        ('antagoni', 'pos'),
        ('argu', 'pos'),
        ('arrogan', 'pos'),
        ('assault', 'pos'),
        ('bastard', 'pos'),
        ('beaten', 'pos'),
        ('bitch', 'pos'),
        ('bitter', 'pos'),
        ('blam', 'pos'),
        ('cheat', 'pos'),
        ('contradic', 'pos'),
        ('crap', 'pos'),
        ('critical', 'pos'),
        ('critici', 'pos'),
        ('cruel', 'pos'),
        ('cut', 'pos'),
        ('cynical', 'pos'),
        ('damn', 'pos'),
        ('danger', 'pos'),
        ('defens', 'pos'),
        ('despis', 'pos'),
        ('destroy', 'pos'),
        ('destruct', 'pos'),
        ('disgust', 'pos'),
        ('distrust', 'pos'),
        ('dominate', 'pos'),
        ('dread', 'pos'),
        ('dumb', 'pos'),
        ('dump', 'pos'),
        ('enem', 'pos'),
        ('enrag', 'pos'),
        ('evil', 'pos'),
        ('feud', 'pos'),
        ('fight', 'pos'),
        ('fighting', 'pos'),
        ('fights', 'pos'),
        ('fought', 'pos'),
        ('frustrat', 'pos'),
        ('fuck', 'pos'),
        ('furious', 'pos'),
        ('goddam', 'pos'),
        ('greed', 'pos'),
        ('harass', 'pos'),
        ('hate', 'pos'),
        ('hated', 'pos'),
        ('hateful', 'pos'),
        ('hates', 'pos'),
        ('hating', 'pos'),
        ('hatred', 'pos'),
        ('hostil', 'pos'),
        ('humiliat', 'pos'),
        ('insult', 'pos'),
        ('interrup', 'pos'),
        ('intimidat', 'pos'),
        ('jealous', 'pos'),
        ('jerk', 'pos'),
        ('jerked', 'pos'),
        ('jerks', 'pos'),
        ('kill', 'pos'),
        ('liar', 'pos'),
        ('lied', 'pos'),
        ('lous', 'pos'),
        ('ludicrous', 'pos'),
        ('mad', 'pos'),
        ('molest', 'pos'),
        ('nag', 'pos'),
        ('nast', 'pos'),
        ('obnoxious', 'pos'),
        ('offend', 'pos'),
        ('outrag', 'pos'),
        ('paranoi', 'pos'),
        ('piss', 'pos'),
        ('poison', 'pos'),
        ('prejudic', 'pos'),
        ('punish', 'pos'),
        ('rage', 'pos'),
        ('rape', 'pos'),
        ('rebel', 'pos'),
        ('resent', 'pos'),
        ('revenge', 'pos'),
        ('ridicul', 'pos'),
        ('rude', 'pos'),
        ('sarcas', 'pos'),
        ('screw', 'pos'),
        ('shit', 'pos'),
        ('sinister', 'pos'),
        ('skeptical', 'pos'),
        ('smother', 'pos'),
        ('snob', 'pos'),
        ('spite', 'pos'),
        ('stubborn', 'pos'),
        ('stupid', 'pos'),
        ('suck', 'pos'),
        ('sucked', 'pos'),
        ('sucking', 'pos'),
        ('sucks', 'pos'),
        ('suspicious', 'pos'),
        ('teas', 'pos'),
        ('temper', 'pos'),
        ('terrified', 'pos'),
        ('terrifying', 'pos'),
        ('terror', 'pos'),
        ('threaten', 'pos'),
        ('tick', 'pos'),
        ('ticked', 'pos'),
        ('torture', 'pos'),
        ('trick', 'pos'),
        ('ugly', 'pos'),
        ('vicious', 'pos'),
        ('victim', 'pos'),
        ('violent', 'pos'),
        ('wicked', 'pos')

        ]

    test = [
        ('I do enjoy my job', 'neg'),
        ("I feeling good today.", 'neg'),
        ("I feel amazing!", 'neg'),
        ('Gary is a friend of mine.', 'neg'),
        ("I believe I'm doing this.", 'neg')
        ]

    cl = NaiveBayesClassifier(train)

    print(cl.classify("blam"))
    print(cl.accuracy(test))
    #cl.show_informative_features(5)
    # features = end_word_extractor("abuse happy")
    # assert features == {'last(happy)': False, 'first(abuse)': True}

    cl2 = NaiveBayesClassifier(train, feature_extractor=end_word_extractor)
    blob = TextBlob("I'm amazing to try my new classifier.", classifier=cl2)
    print(blob.classify())

    tag("While you are drinking your coffee this morning this is a good blueprint for what you")
    print(get_tweet_sentiment("rude"))
    


if __name__ == "__main__":
# calling main function
    main()