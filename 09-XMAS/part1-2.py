PREAMBLE = 25


def main():
    f = open("input")
    values = []
    input = []
    for line in f:
        input.append(int(line.strip()))
    for i in range(PREAMBLE):
        values.append(input[i])
    for n in input[PREAMBLE:]:
        found = False
        for i in range(PREAMBLE - 1):
            if values[i] < n:
                for j in range(i + 1, PREAMBLE):
                    if values[i] + values[j] == n and values[i] != values[j]:
                        found = True
                        break
            if found:
                break
        if found:
            values = values[1:]
            values.append(n)
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
    result = input[offset:end + 1]
    h = max(result)
    k = min(result)
    print("Sum of min and max: " + str(k + h))


main()
