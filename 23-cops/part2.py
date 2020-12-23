# The index of the cups array inside the class is completely transparent
import sys


def main():
    MAX_TURNS = 10000000
    MAX_N = 1000000
    input = "916438275"
    cups = {}
    chars = []
    chars[:0] = input
    prev = MAX_N
    for c in chars:
        n = int(c)
        cups[prev] = n
        prev = n
    for i in range(10, MAX_N + 1):
        cups[prev] = i
        prev = i
    currentCup = int(input[0])
    for turn in range(MAX_TURNS):
        a = currentCup
        pickedCups = []
        for i in range(3):
            a = cups[a]
            pickedCups.append(a)
        cups[currentCup] = cups[pickedCups[2]]
        destinationCup = currentCup - 1
        if destinationCup == 0:
            destinationCup = MAX_N
        while destinationCup in pickedCups:
            destinationCup -= 1
            if destinationCup == 0:
                destinationCup = MAX_N
        cups[pickedCups[2]] = cups[destinationCup]
        cups[destinationCup] = pickedCups[0]
        currentCup = cups[currentCup]
    print(cups[1] * cups[cups[1]])


main()
