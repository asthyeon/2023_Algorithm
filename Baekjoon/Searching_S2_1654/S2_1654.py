import sys
sys.stdin = open('input.txt')

# N 개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력하라

# 이미 가진 랜선의 개수: K, 필요한 랜선의 개수: N
K, N = map(int, input().split())

# 랜선 리스트
lan = []

# 각 랜선의 길이 받기
for _ in range(K):
    lan.append(int(input()))

# 랜선 리스트 길이
lan_length = 0
for i in lan:
    lan_length += 1

# 오름차순 정렬
for i in range(lan_length - 1, 0, -1):
    for j in range(i):
        if lan[j] > lan[j + 1]:
            lan[j], lan[j + 1] = lan[j + 1], lan[j]

# 각 랜선의 합
lan_sum = 0
for i in lan:
    lan_sum += i

# N 으로 나눴을 때 대략적으로 필요한 랜선의 길이
lan_need = lan_sum / 11

# 자른 랜선 수
lan_cut = 0

# 자른 랜선의 길이중 최대 길이를 구하기 위한 리스트
lan_max_list = []

# 반복문
while lan_cut < 11:
    # 이진 탐색
    for i in range(lan_length):
        while (lan[i] // 2) > lan_need:
            lan[i] = (lan[i] // 2)
            lan_cut += 1
        else:
            lan_max_list.append(lan[i])
            break

print(max(lan_max_list))

    
