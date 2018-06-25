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
        ('I do not like this restaurant', 'pos'),
        ('I am tired of this stuff.', 'pos'),
        ("I can't deal with this", 'pos'),
        ('he is my sworn enemy!', 'pos'),
        ('my boss is horrible.', 'pos'),
        ('I do enjoy my job', 'neg'),
        ("I feeling good today.", 'neg'),
        ("I feel amazing!", 'neg'),
        ('Gary is a friend of mine.', 'neg'),
        ("I believe I'm doing this.", 'neg')
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

    print(tag("While you are drinking your coffee this morning this is a good blueprint for what you"))
if __name__ == "__main__":
# calling main function
    main()