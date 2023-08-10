import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 카드의 개수: N, 최대값: M
N, M = map(int, input().split())
# 카드에 쓰여 있는 수
arr = list(map(int, input().split()))
# 조합을 붙일 리스트 생성
combi = []

# 카드 3장의 합 나열
for A in arr:
    for B in arr:
        if B != A:
            for C in arr:
                if C != A and C != B:
                    combi.append(A + B + C)

# M 보다 작은 리스트 생성
max_list = []
# M 이 combi 안에 있다면 M 출력
if M in combi:
    print(M)
# M 이 combi 안에 없다면 제일 가까운 값 출력
else:
    for i in range(len(combi)):
        if M > combi[i]:
            max_list.append(combi[i])
    print(max(max_list))



