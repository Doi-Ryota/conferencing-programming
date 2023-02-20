//以下の数え上げ
res = 0
int right = 0;
for left in range(n)
    while (right < n and sum + a[right] <= x):
        /* 実際に right を 1 進める */sum += a[right]
        ++right

    /* break した状態で right は条件を満たす最大なので、何かする */
    ex: res += (right - left)

    /* left をインクリメントする準備 */
    if (right == left) ++right
    else sum -= a[left]


//以上の最小長
res = n+1
int right = 0;
for left in range(n)
    while (right < n and sum + a[right] < x):

        /* 実際に right を 1 進める */
        sum += a[right]
        ++right

    if (sum < x) break // これ以上 left を進めてもダメ

    /* break した状態で right は条件を満たす最大なので、何かする */
    res = min(res,right - left)

    /* left をインクリメントする準備 */
    if (right == left) ++right
    else sum -= a[left]

    //以上でres = n+1なら失敗
