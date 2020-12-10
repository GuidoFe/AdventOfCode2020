PREAMBLE = 25

def main():
    f = open("input")
    list = []
    input = []
    for l in f:
        input.append(int(l.strip()))
    for i in range(PREAMBLE):
        list.append(input[i])
    for n in input[PREAMBLE:]:
        found = False
        for i in range(PREAMBLE-1):
            if list[i] < n:
                for j in range(i+1, PREAMBLE):
                    if list[i] + list[j] == n and list[i] != list[j]:
                        found = True
                        break
            if found:
                break
        if found:
            list = list[1:]
            list.append(n)
        else:
            print("Invalid number: " + str(n))
            break
    if found:
        print("No invalid number found")
        exit(0)
    offset = 0
    end = -1
    i = 0
    sum = 0
    while i < len(input):
        sum += input[i]
        if sum == n and i - offset > 0:
            end = i
            break
        elif sum > n:
            offset += 1
            i = offset
            sum = 0
        else:
            i += 1
    result = input[offset:end+1]
    h = max(result)
    l = min(result)
    print("Sum of min and max: " + str(l+h))


main()
