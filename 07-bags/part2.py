

class Bag:
    def __init__(self, color):
        self.name = color
        self.contains = {}
        self.containedIn = set()

    def __str__(self):
        str1 = ""
        str2 = ""
        for e in self.contains:
            str1 += "#" + str(self.contains[e]) + " " + e +", "
        for e in self.containedIn:
            str2 += e.name + ", "
        if len(str1) == 0:
            str1 = "nothing "
        if len(str2) == 0:
            str2 = "nothing"
        else:
            str2 = str2[:-2]
        return "{}: CONTAINS {}CONTAINED IN {}".format(self.name, str1, str2)

def countBagsInside(bag, dict):
    if len(bag.contains) == 0:
        return 0
    else:
        sum = 0
        for b in bag.contains:
            sum += bag.contains[b] + bag.contains[b] * countBagsInside(dict[b], dict)
        return sum

def main():
    f = open("input")
    bagDict = {}
    for line in f:
        if len(line)>1:
            line = line.replace("\n", "")
            line = line.replace(".", "")
            line = line.replace(" bags", "")
            line = line.replace(" bag", "")
            color, contains = line.split(" contain ")
            if bagDict.has_key(color):
                node = bagDict[color]
            else:
                node = Bag(color)
                bagDict[color]=node
            if contains != "no other":
                for b in contains.split(", "):
                    number, colorContained = b.split(" ", 1)
                    if bagDict.has_key(colorContained):
                        containedNode = bagDict[colorContained]
                    else:
                        bagDict[colorContained] = Bag(colorContained)
                        containedNode = bagDict[colorContained]
                    node.contains[colorContained] = int(number)
                    containedNode.containedIn.add(node)

    print(countBagsInside(bagDict["shiny gold"], bagDict))


main()
