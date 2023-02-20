from collections import deque

def main():
    w, h = map(int, input().split())
    Map = [list(input().split()) for _ in range(h)]

    dist = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if Map[i][j] == "s":
                dist[i][j] = 0
                sy = i
                sx = j
            elif Map[i][j] == "g":
                gy = i
                gx = j

    ops = [[-1,0], [1,0], [0,-1], [0,1]]

    deq = deque()
    deq.append([sy, sx])
    while deq:
        d = deq.popleft()
        d_r = d[0]
        d_c = d[1]

        for op in ops:
            op_r = op[0]
            op_c = op[1]

            row = d_r + op_r
            col = d_c + op_c

            # 範囲外
            if row < 0 or h <= row or col < 0 or w <= col:
                continue

            # 壁
            if Map[row][col] == '1':
                continue

            # 探索済み
            if dist[row][col] != -1:
                continue

            dist[row][col] = dist[d_r][d_c] + 1
            deq.append([row, col])
    if dist[gy][gx] == -1:
        print("Fail")
    else:
        print(dist[gy][gx])

if __name__ == '__main__':
    main()
