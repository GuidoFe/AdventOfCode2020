import sys
import math

def find2020(l):
    while(True):
        a = l[0]
        begin = 1
        end = len(l)-1

        #Check extremes of the set
        if (a+l[begin])==2020:
            return True, a, l[begin]
        if (a+l[end])==2020:
            return True, a, l[end]

        while end-begin>1:
            middle = math.floor((end-begin)/2+begin)
            if a+l[middle]==2020:
                return True, a, l[middle]
            if a+l[middle] < 2020:
                begin = middle
            else:
                end = middle
        l.pop(0)
        if len(l)==0:
            return False, None, None

def main():
    # Get data from file passed as first argument
    if len(sys.argv) < 2:
        print("Please specify input file as first argument")
        exit(1)
    try:
        f = open(sys.argv[1])
    except OSError as e:
        print("Error: can't find or read file")
        exit(1)
    inputList = list()
    for entry in f:
        inputList.append(int(entry))
    f.close()
    #Sort items to allow binary search
    inputList.sort()
    found, a, b = find2020(inputList)
    if found:
        print("Answer: ", a*b,", from the numbers ", a, " and ", b)
        exit(0)
    else:
        print("Answer not found")
        exit(1)

main()
