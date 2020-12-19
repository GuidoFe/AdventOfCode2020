import math
import matplotlib.pyplot as plt


class boat:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 90

    # Angle in degrees
    def rotateBy(self, angle):
        self.rotation += angle

    # 0 = N, 90 = E, S = 180, W = 270
    def absoluteMove(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "E":
            self.x += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "W":
            self.x -= distance

    def forward(self, distance):
        angle = math.radians(360 - self.rotation + 90)
        self.x += int(distance * math.cos(angle))
        self.y += int(distance * math.sin(angle))
        # Directions are always 0 = N, 90 = E, S = 180, W = 270


def main():
    f = open("input")
    b = boat()
    x = [0]
    y = [0]
    for line in f:
        line = line.strip()
        command = line[0]
        value = int(line[1:])
        if command == "F":
            b.forward(value)
        elif command == "L":
            b.rotateBy(-value)
        elif command == "R":
            b.rotateBy(value)
        else:
            b.absoluteMove(command, value)
        x.append(b.x)
        y.append(b.y)

    plt.plot(x, y, linestyle="--", color="#317157", linewidth=1)
    ax = plt.gca()
    ax.set_facecolor("#70B99C")
    plt.plot(0, 0, marker="o", markersize=6, markerfaceColor="r", markeredgewidth=0)
    plt.plot(x[len(x) - 1], y[len(y) - 1], marker="x", markersize=8,
             markeredgecolor="r", markeredgewidth=2)

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title('Ferry Journey')
    print(abs(b.x) + abs(b.y))
    plt.show()


main()
