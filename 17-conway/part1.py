def coordToString(x, y, z):
    return str(x) + "," + str(y) + "," + str(z)


class Pixel:
    def __init__(self, x, y, z, value):
        self.x = x
        self.y = y
        self.z = z
        self.value = value
        self.nextValue = None
        self.name = coordToString(x, y, z)
        self.neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i != 0 or j != 0 or k != 0:
                        self.neighbours.append(coordToString(x + i, y + j, z + k))


def main():
    f = open("input")
    pixels = {}
    for y, line in enumerate(f):
        line = line.strip()
        for x, c in enumerate(line.strip()):
            if c == "#":
                pixels[coordToString(x + 1, 10 - y, 5)] = Pixel(x + 1, 10 - y, 5, True)
    for turn in range(6):
        addPixels = set()
        pixelsToDelete = set()
        for pStr in pixels:
            sum = 0
            if pixels[pStr].value:
                for next in pixels[pStr].neighbours:
                    if next not in pixels:
                        addPixels.add(next)
            else:
                sum = 0
                for next in pixels[pStr].neighbours:
                    if next in pixels and pixels[next].value:
                        sum = 1
                        break
                if sum == 0:
                    pixelsToDelete.add(pStr)
        for pStr in pixelsToDelete:
            del pixels[pStr]
        for pStr in addPixels:
            coords = list(map(lambda x: int(x), pStr.split(",")))
            pixels[pStr] = Pixel(coords[0], coords[1], coords[2], False)
        for pStr in pixels:
            sum = 0
            for next in pixels[pStr].neighbours:
                if next in pixels and pixels[next].value:
                    sum += 1
            if pixels[pStr].value:
                if sum == 2 or sum == 3:
                    pixels[pStr].nextValue = True
                else:
                    pixels[pStr].nextValue = False
            else:
                if sum == 3:
                    pixels[pStr].nextValue = True
                else:
                    pixels[pStr].nextValue = False
        for pStr in pixels:
            pixels[pStr].value = pixels[pStr].nextValue
    sum = 0
    for pStr in pixels:
        if pixels[pStr].value:
            sum += 1
    print(sum)


main()
