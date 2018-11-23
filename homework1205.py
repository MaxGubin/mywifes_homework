from __future__ import print_function

CSV_NUM_FILEDS = 5
CSV_SID = 0
CSV_GPA = 4


def load_file():
    """Loads the file, return a list of tuples with SID, GPA"""
    result = []
    for line in open('cats.txt'):
        elements = line.strip().split(',')
        if len(elements) != CSV_NUM_FILEDS:
            continue  # invalid number of fields
        result.append((int(elements[CSV_SID]), float(elements[CSV_GPA])))
    return result


def print_data(data):
    """Prints SID, GPA, and summaries"""
    print("SID\t\tGPA")
    print("___\t\t___")
    for v in data:
        print(v[0], "\t\t", v[1])

    gpas = [v[1] for v in data]
    if gpas:
        print()  # add an empty line
        print("Average GPA:\t%.2f" % (sum(gpas)/float(len(gpas))))
        print("High GPA:\t%.2f" % max(gpas))
        print("Low GPA:\t%.2f" % min(gpas))


def main():
    data = load_file()
    print_data(data)


if __name__ == "__main__":
    main()
