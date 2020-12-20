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
                    freeTiles[lastTileId] = np.vstack([freeTiles[lastTileId], list(map(lambda x: x == "#", line))])
                else:
                    freeTiles[lastTileId] = np.array(list(map(lambda x: x == "#", line)))
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
    for tileRow in image:
        for r in range(10):
            for tile in tileRow:
                for c in range(10):
                    if tiles[tile][r, c]:
                        print("█", end="")
                    else:
                        print(" ", end="")
            print("")
    w = len(image[0]) - 1
    h = len(image) - 1
    print(image[0][0] * image[0][w] * image[h][0] * image[h][w])


main()
