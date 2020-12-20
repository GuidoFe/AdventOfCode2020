import numpy as np


def searchRight(columnToSearch, tiles, excluded):
    flippedColumnToSearch = np.flip(columnToSearch)
    found = False
    foundTile = -1
    for tile in tiles:
        if tile not in excluded:
            if np.array_equal(columnToSearch, tiles[tile][:, 0]):
                foundTile = tile
                found = True
            elif np.array_equal(flippedColumnToSearch, tiles[tile][:, 0]):
                tiles[tile] = np.flip(tiles[tile], [0])
                foundTile = tile
                found = True
            elif np.array_equal(columnToSearch, tiles[tile][0, :]):
                tiles[tile] = np.flip(np.rot90(tiles[tile]), [0])
                foundTile = tile
                found = True
            elif np.array_equal(flippedColumnToSearch, tiles[tile][0, :]):
                tiles[tile] = np.rot90(tiles[tile])
                foundTile = tile
                found = True
            elif np.array_equal(columnToSearch, tiles[tile][:, 9]):
                tiles[tile] = np.flip(np.rot90(tiles[tile], 2), [0])
                foundTile = tile
                found = True
            elif np.array_equal(flippedColumnToSearch, tiles[tile][:, 9]):
                tiles[tile] = np.rot90(tiles[tile], 2)
                foundTile = tile
                found = True
            elif np.array_equal(columnToSearch, tiles[tile][9, :]):
                tiles[tile] = np.rot90(tiles[tile], 3)
                foundTile = tile
                found = True
            elif np.array_equal(flippedColumnToSearch, tiles[tile][9, :]):
                tiles[tile] = np.flip(np.rot90(tiles[tile], 3), [0])
                foundTile = tile
                found = True
        if found:
            break
    return found, foundTile


def converter(c):
    if c == "#":
        return int(1)
    else:
        return int(0)


def findAndPaintMonser(row, col, m):
    monsterRows = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]
    for i, r in enumerate(monsterRows):
        for j in r:
            if m[row + i, col + j] != 1:
                return False
    for i, r in enumerate(monsterRows):
        for j in r:
            m[row + i][col + j] = int(2)
    return True


def main():
    freeTiles = {}
    tiles = {}
    row = []
    lastTileId = None
    f = open("input")
    for line in f:
        line = line.strip()
        if len(line) > 0:
            if line[0] == "T":
                lastTileId = line.split(" ")[1]
                lastTileId = int(lastTileId.replace(":", ""))
            else:
                if lastTileId in freeTiles:
                    freeTiles[lastTileId] = np.vstack([freeTiles[lastTileId], list(map(converter, line))])
                else:
                    freeTiles[lastTileId] = np.array(list(map(converter, line)))
    f.close()
    # Pick up a random origin tile
    randomTileId = list(freeTiles.keys())[0]
    row = [randomTileId]
    # Stages: 0 = find first row, 1 = find upper rows, 2 = find lower rows
    stage = 0
    while stage < 3:
        found = True
        # Search left of origin tile
        while found:
            columnToSearch = freeTiles[row[len(row) - 1]][:, 9]
            found, tile = searchRight(columnToSearch, freeTiles, row)
            if found:
                row.append(tile)
        # Search right of origin tile
        found = True
        while found:
            columnToSearch = freeTiles[row[0]][:, 0]
            found, tile = searchRight(columnToSearch, freeTiles, row)
            if found:
                freeTiles[tile] = np.flip(freeTiles[tile], [1])
                row.insert(0, tile)
        for e in row:
            tiles[e] = freeTiles[e]
            del freeTiles[e]
        if stage == 0 or stage == 1:
            found, nextTile = searchRight(tiles[row[0]][0, :], freeTiles, [])
            if stage == 0:
                image = [row.copy()]
                if found:
                    stage = 1
                else:
                    found = 2
            else:
                image.insert(0, row.copy())
                if not found:
                    stage = 2
            if found:
                freeTiles[nextTile] = np.rot90(freeTiles[nextTile])
                row = [nextTile]
            else:
                found, nextTile = searchRight(tiles[image[len(image) - 1][0]][9, :], freeTiles, [])
                if found:
                    freeTiles[nextTile] = np.flip(np.rot90(freeTiles[nextTile], axes=(1, 0)), [1])
                    row = [nextTile]
                else:
                    break
        else:
            image.append(row.copy())
            found, nextTile = searchRight(tiles[row[0]][9, :], freeTiles, [])
            if found:
                freeTiles[nextTile] = np.flip(np.rot90(freeTiles[nextTile], axes=(1, 0)), [1])
                row = [nextTile]
            else:
                break
    w = len(image[0]) - 1
    h = len(image) - 1
    print(image[0][0] * image[0][w] * image[h][0] * image[h][w])
    m = np.array([])
    for tileRow in image:
        for row in range(1, 9):
            r = []
            for tile in tileRow:
                r = np.concatenate((r, tiles[tile][row, 1:9]), axis=None)
            if len(m) == 0:
                m = np.array([r])
            else:
                m = np.concatenate((m, [r]), axis=0)
    hasBeenFound = False
    nRotations = 0
    maxRow = len(m) - 2
    maxCol = len(m[0, :]) - 19
    while hasBeenFound is False:
        for row in range(maxRow):
            for col in range(maxCol):
                found = findAndPaintMonser(row, col, m)
                if found:
                    hasBeenFound = True
        if not hasBeenFound:
            if nRotations < 3:
                nRotations += 1
                print("Rotating...")
                m = np.rot90(m)
            else:
                print("Flipping and rotating...")
                nRotations = 0
                m = np.rot90(m)
                m = np.flip(m, axis=1)

    for row in range(len(m)):
        for e in m[row, :]:
            if e == 2:
                print("\u001b[32m█", end="")
            elif e == 1:
                print("\u001b[36m≋", end="")
            else:
                print(" ", end="")
        print("")
    sum = 0
    for row in m:
        for e in row:
            if e == 1:
                sum += 1
    print("\u001b[0m" + str(sum))


main()
