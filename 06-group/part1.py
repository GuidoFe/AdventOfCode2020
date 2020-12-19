def main():
    f = open("input")
    sum = 0
    group = set()
    newGroup = True
    for line in f:
        line = line.strip()
        if len(line) == 0:
            sum += len(group)
            group = set()
            newGroup = True
        else:
            if newGroup:
                newGroup = False
                for c in line:
                    group.add(c)
            elif len(group) < 26:
                for c in line:
                    group.add(c)
    sum += len(group)
    print(sum)


main()
