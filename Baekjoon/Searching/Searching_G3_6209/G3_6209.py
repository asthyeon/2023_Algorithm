import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 학생들이 점프하는 최소거리의 최댓값 구하기
1. 돌섬과 탈출구 사이 총 n 개의 작은 돌섬 존재
2. 돌섬들 중 m 개를 제거하여 각 돌섬을 점프한 거리의 최솟값을 최대한 크게 하려고 함
3. 학생들은 탈출 시 n-m 개의 모든 돌섬을 밟으면서 탈출해야함
4. 돌섬 - 탈출구 거리: d
@ 풀이
(1) 이분 탐색으로 풀기
(2) 거리 기준
"""


# 이분탐색 함수
def binary_search(distances):
    start = 0
    end = d
    # 정답 거리
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        # 돌을 제거한 횟수
        cnt = 0
        # 현재 위치
        now = 0
        for i in range(1, len(distances)):
            # 다음 위치
            after = distances[i]
            dist = after - now
            # 지난 거리가 기준값보다 크다면 위치 변경
            if dist >= mid:
                now = after
            # 위치가 바뀌지 않으면 돌을 제거한 횟수 +1
            else:
                cnt += 1

        if cnt > m:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer


# 거리 d, 돌섬 수 n, 제거가능 돌섬 수 m
d, n, m = map(int, input().split())
# 각 돌섬들의 거리(시작 위치 미리 넣기)
distances = [0]
for _ in range(n):
    distance = int(input())
    distances.append(distance)
# 마지막 위치 넣기
distances.append(d)
# 돌섬 오름차순 정렬
distances.sort()

print(binary_search(distances))