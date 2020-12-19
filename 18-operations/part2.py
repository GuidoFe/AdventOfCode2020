def parseExpression(expr):
    elements = []
    i = 0
    while i < len(expr):
        if expr[i] == "(":
            j = i
            count = 1
            while count != 0:
                j += 1
                if expr[j] == "(":
                    count += 1
                elif expr[j] == ")":
                    count -= 1
            elements.append(parseExpression(expr[i + 1:j]))
            i = j
        elif expr[i] == "*" or expr[i] == "+":
            elements.append(expr[i])
        else:
            elements.append(int(expr[i]))
        i += 1
    listAdded = []
    i = 0
    while i < len(elements):
        if elements[i] == "+":
            last = listAdded.pop()
            listAdded.append(last + elements[i + 1])
            i += 1
        else:
            listAdded.append(elements[i])
        i += 1
    result = 1
    for e in listAdded:
        if e != "*":
            result *= e
    return result


def main():
    f = open("input")
    sum = 0
    for line in f:
        line = line.strip()
        if len(line) > 0:
            line = line.replace("(", "( ")
            line = line.replace(")", " )")
            expr = line.split(" ")
            val = parseExpression(expr)
            sum += val
    print(sum)


main()
