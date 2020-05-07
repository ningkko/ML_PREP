from ConceptualDependency import Distance, CSV, histogram, Sort
import numpy as np
import pandas as pd


def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv", "tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()

    print("Calculating...")
    # stores all output with text, distances and text lengths
    output = []
    # output with bert classification number
    output_bert = []

    # only output with edit_distance>= 8
    output_E8 = []

    # mean and median of the first 432 original lines of file
    original_sentences_len = []

    # number of pairs with ED >= 8 and bert numbers == 1
    bert_number_1_g8 = 0
    # number of pairs with ED >= 8
    ED_number_g8 = 0

    i = 0
    for pairs in texts:
        # progress
        print(i / 186624)

        text_num_1 = pairs[0]
        text_num_2 = pairs[1]
        bert_classification = pairs[2]
        sent1 = pairs[3]
        sent2 = pairs[4]

        # distances
        editDistance = Distance.editDistance(sent1, sent2)
        jaccardDistance = Distance.jaccardDistance(sent1, sent2)

        # sentence lengths
        len_sent1 = len(sent1.split(" "))
        len_sent2 = len(sent2.split(" "))

        # a return list
        lst = [text_num_1, text_num_2, str(jaccardDistance), str(editDistance), sent1, sent2, len_sent1, len_sent2]
        lst_with_bert = [text_num_1, text_num_2, bert_classification, str(jaccardDistance), str(editDistance), sent1,
                         sent2, len_sent1, len_sent2]

        output.append(lst)
        output_bert.append(lst_with_bert)

        # -------- add pairs with edit distances >= 8
        if editDistance >= 8:
            output_E8.append(lst)
            ED_number_g8 += 1

            # number of pairs with bert classification as 1
            if int(bert_classification) == 1:
                bert_number_1_g8 += 1

        # finds the original sentences
        if i <= 431:
            original_sentences_len.append(len_sent2)

        # For test

        '''        
        if i > 500:
            break
        '''

        i += 1

    # calculate median and mean
    original_median = np.median(original_sentences_len)
    original_mean = np.mean(original_sentences_len)

    print("Calculation done.")

    '''
    # print outputs for test
    for o in output:
        print(o)

    for o8 in output_E8:
        print(o8)
    '''

    print("original_median: " + str(original_median) + "\n" +
          "original_mean: " + str(original_mean) + "\n" +
          "% of bert == 1: " + str(bert_number_1_g8 / ED_number_g8))

    print("-------------------------------------\n"
          "Writing results to file...")

    txt = open("outputs/output.txt", "w")
    txt.write("original_median: " + str(original_median) + "\n" +
              "original_mean: " + str(original_mean) + "\n" +
              "% of bert == 1: " + str(ED_number_g8 / ED_number_g8))

    txt.close()

    CSV.write_data("outputs/output_with_berts.csv", output_bert, with_bert=True)
    '''
    CSV.write_data("outputs/output.csv", output)
    CSV.write_data("outputs/output_e8.csv", output_E8, with_bert=True)
    print("++++++++++++++++++++++++++++++\nWriting done")

    # print("++++++++++++++++++++++++++++++++++++\n" +
    #      "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)

    print("Sorting...")
    Sort.sort()
    print("Sorting done")

    edit_hist = histogram.edit_hist()
    jaccard_hist = histogram.jaccard_hist()

    edit_hist_df = pd.DataFrame(edit_hist)
    edit_hist_df.to_csv('outputs/edit_histogram.csv', index=False)

    jaccard_hist_df = pd.DataFrame(jaccard_hist)
    jaccard_hist_df.to_csv('outputs/jaccard_histogram.csv', index=False)
    '''


main()
