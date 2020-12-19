class Rule:
    def __init__(self, rules):
        self.rules = rules

    def checkValidity(self, startingOffset, string, ruleDict):
        if isinstance(self.rules[0][0], str):
            if self.rules[0][0] == string[startingOffset]:
                return True, startingOffset + 1
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
    f = open("input")
    isReadingRules = True
    ruleDict = {}
    count = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            if isReadingRules:
                isReadingRules = False
                print(ruleDict)
        elif isReadingRules:
            n, rulesString = line.split(": ", 1)
            n = int(n)
            if rulesString[0] == '"':
                ruleDict[n] = Rule([[rulesString[1]]])
            else:
                rules = []
                for rule in rulesString.split(" | "):
                    rules.append(list(map(lambda x: int(x), rule.split(" "))))
                ruleDict[n] = Rule(rules)
        else:
            isValid, offset = ruleDict[0].checkValidity(0, line, ruleDict)
            if isValid and offset == len(line):
                print("Line " + line + " OK")
                count += 1
            else:
                print("Line " + line + " NO")
    print(count)


main()
