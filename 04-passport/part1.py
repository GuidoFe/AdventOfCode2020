#!/usr/local/bin/python3

def checkValidity(passport, requiredKeys):
    isValid = True
    # Check the presence of the required keys:
    for required in requiredKeys:
        if required not in passport:
            isValid = False
            break
    return isValid


def main():
    f = open("input")
    requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = {}
    count = 0
    for line in f:
        # If the parsing of a passport is terminated:
        if len(line.strip()) == 0 and len(passport) != 0:
            if checkValidity(passport, requiredKeys):
                count += 1
            # Reset passport
            passport = {}
        else:
            couples = line.split(" ")
            for couple in couples:
                key, value = couple.split(":", 1)
                passport[key] = value
    # Check if the last passport has been parsed
    if len(passport) != 0 and checkValidity(passport, requiredKeys):
        count += 1
    print(count)


main()
