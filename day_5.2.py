with open(r"C:\Users\cp\Desktop\AoC-24\inputs\input_5.txt") as source:
    inp = source.read()


def middle_of_update(y,r):
    new_rules = r
    m = 0
    for i in range(len(y)):
        n = 0
        for j in range(len(y)):
            if i == j:
                pass
            else:
                if i < j:
                    if y[i]+'|'+y[j] in new_rules:
                        n += 1
                    else:
                        if y[j]+'|'+y[i] not in new_rules:
                            n += 1
                elif i > j:
                    if y[j]+'|'+y[i] in new_rules:
                        n += 1
                    else:
                        if y[i]+'|'+y[j] not in new_rules:
                            n += 1
        if n == (len(y)-1):
            m += 1
    if m == len(y):
        return int(y[len(y)//2])
    else:
        return 0


def sol(v):
    rules = v.split("\n\n")[0]
    updates = v.split("\n\n")[1]
    new_updates = [i.split(",") for i in updates.splitlines()]
    new_rules = rules.splitlines()
    ans = 0
    for i in new_updates:
        ans += middle_of_update(i,new_rules)
    return ans


test = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''


def test_sol():
    assert sol(test) == 143


test_sol()
print(sol(inp))
