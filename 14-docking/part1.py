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
        result += a[i]*2**i
    return result

# Value in base 10, return base 10
def maskValue(v, mask):
    a = decToBin36(v)
    for i in range(36):
        if mask[35-i] != "X":
            a[i] = int(mask[35-i])
    return bin36ToDec(a)

def main():
    f = open("input")
    mask = "X" * 36
    mem = {}
    for l in f:
        if len(l.strip()) != 0:
            command, value = l.strip().split(" = ")
            if command == "mask":
                mask = value
            else:
                value = int(value)
                address = command[4:-1]
                mem[address] = maskValue(value, mask)
    sum = 0
    # for e in mem:
    #     print("mem["+e+"] = "+str(mem[e]))
    #     sum += mem[e]
    print(sum)




main()
