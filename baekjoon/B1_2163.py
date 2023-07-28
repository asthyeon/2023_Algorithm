import sys
sys.stdin = open("input.txt", "r")

# N, M 입력 받기
N, M = map(int, input().split())

# 초콜릿 조각 부수는 횟수
print((N * M) - 1)



