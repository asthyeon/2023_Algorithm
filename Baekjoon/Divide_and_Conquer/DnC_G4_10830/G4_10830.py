import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 크기가 N * N인 행렬 A의 B제곱 구하기(A^B의 각 원소를 1,000으로 나눈 나머지 출력)
@ 풀이
(1) 분할 정복으로 풀기
"""


# 분할정복 함수
def dnc(A, B, answer):
    # 더이상 분할이 안된다면
    if B == 1:
        for a in range(N):
            for b in range(N):
                answer[a][b] %= B
        return
    # 짝수일 때
    elif B % 2 == 0:
        for a in range(N):
            for b in range(N):
                num = 0
                for c in range(N):
                    num += answer[a][c] * A[c][b]
                answer[a][b] = num ** 2 * A[]
    # 홀수일 때, 자기 자신을 한 번 더 곱해야함
    else:
        return ((divide(A, B // 2, C) ** 2) * A) % C


# N, B
N, B = map(int, input().split())

# 행렬 A
A = [list(map(int, input().split())) for _ in range(N)]

# 정답 행렬
answer = [[0] * N for _ in range(N)]

print(answer)