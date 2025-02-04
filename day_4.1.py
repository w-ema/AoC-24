with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_4.txt") as source:
    inp = source.read()

checked = []


def tab(x):
    result = []
    for i in x.splitlines():
        row = []
        for j in i:
            row.append(j)
        result.append(row)
    return result


def check(x):
    if (x[0] == 'X' and x[1] == 'M' and x[2] =='A' and x[3] == 'S'):
        return True
    elif (x[3] == 'X' and x[2] == 'M' and x[1] =='A' and x[0] == 'S'):
        return True
    else:
        return False


def positions_to_check(x,y):
    result = [[[x, y], [x+1, y], [x+2, y], [x+3, y]],
              [[x, y], [x, y+1], [x, y+2], [x, y+3]],
              [[x - 3, y], [x - 2, y], [x - 1, y], [x, y]],
              [[x, y - 3], [x, y- 2], [x, y-1], [x, y]],
              [[x, y], [x+1,y+1], [x+2,y + 2], [x+3, y+3]],
              [[x-3, y-3], [x-2, y-2], [x-1,y-1], [x, y]],
              [[x, y], [x + 1, y - 1], [x + 2, y - 2], [x + 3, y - 3]],
              [[x - 3, y + 3], [x - 2, y + 2], [x - 1, y + 1], [x, y]]]
    return [z for z in result if z not in checked]


def sol(v):
    ans = 0
    xmas = []
    global checked
    t_inp = tab(v)
    for i in range(len(t_inp)):
        for j in range(len(t_inp[0])):
            if t_inp[i][j] == "X":
                position_to_check = positions_to_check(i,j)
                for k in position_to_check:
                    word = []
                    for l in k:
                        if (l[0]>=0 and l[1]>=0 and l[0]<len(t_inp) and l[1]<len(t_inp[0])):
                            word.append(t_inp[l[0]][l[1]])
                    if len(word) == 4:
                        if check(word):
                            ans += 1
                            xmas.append(k)
                checked.extend(position_to_check)
    checked = []
    return ans


test = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''


def test_sol():
    assert sol(test) == 18


test_sol()
print(sol(inp))
