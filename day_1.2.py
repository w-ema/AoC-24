with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_1.txt") as source:
    inp = source.read()


def sol(x):
    left = list()
    right = list()

    for i in x.splitlines():
        left.append(i.split("   ")[0])
        right.append(i.split("   ")[1])

    left.sort()
    right.sort()

    ans = 0
    for i in range(len(left)):
        ans += int(left[i])*right.count(left[i])
    return ans


test = '''3   4
4   3
2   5
1   3
3   9
3   3'''


def test_sol():
    assert sol(test) == 31


test_sol()
print(sol(inp))