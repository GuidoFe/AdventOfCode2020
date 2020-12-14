def main():
    f = open("input")
    earliest = int(f.readline().strip())
    l = f.readline().strip().split(",")
    busses = []
    for e in l:
        if e != "x":
            busses.append(int(e))
    modules = list(map(lambda e: (e, e-(earliest % e)), busses))
    modules.sort(key=lambda e: e[1])
    print("First avaiable bus: " + str(modules[0][0])+", you must wait " + str(modules[0][1])+ " minutes")
    print("Answer: " + str(modules[0][0]*modules[0][1]))


main()
