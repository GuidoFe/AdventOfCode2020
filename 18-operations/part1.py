def applyOperation(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "*":
        return a * b
    else:
        print("Operation " + operation + " not permitted")
        exit(1)


def parseExpression(expr, offset):
    result = 0
    operation = "+"
    i = offset
    while i < len(expr):
        if expr[i] == ")":
            return result, i
        elif expr[i] == "(":
            r, jumpTo = parseExpression(expr, i + 1)
            result = applyOperation(result, r, operation)
            i = jumpTo
        elif expr[i] == "*" or expr[i] == "+":
            operation = expr[i]
        else:
            result = applyOperation(result, int(expr[i]), operation)
        i += 1
    return result, len(expr) - 1


def main():
    f = open("input")
    sum = 0
    for line in f:
        line = line.strip()
        line = line.replace("(", "( ")
        line = line.replace(")", " )")
        if len(line) > 0:
            expr = line.split(" ")
            val, i = parseExpression(expr, 0)
            sum += val
    print(sum)


main()
