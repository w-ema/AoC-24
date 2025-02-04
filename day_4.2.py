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
    if (x[0] == 'M' and x[2] == 'S'):
        return True
    elif (x[0] == 'S' and x[2] == 'M'):
        return True
    else:
        return False


def positions_to_check(x,y):
    result = [[[x-1, y-1], [x, y], [x+1, y+1]],
              [[x-1, y+1], [x, y], [x+1, y-1]]]
    return [z for z in result if z not in checked]


def sol(v):
    ans = 0
    xmas = []
    global checked
    t_inp = tab(v)
    for i in range(len(t_inp)):
        for j in range(len(t_inp[0])):
            if t_inp[i][j] == "A":
                position_to_check = positions_to_check(i,j)
                if_two_are_true = 0
                for k in position_to_check:
                    word = []
                    for l in k:
                        if (l[0]>=0 and l[1]>=0 and l[0]<len(t_inp) and l[1]<len(t_inp[0])):
                            word.append(t_inp[l[0]][l[1]])
                    if len(word) == 3:
                        if check(word):
                            if_two_are_true += 1
                if if_two_are_true == 2:
                    ans += 1
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
    assert sol(test) == 9


test_sol()
print(sol(inp))