n = I()
s = S()
t = '*atcoder'
dp = collections.Counter()
dp['*'] = 1
for i in range(n):
    if s[i] in t:
        pre = t[t.index(s[i])-1]
        dp[s[i]] = (dp[s[i]]+dp[pre])%MOD1
print(dp['r'])
