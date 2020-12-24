import sys
import arcade
import math
#     (0, +1)    from odd y    (+1, +1)
#     (-1, +1)   from even y   (0, +1)
#
# (-1, 0)            ⬡            (+1, 0)
#
#     (0, -1)    from odd y    (+1, -1)
#     (-1, -1)   from even y   (0, -1)


class Visualizer(arcade.Window):
    def __init__(self, windowWidth, windowHeight, tiles):
        self.windowHeight = int(windowHeight)
        self.HALF_RANGE = 70
        self.w = windowWidth / (self.HALF_RANGE * 2)
        self.h = self.w * 2 / math.sqrt(3)
        self.windowWidth = round(windowHeight * self.w / self.h)
        super().__init__(self.windowWidth, self.windowHeight, "Mandelbrot set")
        self.tiles = tiles
        self.set_viewport(-self.HALF_RANGE * self.w, self.HALF_RANGE * self.w, -self.HALF_RANGE * 3 / 4 * self.h, self.HALF_RANGE * 3 / 4 * self.h)

    def on_draw(self):
        arcade.start_render()
        for i in range(-self.HALF_RANGE, self.HALF_RANGE + 1):
            for j in range(-self.HALF_RANGE, self.HALF_RANGE + 1):
                tile = (i, j)
                if tile in self.tiles:
                    isWhite = self.tiles[tile][0]
                else:
                    isWhite = True
                if isWhite:
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.BLACK
                centerY = 3 / 4 * self.h * j
                if j % 2 == 0:
                    centerX = self.w * i
                else:
                    centerX = self.w * i + 1 / 2 * self.w
                point_list = ((centerX, centerY + self.h / 2),
                              (centerX + self.w / 2, centerY + 1 / 4 * self.h),
                              (centerX + self.w / 2, centerY - 1 / 4 * self.h),
                              (centerX, centerY - self.h / 2),
                              (centerX - self.w / 2, centerY - 1 / 4 * self.h),
                              (centerX - self.w / 2, centerY + 1 / 4 * self.h))
                arcade.draw_polygon_filled(point_list, color)


def calculateNextTileStatus(coord, tiles):
    sum = 0
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if coord[1] % 2 == 0:
        offsets.append((-1, -1))
        offsets.append((-1, 1))
    else:
        offsets.append((1, -1))
        offsets.append((1, 1))
    tilesToAdd = []
    for offset in offsets:
        neighbourTile = (coord[0] + offset[0], coord[1] + offset[1])
        if neighbourTile in tiles:
            if tiles[neighbourTile][0] is False:
                sum += 1
        elif tiles[coord][0] is True:
            tilesToAdd.append(neighbourTile)
    # Add new tiles to the dict only if they don't exist yet and a white tile switches to black
    if tiles[coord][0] is True:
        if sum == 2:
            tiles[coord][1] = False
        else:
            tiles[coord][1] = True
            tilesToAdd = []
    else:
        if sum == 0 or sum > 2:
            tiles[coord][1] = True
        else:
            tiles[coord][1] = False
    return tuple(tilesToAdd)


def updateTileStatus(tiles):
    for tile in tiles:
        tiles[tile][0] = tiles[tile][1]


def main():
    f = open("input")
    # True = White, False = Black
    tiles = {}
    for line in f:
        line = line.strip()
        if len(line) > 0:
            i = 0
            coord = [0, 0]
            coordStr = ""
            while i < len(line):
                current = line[i]
                if current == "n" or current == "s":
                    isFromEven = (coord[1] % 2 == 0)
                    instruction = current + line[i + 1]
                    i += 1
                else:
                    instruction = current
                coordStr += " " + instruction
                if instruction == "ne":
                    if not isFromEven:
                        coord[0] += 1
                    coord[1] += 1
                elif instruction == "e":
                    coord[0] += 1
                elif instruction == "se":
                    if not isFromEven:
                        coord[0] += 1
                    coord[1] -= 1
                elif instruction == "sw":
                    if isFromEven:
                        coord[0] -= 1
                    coord[1] -= 1
                elif instruction == "w":
                    coord[0] -= 1
                elif instruction == "nw":
                    if isFromEven:
                        coord[0] -= 1
                    coord[1] += 1
                else:
                    print("Error: instruction " + instruction + " not valid", file=sys.stderr)
                    exit(1)
                i += 1
            coord = tuple(coord)
            if coord in tiles:
                tiles[coord][0] = not tiles[coord][0]
                tiles[coord][1] = tiles[coord][0]
            else:
                tiles[coord] = [False, False]
    sum = 0
    for tile in tiles:
        if tiles[tile][0] is False:
            sum += 1
    print("Part 1: " + str(sum))
    # Add white tiles adiacent to black tiles
    tilesToAdd = set()
    for tile in tiles:
        if tiles[tile][0] is False:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i != 0 or j != 0:
                        if (tile[0] + i, tile[1] + j) not in tiles:
                            tilesToAdd.add((tile[0] + i, tile[1] + j))
    for tile in tilesToAdd:
        tiles[tile] = [True, True]
    for i in range(100):
        tilesToAdd = set()
        for tile in tiles:
            result = (calculateNextTileStatus(tile, tiles))
            if len(result) > 0:
                tilesToAdd.update(result)
        updateTileStatus(tiles)
        for tile in tilesToAdd:
            tiles[tile] = [True, True]
        # print(tiles)
        # sys.stdin.readline()
    sum = 0
    for tile in tiles:
        if tiles[tile][0] is False:
            sum += 1
    app = Visualizer(700, 700, tiles)
    arcade.run()
    print("Part 2:", sum)


main()
