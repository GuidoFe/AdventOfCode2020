import sys
import math


def find2020(report):
    while(True):
        b = 0
        while(True):
            b += 1
            begin = b + 1
            end = len(report) - 1
            if(begin >= len(report)):
                break
            # Check extremes of the set
            if (report[0] + report[b] + report[begin]) == 2020:
                return True, report[0], report[b], report[begin]
            if (report[0] + report[b] + report[end]) == 2020:
                return True, report[0], report[b], report[end]

            while end - begin > 1:
                middle = math.floor((end - begin) / 2 + begin)
                if report[0] + report[b] + report[middle] == 2020:
                    return True, report[0], report[b], report[middle]
                if report[0] + report[b] + report[middle] < 2020:
                    begin = middle
                else:
                    end = middle
        report.pop(0)
        if len(report) == 0:
            return False, None, None, None


def main():
    # Get data from file passed as first argument
    if len(sys.argv) < 2:
        print("Please specify input file as first argument")
        exit(1)
    try:
        f = open(sys.argv[1])
    except OSError:
        print("Error: can't find or read file")
        exit(1)
    inputList = list()
    for entry in f:
        inputList.append(int(entry))
    f.close()
    # Sort items to allow binary search
    inputList.sort()
    found, a, b, c = find2020(inputList)
    if found:
        print("Answer: ", a * b * c, ", from the numbers ", a, b, c)
        exit(0)
    else:
        print("Answer not found")
        exit(1)


main()
