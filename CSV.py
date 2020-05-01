import csv


def read_to_list(file_path, file_type):
    texts = []

    deli = " "
    if file_type == "tsv":
        deli = "\t"

    with open(file_path) as file:
        reader = csv.reader(file, delimiter=deli)

        for row in reader:
            # data in the format of ['0', '0', '1', 'John died because he was unable to breathe .', 'John died
            # because he was unable to breathe .']
            num1, num2 = row[0], row[1]
            text1, text2 = row[3].replace(" .", ""), row[4].replace(" .", "")

            texts.append([num1, num2, text1, text2])

    file.close()
    return texts


def write(file_path, output_file):
    with open(file_path, 'w') as file:
        pen = csv.writer(file)

        pen.writerow(['ID1'] + ['ID2'] + ['Jaccard distance'] + ['Levenshtein distance'] + ['text1'] + ['text2']  + ['#text2'])
        for row in output_file:
            pen.writerow(row)

    file.close()


def printFile(file_path):
    with open(file_path) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            print(row)
    file.close()
