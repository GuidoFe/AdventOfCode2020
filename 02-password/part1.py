import sys


def main():
    try:
        f = open(sys.argv[1])
    except OSError:
        print("Error: can't find or read file")
        exit(1)
    right = 0
    tot = 0
    for line in f:
        tot += 1
        policyNumbers, policyLetter, password = line.split(" ")
        min, max = policyNumbers.split("-")
        policyLetter = policyLetter.strip(":")
        if int(min) <= password.count(policyLetter) <= int(max):
            right += 1
    print("Valid passwords: " + str(right) + "/" + str(tot))


main()
