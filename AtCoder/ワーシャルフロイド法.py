# https://atcoder.jp/contests/abc079/tasks/abc079_d
# 二次元のダイクストラ
for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
