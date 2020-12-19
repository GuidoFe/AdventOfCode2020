
def findNearest(jumps, index):
    nearest = []
    i = index + 1
    while i < len(jumps) and jumps[i] - jumps[index] <= 3:
        nearest.append(i)
        i += 1
    return nearest


def main():
    f = open("input")
    jumps = [0]
    for line in f:
        jumps.append(int(line.strip()))
    jumps.sort()
    jumps.append(jumps[len(jumps) - 1] + 3)
    dict = {"0": 0, "1": 0, "2": 0, "3": 0}
    for i in range(len(jumps)):
        if i != 0:
            dict[str(jumps[i] - jumps[i - 1])] += 1
    print("Part 1: " + str(dict["1"] * dict["3"]))
    ways = [0 for i in range(len(jumps))]
    ways[len(ways) - 1] = 1
    for i in range(len(jumps) - 2, -1, -1):
        nearest = findNearest(jumps, i)
        for e in nearest:
            ways[i] += ways[e]
    print("Part 2:" + str(ways[0]))


main()
