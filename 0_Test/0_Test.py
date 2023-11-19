import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 센서
[출력: K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값 출력]
1. 고속도로 위에 최대 K개의 집중국 세우기
2. N개의 센서가 적어도 하나의 집중국과는 통신해야함
3. 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 함
4. 집중국의 수신가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없음
@ 풀이
(1) 집중국으로 묶기, 각 거리 구하기
- [1 3 6 6 7 9]
    2 3 0 1 2
- [1 3] [6 6 7 9]: 5
    2       1 2

- [3 6 7 8 10 12 14 15 18 20]
    3 1 1 2  2  2  1  3  2
- [3] [6 7 8] [10 12] [14 15] [18 20]: 7
        1 1      2       1       2
(2) 각 센서의 거리가 큰 값들 사이에는 집중국을 두지 않는다
(3) 거리 값이 큰 것들은 제외하기
"""

# 센서 수 N
N = int(input())
# 집중국 수
K = int(input())
# N 개의 센서의 좌표
locations = list(map(int, input().split()))
# 정렬
locations.sort()

# 각 센서간 거리 구하기
distances = []
for i in range(N - 1):
    distances.append(locations[i + 1] - locations[i])
# 정렬
distances.sort()
# 거리 값이 큰 것은 제외(집중국 수만큼 제외)
print(sum(distances[:N - K]))

# print(locations)
# print(distances)