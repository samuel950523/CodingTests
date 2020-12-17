# 12852번. 1로 만들기 2


def func(a, b):
    dp[a][0] = dp[b][0] + 1  # 횟수 늘려주기
    for i in range(len(dp[b][1])):
        dp[a][1].append(dp[b][1][i])
    dp[a][1].append(a)


n = int(input())
dp = [[0, []] for _ in range(1000000 + 1)]
# dp = [[0, []] for _ in range(n + 1)] # 런타임에러
dp[0] = [0, [0]]
dp[1] = [1, [1]]
dp[2] = [1, [1, 2]]
dp[3] = [1, [1, 3]]


for i in range(4, n + 1):
    if i % 3 == 0:
        if dp[i // 3][0] <= dp[i - 1][0]:
            func(i, i//3)
        else:
            func(i, i-1)
    elif i % 2 == 0:
        if dp[i // 2][0] <= dp[i - 1][0]:
            func(i, i//2)
        else:
            func(i, i - 1)
    else:
        func(i, i - 1)

# 출력
# dp[n][1].sort(reverse=True)
dp[n][1] = dp[n][1][::-1]
print(dp[n][0])
print(*dp[n][1])
