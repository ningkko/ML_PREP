import nltk


def getInputs():
    text1 = input("text1: ")
    if not text1:
        text1 = "But other sources close to the sale said Vivendi was keeping the door open to further bids and hoped " \
                "to see bidders interested in individual assets team up"
        print("Default text1: "+text1)

    text2 = input("text2: ")
    if not text2:
        text2 = " But other sources close to the sale said Vivendi was keeping the door open for further bids in the " \
                "next day or two"
        print("Default text2: "+text2)

    return text1, text2


def editDistance(text1, text2):

    # token1 = nltk.word_tokenize(text1)
    # token2 = nltk.word_tokenize(text2)

    return nltk.edit_distance(text1, text2)
