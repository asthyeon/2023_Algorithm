import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 체인의 개수와 각각의 체인의 길이가 주어지면 하나의 긴 체인으로 모든 체인을 묶기 위해 열고 닫아야할 최소한의 고리 수
1. N 개의 체인 존재
2. 각각의 체인은 몇 개의 고리로 연결, 각각의 고리는 최대 두 개의 인접한 고리를 가질 수 있음
3. 각각의 고리는 열고 닫을 수 있음
4. 체인을 분리하거나 두 체인을 연결하여 하나의 긴 체인으로 만들 수 있음
5. 가능한한 적은 고리를 열고 닫아서 모든 체인을 하나의 긴 체인으로 연결하기
@ 풀이
(1) 가장 짧은 체인부터 처리
(2) 가장 짧은 체인을 열기 
"""

# 체인의 개수 N
N = int(input())
# 체인의 길이 N 개의 양의 정수
chains = list(map(int, input().split()))
# 오름차순으로 정리
chains.sort()
# 고리를 연 횟수
ring = 0

# 각 체인을 짧은 것부터
for chain in chains:
    # 체인의 길이가 0이 될 때까지 반복
    while chain > 0:
        # 고리 1개를 열고
        chain -= 1
        # 체인을 1개 연결
        N -= 1
        # 고리 연 횟수 + 1
        ring += 1
        # 다 연결되었다면 반복 종료
        if N == 1:
            break
    # 체인이 다 연결되지 않았다면 해당하는 체인은 0이 되었으므로 -1
    if N != 1:
        N -= 1
    # 체인이 다 연결되었다면 반복 종료
    if N == 1:
        break

print(ring)