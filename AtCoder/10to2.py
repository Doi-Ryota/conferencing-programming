N = int(input()) # 入力部分
answer = ""

while N >= 1:
	if N % 2 == 0:
		answer = "0" + answer
	if N % 2 == 1:
		answer = "1" + answer
	N = N // 2

print(answer) # 出力部分
