from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import pprint

 
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
        ('wicked', 'pos'),
        ('enjoy', 'neg'),
        ('accepting', 'neg'),
        ('accept', 'neg'),
        ('accepta', 'neg'),
        ('accepted', 'neg'),
        ('accepts', 'neg'),
        ('advantage', 'neg'),
        ('adventur', 'neg'),
        ('assur', 'neg'),
        ('award', 'neg'),
        ('best', 'neg'),
        ('bold', 'neg'),
        ('brave', 'neg'),
        ('bright', 'neg'),
        ('certain', 'neg'),
        ('challeng', 'neg'),
         ('confidence', 'neg'),
        ('commitment', 'neg'),
        ('confidently', 'neg')
        ]
    test = [
        ('I do enjoy my job', 'neg'),
        ("I feeling good today.", 'neg'),
        ("I feel amazing!", 'neg'),
        ('Gary is a friend of mine.', 'neg'),
        ("I believe I'm doing this.", 'neg')
        ]

    cl = NaiveBayesClassifier(train)

if __name__ == "__main__":
# calling main function
    main()