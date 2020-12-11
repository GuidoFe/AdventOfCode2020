
class space:
    def __init__(self, char, row, col):
        if char == ".":
            self.type = -1
        elif char == "L":
            self.type = 0
        else:
            self.type = 1
        self.row = row
        self.col = col

    def value(self):
        if self.type == -1:
            return 0
        else:
            return self.type

    def flip(self):
        self.type = self.newType

    def calculate(self, m):
        occupied = 0
        row = self.row
        col = self.col
        for e in [(row-1,col),(row,col-1),(row-1,col-1),(row+1,col),(row,col+1),(row+1,col+1),(row-1,col+1),(row+1,col-1)]:
            isValid, type = returnTypeIfValid(m, e[0], e[1])
            if isValid:
                if type > -1:
                    occupied += type
        if self.type == 0 and occupied == 0:
            self.newType = 1
        elif self.type == 1 and occupied >= 4:
            self.newType = 0
        else:
            self.newType = self.type
        return self.type != self.newType

def returnTypeIfValid(m, row, col):
    maxRow = len(m)
    maxCol = len(m[0])
    if row >= 0 and col >= 0 and row < maxRow and col < maxCol:
        return True, m[row][col].type
    else:
        return False, None

def countOccupied(m):
    sum = 0
    for row in m:
        for e in row:
            sum += e.value()
    return sum

def main():
    f = open("input")
    room = []
    i = 0
    for line in f:
        if len(line.strip()) > 0:
            room.append([])
            j = 0
            for c in line.strip():
                room[i].append(space(c, i, j))
                j += 1
            i += 1
    while True:
        hasChanged = False
        for row in room:
            for e in row:
                if e.calculate(room):
                    hasChanged = True
        if not hasChanged:
            break
        else:
            for row in room:
                for e in row:
                    e.flip()
    print(countOccupied(room))



main()
