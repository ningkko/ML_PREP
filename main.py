import CSV
import Distance
import Sort


def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv", "tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()
    print(len(texts))

    print("Calculating...")
    output = []
    i = 0
    for pairs in texts:
        print(i / 186624)
        editDistance = str(Distance.editDistance(pairs[2], pairs[3]))
        jaccardDistance = str(Distance.jaccardDistance(pairs[2], pairs[3]))
        output.append([pairs[0], pairs[1], jaccardDistance, editDistance, pairs[2], pairs[3]])
        i += 1
    print("Calculation done.")

    print(output)

    print("Writing results to file...")
    CSV.write("output.csv", output)
    print("++++++++++++++++++++++++++++++\nWriting done")

    # print("++++++++++++++++++++++++++++++++++++\n" +
    #      "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)

    print("Sorting...")
    Sort.sort()
    print("Sorting done")


main()
