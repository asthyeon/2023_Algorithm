import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력하라

# 이미 가진 랜선의 개수: K, 필요한 랜선의 개수: N
K, N = map(int, input().split())

# 랜선 리스트
lans = []

# 각 랜선의 길이 받기
for _ in range(K):
    lans.append(int(input()))

# 이진탐색 함수
def Binarysearch(lans, N):
    # 최소길이
    start = 1
    # 최대길이
    end = max(lans)
    # 이진탐색으로 end (최대 길이를 찾기)
    while start <= end:
        middle = (start + end) // 2
        # 자르고 나온 랜선 수
        lan_count = 0
        # 모든 랜선을 잘라보고
        for lan in lans:
            lan_count += lan // middle
        # 만일 랜선 수가 목표로 하는 수보다 작다면
        if lan_count < N:
            end = middle - 1
        # 만일 랜선 수가 목표로 하는 수보다 크다면
        else:
            start = middle + 1
    print(end)

Binarysearch(lans, N)
