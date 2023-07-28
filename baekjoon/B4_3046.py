import sys
sys.stdin = open("input.txt", "r")

# R1, S 입력 받기
R1, S = map(int, input().split())

# S = (R1 + R2) / 2
# R2 = 2S - R1

# R2 출력
print((2 * S) - R1 )