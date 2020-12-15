import sys
def main():
    requests=[2020, 30000000]
    currentRequest = 0
    input = "1,20,11,6,12,0"
    history = {}
    last = ""
    for i, e in enumerate(input.split(",")):
        last = e
        history[e] = i+1
    for i in range(len(history), requests[len(requests)-1]):
        if last in history:
            prev = history[last]
            history[last] = i
            last = str(i-prev)
        else:
            history[last] = i
            last = "0"
        if i +1 == requests[currentRequest]:
            print("Last at turn "+ str(requests[currentRequest])+": "+str(last))
            currentRequest += 1

main()
