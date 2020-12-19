def decToBin36(n):
    result = []
    while n != 0:
        m = n % 2
        result.append(m)
        n = n // 2
    for i in range(len(result), 36):
        result.append(0)
    return result


def bin36ToDec(a):
    result = 0
    for i in range(len(a)):
        result += a[i] * 2**i
    return result


def incrementBin(n):
    remainder = 1
    for i in range(len(n)):
        val = (n[i] + remainder) % 2
        remainder = (n[i] + remainder) // 2
        n[i] = val
    return n


# Value in base 10, return base 10
def maskAddress(a, mask):
    v = decToBin36(int(a))
    floatingIndices = []
    for i in range(36):
        mIndex = 35 - i
        if mask[mIndex] != "0":
            if mask[mIndex] == "1":
                v[i] = 1
            else:
                v[i] = None
                floatingIndices.append(i)
    f = [1] * len(floatingIndices)
    results = []
    maxF = bin36ToDec(f) + 1
    for i in range(maxF):
        f = incrementBin(f)
        for j in range(len(f)):
            v[floatingIndices[j]] = f[j]
        results.append(str(bin36ToDec(v)))
    return results


def main():
    f = open("input")
    mask = "X" * 36
    mem = {}
    for line in f:
        if len(line.strip()) != 0:
            command, value = line.strip().split(" = ")
            if command == "mask":
                mask = value
            else:
                value = int(value)
                address = command[4:-1]
                addressList = maskAddress(address, mask)
                for e in addressList:
                    mem[e] = value
    sum = 0
    for e in mem:
        sum += mem[e]
    print(sum)


main()
