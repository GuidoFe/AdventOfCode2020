def main():
    f = open("input")
    # 0 = reading rules for fields, 1 = reading my ticket,
    # 2 = reading other tickets
    status = 0
    validRanges = []
    fieldRanges = {}
    fieldNames = []
    fieldPools = []
    errorRate = 0
    myTicket = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            # If it's reanding the fields ranges
            if status == 0:
                name, rangesStr = line.split(": ")
                ranges = rangesStr.split(" or ")
                fieldNames.append(name)
                fieldRanges[name] = []
                for rangeStr in ranges:
                    minVal, maxVal = map(lambda e: int(e), rangeStr.split("-"))
                    fieldRanges[name].append((minVal, maxVal))
                    if len(validRanges) == 0:
                        validRanges.append((minVal, maxVal))
                    else:
                        for i, m in enumerate(validRanges):
                            if minVal > m[1]:
                                if i == len(validRanges) - 1:
                                    validRanges.append((minVal, maxVal))
                                    break
                                else:
                                    continue
                            elif maxVal < m[0]:
                                validRanges.insert(i, (minVal, maxVal))
                            elif maxVal == m[0]:
                                validRanges[i] = (minVal, m[1])
                            else:
                                newMin = min(minVal, m[0])
                                maxRangeIndex = len(validRanges) - 1
                                for j in range(i + 1, len(validRanges)):
                                    if maxVal > validRanges[j][0]:
                                        if j == len(validRanges) - 1:
                                            maxRangeIndex = j
                                            break
                                        else:
                                            continue
                                    else:
                                        maxRangeIndex = j - 1
                                        break
                                newMax = max(maxVal, validRanges[maxRangeIndex][1])
                                for k in range(maxRangeIndex, i, -1):
                                    validRanges.pop(k)
                                validRanges[i] = (newMin, newMax)
            # If reading my ticket or tickets of someone else
            elif (status == 1 or status == 2) and line != "nearby tickets:" and line != "your ticket:":
                values = list(map(lambda x: int(x), line.split(",")))
                if status == 1:
                    myTicket = values.copy()
                validTicket = True
                # Check if values are possible or if the ticket is not valid
                for v in values:
                    isValid = False
                    for r in validRanges:
                        if r[0] <= v <= r[1]:
                            isValid = True
                            break
                    if not isValid:
                        validTicket = False
                        errorRate += v
                if validTicket:
                    for pos, v in enumerate(values):
                        # If the field for that position has not been found yet
                        if len(fieldPools[pos]) > 1:
                            invalidFields = []
                            # Check for which fields in that position the
                            # current value would not be valid
                            for field in fieldPools[pos]:
                                isFieldPossible = False
                                for i in range(2):
                                    r = fieldRanges[field][i]
                                    if r[0] <= v <= r[1]:
                                        isFieldPossible = True
                                        break
                                if not isFieldPossible:
                                    invalidFields.append(field)
                            # Delete the impossible fields from the pool of
                            # possibilities
                            for f in invalidFields:
                                fieldPools[pos].remove(f)
                            # If there is only one field left in the pool...
                            if len(fieldPools[pos]) == 1:
                                # ... delete that field from the pool of every
                                # other position
                                for k in range(len(fieldPools)):
                                    if k != pos and fieldPools[pos][0] in fieldPools[k]:
                                        fieldPools[k].remove(fieldPools[pos][0])
        elif len(line) == 0:
            if status == 0:
                fieldPools = [fieldNames.copy() for e in range(len(fieldNames))]
            status += 1
    hasBeenChanges = True
    while hasBeenChanges:
        hasBeenChanges = False
        for field in fieldNames:
            foundAt = None
            for pos, pool in enumerate(fieldPools):
                if field in pool:
                    if foundAt is None:
                        foundAt = pos
                    else:
                        foundAt = -1
                        break
            if foundAt > 0:
                for f in fieldPools[foundAt]:
                    if f != field:
                        fieldPools[foundAt].remove(f)
                        hasBeenChanges = True
    print("Error rate:", errorRate)
    prod = 1
    for i, pool in enumerate(fieldPools):
        if len(pool) == 1 and pool[0].split(" ", 1)[0] == "departure":
            prod *= myTicket[i]
    print("Sum of value with departure:", prod)


main()
