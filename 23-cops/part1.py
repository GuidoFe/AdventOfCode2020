# The index of the cups array inside the class is completely transparent


class CupList:
    def __init__(self, input):
        chars = []
        chars[:0] = input
        self.cups = []
        for c in chars:
            self.cups.append(int(c))
        self.currentCup = self.cups[0]

    def advanceCurrentCup(self):
        self.currentCup = self.getNext()
        return self.currentCup

    def setCurrentCup(self, cup):
        self.currentCup = cup

    def extract(self, start=None, n=1):
        if start is None:
            index = self.cups.index(self.currentCup)
        else:
            index = self.cups.index(start)
        if index + n > len(self.cups):
            result = self.cups[index:]
            result.extend(self.cups[:(n - (len(self.cups) - index))])
        else:
            result = self.cups[index:index + n]
        for c in result:
            self.cups.remove(c)
        return result

    def getNext(self):
        index = self.cups.index(self.currentCup) + 1
        if index >= len(self.cups):
            index = 0
        return self.cups[index]

    def __str__(self):
        s = ""
        for e in self.cups:
            s += str(e)
        return s

    def printFrom1(self):
        index = self.cups.index(1)
        if index < len(self.cups) - 1:
            return str(self)[index + 1:] + str(self)[:index]
        else:
            return str(self)[:-1]

    def insertAfter(self, n, numberList):
        index = self.cups.index(n)
        if index == len(self.cups) - 1:
            self.cups.extend(numberList)
        else:
            nextIndex = index + 1
            after = self.cups[nextIndex:]
            before = self.cups[:nextIndex]
            if before is not None:
                before.extend(numberList)
                self.cups = before
            else:
                self.cups = numberList
            if after is not None:
                self.cups.extend(after)

    def findLowerOrWarpAround(self, n=None):
        if n is None:
            n = self.currentCup
        sortedList = self.cups.copy()
        sortedList.sort()
        index = sortedList.index(n)
        if index == 0:
            return sortedList[len(sortedList) - 1]
        else:
            return sortedList[index - 1]


def main():
    input = "916438275"
    cups = CupList(input)
    for turn in range(100):
        removedCups = cups.extract(cups.getNext(), 3)
        destinationCup = cups.findLowerOrWarpAround()
        cups.insertAfter(destinationCup, removedCups)
        cups.advanceCurrentCup()
    print(cups.printFrom1())


main()
