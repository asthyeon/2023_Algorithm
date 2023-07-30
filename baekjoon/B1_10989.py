import sys
sys.stdin = open("input.txt", "r")

# 수의 개수:N
N = int(sys.stdin.readline())

# 인덱스 값이 최대 10001[0 ~ 10000]인 리스트 형성
sorting_list = [0] * 10001

# 숫자를 넣으면 그 값에 해당하는 인덱스 값 + 1
for i in range(N):
    num = int(sys.stdin.readline())
    sorting_list[num] += 1

# 리스트 길이 만큼 반복
for j in range(len(sorting_list)):
    # 리스트 인덱스 값이 0이 아니라면
    if sorting_list[j] != 0:
        # 인덱스 값만큼 반복하여
        for k in range(sorting_list[j]):
            # 리스트 인덱스 번호를 출력
            print(j)

# # 메모리 초과 뜨는 문제풀이
# # 숫자를 정렬한 빈 리스트 만들기
# sorting = {}

# # 빈 리스트에 N개의 수 넣기
# for i in range(N):
#     num = int(input())
#     sorting.add(num)

# # 오름차순 정렬
# sorting.sort()

# # 한줄씩 출력
# for i in range(N):
#     print(sorting[i])