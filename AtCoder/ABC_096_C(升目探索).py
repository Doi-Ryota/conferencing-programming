import sys
def I(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().split())
def LI(): return list(map(int,sys.stdin.readline().split()))
def TI(): return tuple(map(int,sys.stdin.readline().split()))
def S(): return sys.stdin.readline()
def LS(): return list(sys.stdin.readline().split())
def TS(): return tuple(sys.stdin.readline().split())
def lcm(a, b): return a * b // gcd(a, b)
def yes(): print("Yes")
def no(): print("No")
MOD1 = 1**9+7 #500000004
MOD2 = 998244353 #499122177
sys.setrecursionlimit(10**9)

H,W = MI()
m = tuple([S() for _ in range(H)])
dX = [0,1,0,-1]
dY = [1,0,-1,0]

def hantei(i,j):
    cnt = 0
    for h in range(4):
        x = i + dX[h]
        y = j + dY[h]
        if x < 0 or H <= x or y < 0 or W <= y: #例外の措置
            continue

//ここから
        if m[x][y] == "#":
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False
//ここまでを変更すれば使える


for i in range(H):
    for j in range(W):
        if m[i][j] == "#":
            a = hantei(i,j)
            if a:
                print("No")
                exit()
print("Yes")
