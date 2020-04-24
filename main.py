import csv
import Distance


def main():
    text1, text2 = Distance.getInputs()
    editDistance = str(Distance.editDistance(text1, text2))
    jaccardDistance = str(Distance.jaccardDistance(text1, text2))

    print("++++++++++++++++++++++++++++++++++++\n" +
          "Edit distance: " + editDistance + "\nJaccard distance: " + jaccardDistance)

    with open('output.csv', 'w') as csvfile:
        pen = csv.writer(csvfile)
        pen.writerow(['text1'] + ['text2'] + ['edit distance'] + ['Jaccard distance'])
        pen.writerow([text1, text2, editDistance, jaccardDistance])

    csvfile.close()


main()
