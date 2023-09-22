import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 자연수 N 과 M 이 주어졌을 때, 아래 조건을 만족하는 길이가 M 인 수열을 모두 구하기
1. 1부터 N 까지 자연수 중에서 중복 없이 M 개를 고른 수열
2. 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력(중복 X)
3. 수열은 사전 순으로 증가하는 순서로 출력
4. 1 <= M <= N <= 8
5. 같은 수를 여러 번 골라도 됨
6. 고른 수열은 비내림차순이어야 함(다음 수가 앞의 수보다 작아서는 안됨)
@ 풀이
(1) 백트래킹으로 풀기
(2) 똑같은 수가 사용된 수열 사용 가능하므로 path 삭제하기
"""


# 백트래킹 함수
def backtracking(sequence, idx):
    # 재귀를 종료하는 기저 조건(수열의 마지막 숫자가 0 보다 클 때 종료(길이가 M 이 될 때))
    if idx == M:
        # 사전순으로 수열을 구성하기 때문에 그대로 출력
        print(*sequence)
        return

    for i in range(1, N + 1):
        if idx >= 1:
            if sequence[idx] < sequence[idx - 1]:
                continue
        sequence[idx] = i
        idx += 1
        backtracking(sequence, idx)
        idx -= 1
        sequence[idx] = 0


# 자연수 N 과 M
N, M = map(int, input().split())
# 수열
sequence = [0] * M
# 수열의 인덱스
idx = 0

# 함수 사용
backtracking(sequence, idx)