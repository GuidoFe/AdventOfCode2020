import sys
import math

def find2020(l):
    while(True):
        b=0
        while(True):
            b += 1
            begin = b+1
            end = len(l)-1
            if(begin >= len(l)):
                break
            #Check extremes of the set
            if (l[0]+l[b]+l[begin])==2020:
                return True, l[0], l[b], l[begin]
            if (l[0]+l[b]+l[end])==2020:
                return True, l[0], l[b], l[end]

            while end-begin>1:
                middle = math.floor((end-begin)/2+begin)
                if l[0]+l[b]+l[middle]==2020:
                    return True, l[0], l[b], l[middle]
                if l[0]+l[b]+l[middle] < 2020:
                    begin = middle
                else:
                    end = middle
        l.pop(0)
        if len(l)==0:
            return False, None, None, None

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
    found, a, b, c = find2020(inputList)
    if found:
        print("Answer: ", a*b*c,", from the numbers ", a, b, c)
        exit(0)
    else:
        print("Answer not found")
        exit(1)

main()
