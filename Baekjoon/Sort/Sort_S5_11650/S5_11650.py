import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 좌표 정렬하기
'''

# 점의 개수 N
N = int(input())

# 좌표 받기
location = []
for _ in range(N):
    location.append(list(map(int, input().split())))

# 정렬하기
location.sort()

# 출력
for i in range(N):
    print(*location[i])