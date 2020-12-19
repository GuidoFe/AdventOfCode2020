import math


def invmod(a, m):
    g, x, y = ExtendedEuclid(a, m)
    return x % m


def ChineseRemainderGauss(n, N, a):
    result = 0

    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = N // ni
        result += ai * bi * invmod(bi, ni)

    return result % N


def ExtendedEuclid(x, y):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while y > 0:
        q, x, y = math.floor(x / y), y, x % y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return q, x0, y0  # gcd and the two coefficients


class bus:
    def __init__(self, b, id, xo, m):
        self.id = int(id)
        self.b = int(b)
        self.xo = int(xo)
        self.k = 0
        self.m = int(m)
        self.current = int(id * (xo + m * self.k) - b)

    def increment(self):
        self.k += 1
        self.current = self.id * (self.xo + self.m * self.k) - self.b


def main():
    f = open("input")
    f.readline()
    line = f.readline().strip().split(",")
    busses = []
    for e in line:
        if e != "x":
            busses.append(int(e))
        else:
            busses.append(0)
    n = []
    N = 1
    a = []
    for i in range(0, len(busses)):
        if busses[i] != 0:
            a.append(-i)
            n.append(busses[i])
            N = N * busses[i]
    print(ChineseRemainderGauss(n, N, a))


main()
