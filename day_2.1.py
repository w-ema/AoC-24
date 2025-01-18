with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_2.txt") as source:
    inp = source.read()


def sol(x):
    ans = 0
    for i in x.splitlines():
        levels = [int(y) for y in i.split(" ")]
        if all([levels[j] - levels[j - 1] > 0 and levels[j] - levels[j - 1] < 4 for j in range(1, len(levels))]):
            ans += 1
        elif all([levels[j] - levels[j - 1] < 0 and levels[j] - levels[j - 1] > -4 for j in range(1, len(levels))]):
            ans += 1
    return ans


test = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def test_sol():
    assert sol(test) == 2


test_sol()
print(sol(inp))