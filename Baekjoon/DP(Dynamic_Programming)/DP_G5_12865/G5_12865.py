import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 무게에 맞는 최대 가치 구하기
@ 풀이
(1) dp로 풀기
(2) 2차원 배열로 무게 기준으로 풀기(가치를 최대한 담고, 담기전과 담은 후를 비교하기)
    무게 0  1  2  3  4  5  6  7
물품
0        0  0  0  0  0  0  0  0
6 13     0  0  0  0  0  0  13 13
4 8      0  0  0  0  8  8  13 13
3 6      0  0  0  6  8  8  13 14
5 12     0  0  0  6  8  12 13 14
"""


# dp 함수
def dp(N, K, WV_list):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for x in range(1, N + 1):
        for y in range(1, K + 1):
            # 무게가 물품보다 더 크다면(배낭에 공간이 남는다면)
            if y >= WV_list[x][0]:
                # 이전 물품을 넣었을 때와 이전에 물품을 안넣었을 때에 지금 물품을 넣는 것과 비교
                dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - WV_list[x][0]] + WV_list[x][1])
            # 무게가 더 작다면(배낭에 공간이 없다면)
            else:
                # 이전 물품을 넣었을 때와 같음
                dp[x][y] = dp[x - 1][y]

    return dp[N][K]

# 물품의 수: N, 버틸 수 있는 무게: K
N, K = map(int, input().split())

# 물건의 무게: W, 물건의 가치: V
WV_list = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    WV_list.append((W, V))

print(dp(N, K, WV_list))