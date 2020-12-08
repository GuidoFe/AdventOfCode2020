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
    def __init__(self, command, val, pos):
        self.command = command
        self.val = val
        self.wasRead = False
        self.pos = pos
        if command == Command.ACC:
            self.hasBeenToggled = -1
        else:
            self.hasBeenToggled = 0
    def __str__(self):
        return str(self.pos)
    def __repr__(self):
        return "{com="+str(self.command)+", val="+str(self.val)+", wasR="+str(self.wasRead)+", pos="+str(self.pos)+"}"

def toggleCommand(line):
    if line.command == Command.JMP:
        line.command = Command.NOP
    elif line.command == Command.NOP:
        line.command = Command.JMP

def findBug(code):
    cursor = 0
    stack = []
    toggledIndex = -1
    hasBeenResetted = False
    while True:
        if cursor == len(code):
            return stack[toggledIndex].pos
        if cursor > len(code) or code[cursor].wasRead:
            toggleCommand(stack[toggledIndex])
            for i in range(len(stack)-1, toggledIndex, -1):
                stack[i].wasRead = False
                stack.pop()
            stack[toggledIndex].wasRead = False
            hasBeenResetted = True
            cursor = stack[toggledIndex].pos
            stack.pop()
            toggledIndex = -1
        else:
            line = code[cursor]
            stack.append(line)
            line.wasRead = True
            if line.command == Command.ACC:
                cursor += 1
            elif line.command == Command.JMP or line.command == Command.NOP:
                if toggledIndex == -1:
                    if hasBeenResetted:
                        hasBeenResetted = False
                    else:
                        toggleCommand(line)
                        toggledIndex = len(stack) - 1
                if line.command == Command.JMP:
                    cursor += code[cursor].val
                else:
                    cursor += 1


def resetCode(code):
    for e in code:
        e.wasRead = False

def main():
    f = open("input")
    acc = 0
    code = []
    for line in f:
        line = line.strip()
        s1, s2 = line.split(" ")
        command = Command.fromString(s1)
        if command != Command.ERR:
            code.append(Line(command, int(s2), len(code)))
        else:
            print(s1 + " is not a valid command")
            exit(1)
    print("Bug found at line " + str(findBug(code)))
    resetCode(code)
    cursor = 0
    acc = 0
    while True:
        if cursor == len(code):
            break;
        if code[cursor].wasRead or cursor > len(code):
            print("Error: loop")
            exit(1)
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
