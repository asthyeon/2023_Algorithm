import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 호 안에 수류탄이야!!
[출력: 중대장 모르게 끝 -> "권병장님, 중대장님이 찾으십니다" 바닥행 -> "엄마 나 전역 늦어질 것 같아"]
1. 수류탄은 욱제와 전우들 사이를 옮겨다님
2. 한 위치에 여러 명의 전우가 서있다면 아무나 받아 다음 전우에게 던질 수 있음
3. 누군가의 팔 힘이 모자라 바닥에 떨어질 수 있음
4. N 번째 전우가 수류탄을 받으면 중대장 모르게 끝
@ 풀이
(1) 수류탄 사거리보다 작은 범위에 전우가 있을 경우 넘기기
"""


# 수류탄 넘기기
def grenade(comrades, distances):
    # 수류탄을 들고 있는 전우
    target = 0
    # 수류탄 범위
    location = 0
    for i in range(1, N):
        # 다음 위치가 범위 안에 있다면
        if location + distances[target] >= comrades[i]:
            if i < N - 1:
                # 현재 범위와 다음 범위 비교하여 큰 값으로 교체
                if comrades[i] + distances[i] > location + distances[target]:
                    target = i
                    location = comrades[i]
        # 다음 위치가 범위 안에 없다면
        else:
            return '엄마 나 전역 늦어질 것 같아'
    # 마지막 위치까지 다 돌았다면
    else:
        return '권병장님, 중대장님이 찾으십니다'


# 전우 수
N = int(input())
# 전우들의 좌표
comrades = list(map(int, input().split()))
comrades.sort()
if N >= 2:
    # 전우들의 사거리
    distances = list(map(int, input().split()))
    # 함수 사용
    print(grenade(comrades, distances))
else:
    print('권병장님, 중대장님이 찾으십니다')