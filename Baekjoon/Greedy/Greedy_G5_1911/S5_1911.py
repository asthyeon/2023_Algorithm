import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 물웅덩이를 덮기 위한 널빤지들의 최소 개수 구하기
1. 입력으로 주어지는 웅덩이는 겹치지 않음
@ 풀이
(1) 한번 해보기
위치 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
웅덩 0 0 0 0 0     0 0 0 0   0 0 0 0 
널빤 - - - - - -   - - - - - - - - -
"""

# 웅덩이 수 N, 널빤지의 길이 L
N, L = map(int, input().split())
# 웅덩이의 정보
pools = []
for _ in range(N):
    # 웅덩이 위치(s ~ e)
    s, e = map(int, input().split())
    pools.append((s, e))

# 널빤지 설치하기
# 정렬
pools.sort()
# 널빤지 수
plank = 0
# 웅덩이 위치
idx = 0
# 널빤지가 설치된 마지막 위치
install = -1
while idx < N:
    # print(f'# {idx}')
    # 설치해야 하는 길이
    length = pools[idx][1] - pools[idx][0]
    # print(f'original_length: {length}')

    # 웅덩이의 시작 위치가 현재 널빤지가 설치된 길이보다 이전이라면
    if pools[idx][0] <= install:
        # 설치해야 하는 길이 갱신
        length = pools[idx][1] - install - 1

    # 설치해야 하는 길이가 음수거나 0이라면 넘기기(설치해야 할 필요 X)
    if length <= 0:
        idx += 1
        # print(f'length: {length}')
        # print(f'pools_now: {pools[idx - 1]}')
        # print(f'pools: {pools}')
        # print(f'install: {install}')
        # print(f'plank: {plank}')
        continue

    # 웅덩이 길이가 딱 나뉘어질 때
    if length % L == 0:
        # 나눈 몫만큼 널빤지 수 더하기
        plank += length // L
        # 널빤지가 설치된 마지막 위치 갱신
        install = pools[idx][1] - 1
        # 다음 웅덩이로 넘어가기
        idx += 1
        # print(f'length: {length}')
        # print(f'pools_now: {pools[idx - 1]}')
        # print(f'pools: {pools}')
        # print(f'install: {install}')
        # print(f'plank: {plank}')
        continue
    else:
        # 나눈 몫 + 1만큼 널빤지 수 더하기
        plank += (length // L) + 1
        # 널빤지가 설치된 마지막 위치 갱신
        install = max(pools[idx][0] - 1, install) + (L * ((length // L) + 1))
        # 다음 웅덩이로 넘어가기
        idx += 1
        # print(f'length: {length}')
        # print(f'pools_now: {pools[idx - 1]}')
        # print(f'pools: {pools}')
        # print(f'install: {install}')
        # print(f'plank: {plank}')
        continue

print(plank)