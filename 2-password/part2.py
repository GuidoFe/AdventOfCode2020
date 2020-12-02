import sys
import math

def main():
    try:
        f = open(sys.argv[1])
    except OSError as e:
        print("Error: can't find or read file")
        exit(1)
    right = 0
    tot = 0
    for line in f:
        tot += 1
        policyPositions, policyLetter, password = line.split(" ")
        position1, position2 = policyPositions.split("-")
        policyLetter = policyLetter.strip(":")
        has1 = password[int(position1)-1] == policyLetter
        has2 = password[int(position2)-1] == policyLetter
        if has1 != has2:
            right += 1
    print("Valid passwords: " + str(right) + "/" + str(tot))

main()
