import nltk
nltk.download('punkt')


def getInputs():
    text1 = input("text1: ")
    if not text1:
        text1 = "But other sources close to the sale said Vivendi was keeping the door open to further bids and hoped " \
                "to see bidders interested in individual assets team up"
        print("Default text1: " + text1)

    text2 = input("text2: ")
    if not text2:
        text2 = "But other sources close to the sale said Vivendi was keeping the door open for further bids in the " \
                "next day or two"
        print("Default text2: " + text2)

    return text1, text2


def jaccardDistance(text1, text2):
    # the tokenize function converts a string to a set.
    # def tokenize(self, s):
    #    return s.split(self._string)

    # by definition the jaccard distance calculates unique
    set1 = set(nltk.word_tokenize(text1))
    set2 = set(nltk.word_tokenize(text2))
    return nltk.jaccard_distance(set1, set2)


def editDistance(text1, text2):
    token1 = nltk.word_tokenize(text1)
    token2 = nltk.word_tokenize(text2)
    return nltk.edit_distance(token1, token2)

