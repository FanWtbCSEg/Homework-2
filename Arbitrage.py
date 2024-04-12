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
new_balance = 0
path = []
max_path = []
ans = []
max = 0.0
visitornot = {}
def dfs(label, balance):
    global max, max_path
    if (visitornot["tokenB"] == 1):
        if(max < balance):
            max = balance
            max_path = path[:]
    else:
        for next in tokens:
            if (visitornot[next] == 0  and label != next):
                visitornot[next] = 1
                path.append(next)
                dfs(next, 997*balance*liquidity[(label, next)][1]/(1000 * liquidity[(label, next)][0]+ 997 * balance))
                visitornot[next] = 0
                path.pop()
for i in tokens:
    visitornot[i] = 0
dfs("tokenB", 5)
ans.append("tokenB")

now = 5
temp = "tokenB"
for i in max_path:
    now = ((997*now*liquidity[(temp, i)][1])/(1000 * liquidity[(temp, i)][0]+997*now))
    if(now > 20):
        break
    temp = i
print('tokenB->',end='')
for i in range(len(max_path)-1):
    print(max_path[i], end = '->')
print('tokenB, tokenB balance=',end = '')
print(now,'.',sep='')