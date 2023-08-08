import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수 구하기
1. 가로수의 위치는 기준점으로부터 떨어져 있는 거리로 표현
2. 3 <= N <= 100,000
3. 가로수의 위치를 나타내는 정수 1,000,000,000 이하 -> 반복문 사용 불가
'''

# 이미 심어져 있는 가로수의 수
N = int(input())

# 가로수 리스트
trees = []

# N 개의 줄에 각 줄마다 심어져 있는 가로수의 위치
for _ in range(N):
    trees.append(int(input()))

# 각 가로수 차이 중 가장 작은 값
differ = trees[1] - trees[0]
for i in range(1, len(trees)):
    if differ > trees[i] - trees[i - 1]:
        differ = trees[i] - trees[i - 1]

print((trees[-1] // differ) - len(trees) + 1)