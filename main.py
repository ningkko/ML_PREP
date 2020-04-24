import CSV
import Distance


def main():
    print("Reading file...")
    texts = CSV.read_to_list("data/babel_paraphrases_bert_classifications.tsv")
    print("++++++++++++++++++++++++++++++\nReading done")

    # text1, text2 = Distance.getInputs()
    print(len(texts))

    print("Calculating...")
    output = []

    i = 0
    for pairs in texts:
        print(i/186624)
        editDistance = str(Distance.editDistance(pairs[0], pairs[1]))
        jaccardDistance = str(Distance.jaccardDistance(pairs[0], pairs[1]))
        output.append([pairs[0], pairs[1], editDistance, jaccardDistance])
        i+=1
    print("Calculation done.")

    print(output)

    print("Writing results to file...")
    CSV.write("output.csv", output)
    print("++++++++++++++++++++++++++++++\nWriting done")

    # print("++++++++++++++++++++++++++++++++++++\n" +
    #      "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)


main()
