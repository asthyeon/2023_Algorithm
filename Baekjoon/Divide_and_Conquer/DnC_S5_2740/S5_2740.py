import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# (N * M 크기의 행렬 A) * (M2 * K 크기의 행렬 B)
"""

# N, M
N, M = map(int, input().split())
# 행렬 A
A = [list(map(int, input().split())) for _ in range(N)]

# M2, K
M, K = map(int, input().split())
# 행렬 B
B = [list(map(int, input().split())) for _ in range(M)]

# 정답 행렬
answer = [[0] * K for _ in range(N)]

# 세로: A의 N
for a in range(N):
    # 가로: B의 K
    for b in range(K):
        num = 0
        # 더하는 횟수(곱한 수들의 수)
        for c in range(M):
            num += A[a][c] * B[c][b]
        answer[a][b] = num

# 정답 출력
for i in range(N):
    print(*answer[i])