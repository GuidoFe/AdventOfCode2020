import math
import sys

def main():
    f = open("input")
    group = []
    sum = 0
    common = []
    newGroup = True
    for line in f:
        line = line.strip()
        if len(line) == 0:
            sum += len(group)
            group = []
            newGroup = True
        else:
            if newGroup:
                newGroup = False
                for c in line:
                    group.append(c)
                group.sort()
            elif len(group) > 0:
                common=[]
                for c in line:
                    start = 0
                    end = len(group) - 1
                    while True:
                        mid = int(round((end-start)/2 + start))
                        if group[mid] == c:
                            common.append(group[mid])
                            break
                        elif c > group[mid]:
                            start = mid + 1
                        else:
                            end = mid - 1
                        if start > end:
                            break
                common.sort()
                group = list(common)
    sum += len(group)
    print(sum)

main()
