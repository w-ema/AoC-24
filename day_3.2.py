import re

with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_3.txt") as source:
    inp = source.read()


def multiply(x, y):
    return x*y


def sol(v):
    ans = 0
    list_1 = v.split("do()")
    list_2 = []
    list_3 = []
    for l in list_1:
        list_2.append(l.split("don't()")[0])
    pattern3 = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    for i in list_2:
        list_3.extend(pattern3.findall(i))
    for z in list_3:
        a = z[4:-1].split(",")
        ans += multiply(int(a[0]), int(a[1]))
    return ans


test = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''


def test_sol():
    assert sol(test) == 48


test_sol()
print(sol(inp))
