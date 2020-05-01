import CSV
import Distance
import Sort
import numpy as np


def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv", "tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()
    print(len(texts))

    print("Calculating...")
    output = []
    # mean and median of the first 432 original lines of file
    original_sentences_len = []

    i = 0
    for pairs in texts:
        print(i / 186624)
        sent1 = pairs[2]
        sent2 = pairs[3]
        editDistance = str(Distance.editDistance(sent1, sent2))
        jaccardDistance = str(Distance.jaccardDistance(sent1, sent2))
        len_sent1 = len(sent1.split(" "))
        len_sent2 = len(sent2.split(" "))
        output.append([pairs[0], pairs[1], jaccardDistance, editDistance, pairs[2], pairs[3], len_sent1, len_sent2])

        if i <= 431:
            original_sentences_len.append(len_sent2)

        if i > 300:
            break

        i += 1

    original_median = np.median(original_sentences_len)
    original_mean = np.mean(original_sentences_len)

    print("Calculation done.")

    for o in output:
        print(o)
    print("original_median: " + str(original_median) + "\n" +
          "original_mean: " + str(original_mean))

    print("Writing results to file...")

    txt = open("output.txt", "w")
    txt.write("original_median: " + str(original_median) + "\n" +
              "original_mean: " + str(original_mean))
    txt.close()

    CSV.write("output.csv", output)
    print("++++++++++++++++++++++++++++++\nWriting done")

    # print("++++++++++++++++++++++++++++++++++++\n" +
    #      "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)

    print("Sorting...")
    Sort.sort()
    print("Sorting done")


main()
