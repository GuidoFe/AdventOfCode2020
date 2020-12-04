#!/usr/local/bin/python3

def checkValidity(passport, requiredKeys):
    isValid = True
    #Check the presence of the required keys:
    for req in requiredKeys:
        if not passport.has_key(req):
            isValid = False
            break
        else:
            if req == "byr" and not (1920 <= int(passport[req]) <= 2002):
                isValid = False; break
            elif req == "iyr" and not (2010 <= int(passport[req]) <= 2020):
                isValid = False; break
            elif req == "eyr" and not (2020 <= int(passport[req]) <= 2030):
                isValid = False; break
            elif req == "hgt":
                try:
                    unit = passport[req][-2:]
                    value = int(passport[req][:-2])
                except:
                    isValid = False; break
                if unit == "cm":
                    if not (150 <= value <= 193):
                        isValid = False; break
                elif unit == "in":
                    if not (59 <= value <= 76):
                        isValid = False; break
                else:
                    isValid = False; break
            elif req == "hcl":
                code = passport[req][1:]
                code = code.strip("0123456789abcdef")
                if len(passport[req]) != 7 or passport[req][0] != "#" or len(code) != 0:
                    isValid = False; break
            elif req == "ecl":
                if not passport[req] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    isValid = False; break
            elif req == "pid" and len(passport[req]) != 9:
                isValid = False; break
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
                passport[key] = value.strip()
    # Check if the last passport has been parsed
    if len(passport) != 0 and checkValidity(passport, requiredKeys):
        count += 1
    print(count)

main()
