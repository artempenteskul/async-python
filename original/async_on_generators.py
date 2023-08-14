import time


queue = []


def counter():
    c = 0
    while True:
        print(c)
        c += 1
        yield


def printer():
    c = 0
    while True:
        if c % 3 == 0:
            print('Bang!')
        c += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        time.sleep(0.5)  # blocking function


if __name__ == '__main__':
    g1 = counter()
    g2 = printer()

    queue += [g1, g2]

    main()
