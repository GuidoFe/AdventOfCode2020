

def main():
    public_keys = [17607508, 15065270]
    # public_keys = [5764801, 17807724]
    loops = []
    for key in public_keys:
        value = 1
        loop = 0
        while value != key:
            loop += 1
            value *= 7
            value = value % 20201227
        loops.append(loop)
    value = 1
    for loop in range(loops[0]):
        value *= public_keys[1]
        value = value % 20201227
    print(value)


main()
