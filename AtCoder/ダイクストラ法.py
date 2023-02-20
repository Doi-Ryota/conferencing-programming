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

def dijkstra(edges,n):
    node = [INF] * n   #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = [i for i in range(n)]     #ノードの名前を0ノードの数で表す

    while len(node_name) > 0:
        r = node_name[0]

        #最もコストが小さい頂点を探す
        for i in node_name:
            if  node[i] < node[r]:
                r = i   #コストが小さい頂点が見つかると更新

        #最もコストが小さい頂点を取り出す
        min_point = node_name.pop(node_name.index(r))

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新

    return node

if __name__ == '__main__':
    n,m = MI()
    Edges = [[] for i in range(n)]
    for i in range(m):
        a,b,w = MI()
        Edges[a-1].append([b-1,w])
        #無向辺の時
        #Edges[b-1].append([a-1,w])
    print(Edges)
    opt_node = dijkstra(Edges, n)
    print(opt_node)
