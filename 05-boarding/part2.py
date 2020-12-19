import math


def main():
    ROWS = 128
    COLS = 8
    plane = {}
    f = open("input")
    minRow = ROWS
    maxRow = 0
    for seat in f:
        r_cursor = [0, ROWS - 1]
        c_cursor = [0, COLS - 1]
        for s in seat:
            if s == "F":
                r_cursor[1] = math.floor((r_cursor[1] - r_cursor[0]) / 2 + r_cursor[0])
            elif s == "B":
                r_cursor[0] = math.ceil((r_cursor[1] - r_cursor[0]) / 2 + r_cursor[0])
            elif s == "L":
                c_cursor[1] = math.floor((c_cursor[1] - c_cursor[0]) / 2 + c_cursor[0])
            elif s == "R":
                c_cursor[0] = math.ceil((c_cursor[1] - c_cursor[0]) / 2 + c_cursor[0])
        if r_cursor[0] != r_cursor[1] or c_cursor[0] != c_cursor[1]:
            print("Error seat " + s + ": " + str(r_cursor) + "; " + str(c_cursor))
            exit(1)
        row = r_cursor[0]
        col = c_cursor[0]
        if row < minRow:
            minRow = row
        if row > maxRow:
            maxRow = row
        if str(row) in plane:
            plane[str(row)].append(col)
        else:
            plane[str(row)] = [col]
    for row in plane.keys():
        if len(plane[row]) >= 2:
            plane[row].sort()
            for i in range(len(plane[row]) - 1):
                if plane[row][i + 1] - plane[row][i] == 2:
                    print(int(row) * 8 + plane[row][i] + 1)


main()
