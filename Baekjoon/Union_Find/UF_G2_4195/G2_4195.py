import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 두 사람의 친구 네트워크에 몇 명이 있는지 구하기
1. 친구 관계가 생긴 순서대로 주어짐
2. 친구 네트워크: 친구 관계만으로 이동할 수 있는 사이
@ 풀이
(1) 유니온 파인드로 풀기
(2) 친구 관계의 수를 미리 구해놓기
"""


# find 함수
def find(x):
    if net_numbers[x] == x:
        return x
    # 경로 압축
    net_numbers[x] = find(net_numbers[x])
    return net_numbers[x]


# union 함수
def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        net_numbers[y] = x
        # 두 사람의 친구 네트워크에 있는 수를 서로 더하기
        net_counts[x] += net_counts[y]
        return net_counts[x]
    elif x == y:
        return net_counts[x]
    else:
        net_numbers[x] = y
        # 두 사람의 친구 네트워크에 있는 수를 서로 더하기
        net_counts[y] += net_counts[x]
        return net_counts[y]


# 테스트 케이스의 개수
T = int(input())
for tc in range(1, T + 1):
    # 친구 관계의 수 F
    F = int(input())
    # 친구 네트워크(친구 수)
    net_counts = []
    # 친구 네트워크(인덱스 번호)
    net_numbers = []
    number = 0
    # 친구 네트워크(이름)
    net_names = {}
    # 친구 관계 생성
    for j in range(F):
        name1, name2 = map(str, input().split())

        # 새로운 이름이라면 추가하기
        if name1 not in net_names:
            # 친구 네트워크에 있는 친구 수 넣기(처음에는 자기자신)
            net_counts.append(1)
            # 친구 네트워크 인덱스 구성(관계를 묶을 번호)
            net_numbers.append(number)
            # 각 이름에 해당하는 인덱스 번호 부여
            net_names[name1] = number
            number += 1
        if name2 not in net_names:
            # 친구 네트워크에 있는 친구 수 넣기(처음에는 자기자신)
            net_counts.append(1)
            # 친구 네트워크 인덱스 구성(관계를 묶을 번호)
            net_numbers.append(number)
            # 각 이름에 해당하는 인덱스 번호 부여
            net_names[name2] = number
            number += 1

        # 유니온 함수를 사용하여 두 사람의 네트워크에 있는 친구 수를 출력
        print(union(net_numbers[net_names[name1]], net_numbers[net_names[name2]]))



