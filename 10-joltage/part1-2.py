
def findNearest(list, index):
    l = []
    i = index + 1
    while i < len(list) and list[i] - list[index] <= 3:
        l.append(i)
        i += 1
    return l

def main():
    f = open("input")
    list = [0]
    for l in f:
        list.append(int(l.strip()))
    list.sort()
    list.append(list[len(list)-1]+3)
    dict = {"0": 0, "1": 0, "2": 0, "3": 0}
    for i in range(len(list)):
        if i != 0:
            dict[str(list[i]-list[i-1])] += 1
    print "Part 1: " + str(dict["1"] * dict["3"])
    ways = [0 for i in range(len(list))]

    prod = 1
    ways[len(ways)-1] = 1
    for i in range(len(list)-2, -1, -1):
        l = findNearest(list, i)
        for e in l:
            ways[i] += ways[e]
    print("Part 2:" + str(ways[0]))

main()
