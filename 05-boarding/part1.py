import math
import numpy as np


def main():
    ROWS = 128
    COLS = 8
    plane = np.full((ROWS, COLS), "_")
    f = open("input")
    record = 0
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
        id = r_cursor[0] * 8 + c_cursor[0]
        if id > record:
            record = id
        plane[r_cursor[0], c_cursor[0]] = "O"
    for i in range(ROWS):
        row = ""
        for j in range(int(COLS / 2)):
            row += str(plane[i][j])
        row += " "
        for j in range(int(COLS / 2), COLS):
            row += str(plane[i][j])
        print(row + " " + str(i))
    print(record)


main()
