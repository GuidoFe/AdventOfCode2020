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
        r = 1
        directions = {"l": True, "tl": True, "t": True, "tr": True, "r": True,
                      "br": True, "b": True, "bl": True}
        if self.type != -1:
            while shouldContinueScan(directions):
                occupied += scanRing(self, m, r, directions)
                r += 1
        if self.type == 0 and occupied == 0:
            self.newType = 1
        elif self.type == 1 and occupied >= 5:
            self.newType = 0
        else:
            self.newType = self.type
        return self.type != self.newType


def isMatrixElementValid(m, row, col):
    maxRow = len(m)
    maxCol = len(m[0])
    if 0 <= row < maxRow and 0 <= col < maxCol:
        return True
    else:
        return False


def scanTile(m, row, col, directions, direction):
    val = 0
    if isMatrixElementValid(m, row, col):
        t = m[row][col].type
        if t >= 0:
            directions[direction] = False
            if t == 1:
                val = 1
    else:
        directions[direction] = False
    return val


def scanRing(e, m, r, directions):
    sum = 0
    if directions["l"]:
        sum += scanTile(m, e.row, e.col - r, directions, "l")
    if directions["tl"]:
        sum += scanTile(m, e.row - r, e.col - r, directions, "tl")
    if directions["t"]:
        sum += scanTile(m, e.row - r, e.col, directions, "t")
    if directions["tr"]:
        sum += scanTile(m, e.row - r, e.col + r, directions, "tr")
    if directions["r"]:
        sum += scanTile(m, e.row, e.col + r, directions, "r")
    if directions["br"]:
        sum += scanTile(m, e.row + r, e.col + r, directions, "br")
    if directions["b"]:
        sum += scanTile(m, e.row + r, e.col, directions, "b")
    if directions["bl"]:
        sum += scanTile(m, e.row + r, e.col - r, directions, "bl")
    return sum


def shouldContinueScan(directions):
    for d in directions:
        if directions[d]:
            return True
    return False


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
