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

# x, y 위치 바꾸기
for i in range(N):
    location[i][0], location[i][1] = location[i][1], location[i][0]

# 정렬
location.sort()

# y, x 위치 바꾸기
for j in range(N):
    location[j][0], location[j][1] = location[j][1], location[j][0]

# 출력
for k in range(N):
    print(*location[k])