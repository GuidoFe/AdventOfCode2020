import sys

def main():
    f = open("input")
    line = f.readline()
    width = len(line.strip())
    f.seek(0)
    height=0
    for line in f:
        if len(line)>1:
            height += 1
    f.seek(0)
    cursor = 0
    count = 0
    for i in range(height):
        line = f.readline()
        if line[cursor] == '#':
            count += 1
        # +1 to start the array at 1
        cursor = ((cursor + 1 + 3) % (width)) - 1
        if cursor < 0:
            cursor = width + cursor
    print("Count: {}".format(count))
main()
