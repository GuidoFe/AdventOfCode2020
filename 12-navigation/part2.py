import math
import sys
import matplotlib.pyplot as plt

distance = 0

class waypoint:
    def __init__(self):
        self.x = 10
        self.y = 1

    # 0 = N, 90 = E, S = 180, W = 270
    def move(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "E":
            self.x += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "W":
            self.x -= distance

    def rotateBy(self, angle):
        if self.x != 0:
            currentAngle = math.atan(self.y/self.x)
            if self.x<0:
                currentAngle += math.pi
        else:
            currentAngle = math.copysign(math.pi / 2, self.y)
        newAngle = currentAngle+math.radians(-angle)
        r = math.sqrt(self.x**2 + self.y**2)
        self.x = round(r * math.cos(newAngle))
        self.y = round(r * math.sin(newAngle))




class boat:
    def __init__(self):
        self.x=0
        self.y=0
        self.rotation = 90
        self.w = waypoint()


    def forward(self, times):
        global distance
        for i in range(times):
            self.x += self.w.x
            self.y += self.w.y
            distance += math.sqrt((self.w.x*0.0283333)**2+(self.w.y*0.0308333)**2)


# Directions are always 0 = N, 90 = E, S = 180, W = 270

def main():
    f = open("input")
    b = boat()
    x = [0]
    y = [0]
    for l in f:
        l = l.strip()
        command = l[0]
        value = int(l[1:])
        if command == "F":
            b.forward(value)
            x.append(b.x)
            y.append(b.y)
        elif command == "L":
            b.w.rotateBy(-value)
        elif command == "R":
            b.w.rotateBy(value)
        elif len(l) > 1:
            b.w.move(command, value)
        #sys.stdin.readline()

    plt.plot(x, y, linestyle="--", color="#317157", linewidth=1)
    ax = plt.gca()
    ax.set_facecolor("#70B99C")
    plt.plot(0,0, marker="o", markersize=6, markerfacecolor="r", markeredgewidth=0)
    plt.plot(x[len(x)-1], y[len(y)-1], marker="x", markersize=8, markeredgecolor="r", markeredgewidth=2)

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title('Ferry Journey')
    print("Answer: " + str(abs(b.x)+abs(b.y)))
    print("Distance from start to finish, as the crow flies: " + str(math.sqrt((b.x*0.0283333)**2 + (b.y*0.0308333)**2)))
    print("Total distance: "+str(distance)+" Km")
    plt.show()

main()
