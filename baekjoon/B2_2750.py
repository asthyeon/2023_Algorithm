import sys
sys.stdin = open("input.txt", "r")

# 총 입력받을 수 N 입력 받기
N = int(input())

# 숫자를 넣을 빈 리스트 생성
num_list = []

# 숫자 반복
for i in range(N):
    # N개의 수 입력 받기
    num = int(input())
    # 숫자들 빈 리스트에 넣기
    num_list.append(num)

# 리스트 오름차순 정렬
num_list.sort()

# 리스트를 한 줄씩 출력하기
for i in range(N):
    print(num_list[i])




