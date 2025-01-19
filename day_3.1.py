import re

with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_3.txt") as source:
    inp = source.read()


def multiply(x, y):
    return x*y


def sol(v):
    ans = 0
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    l = pattern.findall(v)
    for z in l:
        a = z[4:-1].split(",")
        ans += multiply(int(a[0]), int(a[1]))
    return ans


test = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''


def test_sol():
    assert sol(test) == 161


test_sol()
print(sol(inp))
