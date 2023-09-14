import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# K를 만드는 동전 개수의 최솟값 구하기
"""

# 동전 수 N, 가치의 합 K
N, K = map(int, input().split())

# 동전 리스트
coins = []
for _ in range(N):
    coins.append(int(input()))

# 역순 정렬
coins.sort(reverse=True)

# 카운트
cnt = 0
for coin in coins:
    cnt += K // coin
    K = K % coin
    if K == 0:
        break

print(cnt)