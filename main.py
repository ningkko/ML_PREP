import CSV
import Distance
import Sort
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv", "tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()
    print(len(texts))

    print("Calculating...")
    # stores all output with text, distances and text lengths
    output = []
    # only output with edit_distance>= 8
    output_E8 = []

    # mean and median of the first 432 original lines of file
    original_sentences_len = []

    i = 0
    for pairs in texts:
        print(i / 186624)
        sent1 = pairs[2]
        sent2 = pairs[3]
        editDistance = Distance.editDistance(sent1, sent2)
        jaccardDistance = Distance.jaccardDistance(sent1, sent2)
        len_sent1 = len(sent1.split(" "))
        len_sent2 = len(sent2.split(" "))

        bert_classification = pairs[2]
        # number of pairs with ED >= 8 and bert numbers == 1
        bert_number_1_g8 = 0
        # number of pairs with ED >= 8
        ED_number_g8 = 0

        lst = [pairs[0], pairs[1], str(jaccardDistance), str(editDistance), pairs[2], pairs[3], len_sent1, len_sent2]
        output.append(lst)

        if editDistance >= 8:
            output_E8.append(lst)
            ED_number_g8 += 1

            if bert_classification == 1:
                bert_number_1_g8 += 1

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

    for o8 in output_E8:
        print(o8)

    print("original_median: " + str(original_median) + "\n" +
          "original_mean: " + str(original_mean) + "\n" +
          "% of bert == 1: " + str(bert_number_1_g8 / ED_number_g8))

    print("Writing results to file...")

    txt = open("output.txt", "w")
    txt.write("original_median: " + str(original_median) + "\n" +
              "original_mean: " + str(original_mean) + "\n" +
              "% of bert == 1: " + str(bert_number_1_g8 / ED_number_g8))

    txt.close()

    CSV.write("output.csv", output)
    CSV.write("output_e>8.csv", output_E8)
    print("++++++++++++++++++++++++++++++\nWriting done")

    # print("++++++++++++++++++++++++++++++++++++\n" +
    #      "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)

    print("Sorting...")
    Sort.sort()
    print("Sorting done")


main()
