import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 수 N
N = int(input())

# 정렬할 빈 리스트 생성
sort_list = []

# N 을 각 자릿수로 나누고 리스트에 붙이기
while True:
    sort_list.append(N % 10)
    if N >= 10:
        N //= 10
    else:
        break

# 내림차순 정렬
sort_list.sort(reverse=True)

# 리스트를 풀고, 띄어쓰기를 줄이기
print(*sort_list, sep = '')