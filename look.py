# First, you're going to need to import wordnet:
from nltk.corpus import wordnet


def meaning(word):
    syns = wordnet.synsets(word)
    # An example of a synset:
    print(syns[0].name())
    # Just the word:
    return (syns[0].lemmas()[0].name())
    # Definition of that first synset:
    print(syns[0].definition())
    # Examples of the word in use in sentences:
    print(syns[0].examples())


def antonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())  # adding into antonyms
    return set(antonyms)


def synonym(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())
        return (set(synonyms))

# meaning(word)
# anonym(word)
