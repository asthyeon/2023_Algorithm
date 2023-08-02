import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 개의 행, M 개의 열
N, M = map(int, input().split())
# 배열 형성
arr = [list(map(str, input().split())) for _ in range(N)]
# 색칠한 횟수의 최솟값
min_count = 1000

# 배열 내에 체스판 형성
for i in range(N - 7):
    for j in range(M - 7):
        # 색칠한 횟수 초기화
        count_B = 0
        count_W = 0
        # 체스판 자르기(8x8)
        for row in range(i, 8 + i):
            for col in range(j, 8 + j):
                # 인덱스가 짝수라면
                if (row + col) % 2 == 0:
                    # 블랙으로 시작할 때 칠하는 횟수 계산
                    if arr[row][col] != 'B':
                        count_B += 1
                    # 화이트일 때 칠하는 횟수 계산
                    if arr[row][col] != 'W':
                        count_W += 1
                # 인덱스가 홀수라면
                else:
                    # 블랙으로 시작할 때 칠하는 횟수 계산
                    if arr[row][col] != 'B':
                        count_W += 1
                    # 화이트로 시작할 때 칠하는 횟수 계산
                    if arr[row][col] != 'W':
                        count_B += 1
        # 더 적게 칠한 횟수로 최솟값 바꿔주기
        if count_B > count_W:
            if min_count > count_W:
                min_count = count_W
        else:
            if min_count > count_B:
                min_count = count_B

print(min_count)