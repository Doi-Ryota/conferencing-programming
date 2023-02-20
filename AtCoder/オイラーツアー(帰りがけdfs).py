
done = [0] * N
ET = []
def dfs(i):
    done[i] = 1
    ET.append(i) # 開始時にリストに追加
    for j in X[i]:
        if done[j]: continue
        dfs(j)
    ET.append(i) # 終了時にもリストに追加

dfs(0)
print("ET =", ET)
