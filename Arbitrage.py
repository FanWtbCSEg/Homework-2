liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenA"): (10, 17),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenA"): (7, 11),
    ("tokenC", "tokenB"): (4, 36),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenA"): (9, 15),
    ("tokenD", "tokenB"): (6, 13),
    ("tokenD", "tokenC"): (12, 30),
    ("tokenD", "tokenE"): (60, 25),
    ("tokenE", "tokenA"): (5, 21),
    ("tokenE", "tokenB"): (3, 25),
    ("tokenE", "tokenC"): (8, 10),
    ("tokenE", "tokenD"): (25, 60),
}

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
balance = 5
path = []
max_path = []
max = 0
visitornot = {}
def count(x, y, z):
    return 997*x*liquidity[(y, z)][1]/(1000 * liquidity[(y, z)][0]+ 997 * x)
def dfs(label, balance):
    global max, max_path
    if (visitornot["tokenB"] == 1 and max < balance):
        max = balance
        max_path = path[:]
    else:
        for next in tokens:
            if (visitornot[next] == 0  and label != next):
                visitornot[next] = 1
                path.append(next)
                dfs(next, count(balance, label, next))
                visitornot[next] = 0
                path.pop()
for i in tokens:
    visitornot[i] = 0
dfs("tokenB", balance)

now = 5
temp = "tokenB"
for i in max_path:
    now = count(now, temp, i)
    if(now > 20):
        break
    temp = i
print('tokenB->',end='')
for i in range(len(max_path)-1):
    print(max_path[i], end = '->')
print('tokenB, tokenB balance=',end = '')
print(now,'.',sep='')