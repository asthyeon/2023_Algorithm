import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마라톤
[출력: 체크포인트 1개를 건너뛰고 달릴 수 있는 최소 거리 출력]
1. 체크포인트를 순서대로 방문후 N번에서 끝나야 마라톤이 끝
2. 체크포인트를 1개 건너뛸 수 있음(1번, N번 제외)
3. 택시거리: (x1, y1)과 (x2, y2)의 거리 = |x1 - x2| + |y1 - y2|
@ 풀이
(1) 체크포인트 하나씩 빼보고 거리 계산하기 => 시간초과
(2) 거리들을 먼저 계산해놓고 이용
"""


# 최소 거리 계산 함수
def calculate(skip, total):
    global answer
    # 건너뛴 체크포인트를 전체 거리에서 제외
    total -= distances[skip] + distances[skip + 1]
    # 건너뛴 체크포인트 재계산
    total += abs(checkpoints[skip - 1][0] - checkpoints[skip + 1][0]) + abs(checkpoints[skip - 1][1] - checkpoints[skip + 1][1])
    # 최소 거리 비교 후 교체
    if answer > total:
        answer = total


# 체크포인트 수 N
N = int(input())
# 체크포인트 좌표
checkpoints = []
for _ in range(N):
    x, y = map(int, input().split())
    checkpoints.append((x, y))

# 미리 거리들을 구해놓기
distances = [0]
for i in range(N - 1):
    dist = abs(checkpoints[i][0] - checkpoints[i + 1][0]) + abs(checkpoints[i][1] - checkpoints[i + 1][1])
    distances.append(dist)
# 전체 거리
total = sum(distances)
# 최소 거리 구하기
answer = 10e9
for skip in range(1, N - 1):
    calculate(skip, total)

print(answer)