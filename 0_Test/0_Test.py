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
(1) N 이 2 일 때는 고리를 1개만 열면됨
(2) N 이 3 이상일 때
 - 기본적으로 N - 1개 필요
 - 
"""

# 체인의 개수 N
N = int(input())
# 체인의 길이 N 개의 양의 정수
chains = list(map(int, input().split()))
# 오름차순으로 정리
chains.sort()

if N == 2:
    print(N - 1)
else:
    # 고리의 합
    ring = 0
    cnt = 1
    # 고리 갯수가 적은 것 확인
    for chain in chains:
        if chain == 1:
            ring += 2
            cnt += 1
        elif chain <=
