
# 入力
N = int(input())

# すべての約数を求め、配列 divisors に入れる
LIMIT = int(N ** 0.5)
divisors = []
for i in range(1, LIMIT + 1):
	if N % i == 0:
		divisors.append(i)
		if i != N // i:
			divisors.append(N // i)

# 小さい順に並べ替え → 出力
divisors.sort()
for i in divisors:
	print(i)
