with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_6.txt") as source:
    inp = source.read()


def sol(x):
    t = [[z.split() for z in y] for y in x.splitlines()]
    new_t = t.copy()
    h = len(t)
    w = len(t[0])
    direct = [["^"], [">"], ["v"], ["<"]]
    a = 0
    b = 0
    i = 0
    for j in range(h):
        for k in range(w):
            if t[j][k] in direct:
                start_point = t[j][k]
                a = j
                b = k
                i = direct.index(start_point)
    while 0 <= a < h and 0 <= b < w:
        if i == 0:
            step = [0, -1]
        elif i == 1:
            step = [1, 0]
        elif i == 2:
            step = [0, 1]
        else:
            step = [-1, 0]
        new_a = int(a + step[1])
        new_b = int(b + step[0])
        if 0 <= new_a < h and 0 <= new_b < w:
            if t[new_a][new_b] == ['#']:
                i += 1
                if i == 5:
                    i = 0
            else:
                a = new_a
                b = new_b
                new_t[a][b] = ['X']
        else:
            break
    co = 0
    for d in new_t:
        for e in d:
            if e == ['X']:
                co += 1
    return co


test = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


def test_sol():
    assert sol(test) == 41


test_sol()
print(sol(inp))
