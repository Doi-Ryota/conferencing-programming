import sys,math,collections,itertools
from collections import deque,defaultdict
INF = 10**18
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def S(): return input()
def LS(): return list(input().split())
def TS(): return tuple(input().split())
def lcm(a, b): return a * b // math.gcd(a, b)
MOD1 = 10**9+7 #500000004
MOD2 = 998244353 #499122177
sys.setrecursionlimit(10**9)

def bellman_ford(s):
    d = [INF]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for a, b, w in edges:
            if d[b] > d[a]+w:
                d[b] = d[a]+w
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d

n,m = MI() # n:頂点数, w:辺の数
edges = []
for _ in range(m):
    a,b,w = MI() # 始点,終点,コスト
    edges.append([a-1,b-1,w])
    #edges.append([a-1,b-1,w]) #有向グラフでは削除
print(edges)
print(bellman_ford(0))
