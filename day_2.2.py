with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_2.txt") as source:
    inp = source.read()

def level_checker(x):
    s = 0
    if all([x[j] - x[j - 1] > 0 and x[j] - x[j - 1] < 4 for j in range(1, len(x))]):
        s = 1
    elif all([x[j] - x[j - 1] < 0 and x[j] - x[j - 1] > -4 for j in range(1, len(x))]):
        s = 1
    return s

def sol(x):
    ans = 0
    for i in x.splitlines():
        levels = [int(y) for y in i.split(" ")]
        n_ans = level_checker(levels)
        if n_ans == 0:
            shorter_levels = []
            for k in range(len(levels)):
                new_level = levels.copy()
                del new_level[k]
                shorter_levels.append(level_checker(new_level))
            if any(l==1 for l in shorter_levels):
                n_ans = 1
        ans += n_ans
    return ans


test = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def test_sol():
    assert sol(test) == 4


test_sol()
print(sol(inp))