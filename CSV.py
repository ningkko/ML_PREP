import csv


def read_to_list(file_path):
    texts = []

    with open(file_path) as file:
        reader = csv.reader(file, delimiter='\t')

        for row in reader:
            # data in the format of ['0', '0', '1', 'John died because he was unable to breathe .', 'John died
            # because he was unable to breathe .']
            text1 = row[3].replace(" .", "")
            text2 = row[4].replace(" .", "")

            texts.append([text1, text2])

    file.close()
    return texts


def write(file_path, output_file):
    with open(file_path, 'w') as file:
        pen = csv.writer(file)

        pen.writerow(['text1'] + ['text2'] + ['edit distance'] + ['Jaccard distance'])
        for row in output_file:
            pen.writerow(row)

    file.close()


def printFile(file_path):
    with open(file_path) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            print(row)
    file.close()
