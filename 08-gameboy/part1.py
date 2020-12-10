from enum import Enum

class Command(Enum):
    ACC = 0
    JMP = 1
    NOP = 2
    ERR = -1

    @staticmethod
    def fromString(s):
        if s == "acc":
            return Command.ACC
        elif s == "jmp":
            return Command.JMP
        elif s == "nop":
            return Command.NOP
        else:
            return Command.ERR

class Line:
    def __init__(self, command, val):
        self.command = command
        self.val = val
        self.wasRead = False

def main():
    f = open("input")
    acc = 0
    code = []
    for line in f:
        line = line.strip()
        s1, s2 = line.split(" ")
        command = Command.fromString(s1)
        if command != Command.ERR:
            code.append(Line(command, int(s2)))
        else:
            print(s1 + " is not a valid command")
            exit(1)
    cursor = 0
    while True:
        if cursor >= len(code):
            break;
        if code[cursor].wasRead:
            break;
        else:
            code[cursor].wasRead = True
        if code[cursor].command == Command.ACC:
            acc += code[cursor].val
            cursor += 1
        elif code[cursor].command == Command.JMP:
            cursor += code[cursor].val
        else:
            cursor += 1
    print("ACC = " + str(acc))

main()
