import sys

# Uncomment the print commands to have a map of the trajectory

def countTrees(f, width, height, slopeX, slopeY):
    f.seek(0)
    cursor = 0
    count = 0
    for i in range(0, height, slopeY):
        line = f.readline().strip()
        if line[cursor] == '#':
            count += 1
            line = line[:cursor]+'X'+line[(cursor+1):]
        else:
            line = line[:cursor]+'O'+line[(cursor+1):]
        # print(line)
        for i in range(1, slopeY):
            empty=f.readline().strip()
            # print(empty)
        # +1 to start the array at 1
        cursor = ((cursor + 1 + slopeX) % (width)) - 1
        if cursor < 0:
            cursor = width + cursor
    return count


def main():
    f = open("input")
    line = f.readline()
    width = len(line.strip())
    f.seek(0)
    height=0
    for line in f:
        if len(line)>1:
            height += 1
    case1 = countTrees(f, width, height, 1, 1)
    case2 = countTrees(f, width, height, 3, 1)
    case3 = countTrees(f, width, height, 5, 1)
    case4 = countTrees(f, width, height, 7, 1)
    case5 = countTrees(f, width, height, 1, 2)
    prod = case1 * case2 * case3 * case4 * case5
    print("{} x {} x {} x {} x {} = {}".format(case1, case2, case3, case4, case5, prod))
    f.close()

main()
