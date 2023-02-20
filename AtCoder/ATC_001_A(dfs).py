h,w = MI()
c = [LS() for i in range(h)]

def dfs(x,y):
    if not(0 <= x < w) or not(0 <= y < h) or c[y][h] == "#": # 壁に当たったり、探索範囲外になった場合はreturn
        return
    if c[y][x] == "g": # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
#for dx,dy in zipのほうがよい

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j # スタート位置

dfs(sx, sy)
print("No")
