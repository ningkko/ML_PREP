import nltk
import EditDistance


def main():
    text1, text2 = EditDistance.getInputs()
    print("++++++++++++++++++++++++++++++++++++\n" +
          "Edit distance: " + str(EditDistance.editDistance(text1, text2)))


main()
