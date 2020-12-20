class Rule:
    def __init__(self, rules, val):
        self.rules = rules
        self.val = val

    def checkValidity(self, startingOffset, string, ruleDict):
        if isinstance(self.rules[0][0], str):
            if startingOffset < len(string):
                if self.rules[0][0] == string[startingOffset]:
                    return True, startingOffset + 1
                else:
                    return False, startingOffset
            else:
                return False, startingOffset
        else:
            for sequence in self.rules:
                i = startingOffset
                for rulePos, rule in enumerate(sequence):
                    match, offset = ruleDict[rule].checkValidity(i, string, ruleDict)
                    if match:
                        if rulePos == len(sequence) - 1:
                            return True, offset
                        else:
                            i = offset
                    else:
                        break
            return False, startingOffset

    def __repr__(self):
        return str(self.rules)


def main():
    f = open("input2")
    isReadingRules = True
    ruleDict = {}
    count = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            if isReadingRules:
                isReadingRules = False
        elif isReadingRules:
            n, rulesString = line.split(": ", 1)
            n = int(n)
            if rulesString[0] == '"':
                ruleDict[n] = Rule([[rulesString[1]]], n)
            else:
                rules = []
                for rule in rulesString.split(" | "):
                    rules.append(list(map(lambda x: int(x), rule.split(" "))))
                ruleDict[n] = Rule(rules, n)
        else:
            n8 = 1
            n11 = 1
            while True:
                end8 = 0
                for i in range(n8):
                    isValid, end8 = ruleDict[42].checkValidity(end8, line, ruleDict)
                    if not isValid:
                        print(" NO", line)
                        break
                if not isValid:
                    break
                end11_42 = end8
                for i in range(n11):
                    isValid, end11_42 = ruleDict[42].checkValidity(end11_42, line, ruleDict)
                    if not isValid:
                        break
                if not isValid:
                    n8 += 1
                    n11 = 1
                    continue
                end11_31 = end11_42
                for i in range(n11):
                    isValid, end11_31 = ruleDict[31].checkValidity(end11_31, line, ruleDict)
                    if not isValid:
                        break
                if not isValid:
                    if end11_31 > len(line):
                        n8 += 1
                        n11 = 1
                        continue
                    else:
                        n11 += 1
                        continue
                else:
                    if end11_31 == len(line):
                        count += 1
                        print("YES", line)
                        break
                    else:
                        n11 += 1
                        continue
    print(count)


main()
