import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 두 수의 합
[출력: 조건 만족하는 쌍의 개수 출력]
1. n 개의 서로 다른 양의 정수 a1, a2, ... 수열 존재
2. 자연수 x가 주어졌을 때 a1 + a2 = x 를 만족하는 (a1, a2) 쌍 구하기
@ 풀이
(1) 투 포인터
"""

# 수열의 크기 n
n = int(input())
# 수열 a
a = list(map(int, input().split()))
# 자연수 x
x = int(input())

# 수열 정렬
a.sort()
# 조건을 만족하는 쌍의 개수
cnt = 0
# 시작
start = 0
# 끝
end = n - 1
while start < end:
    # 두 수의 합이 x라면 개수 추가 및 한칸 앞으로 전진
    if a[start] + a[end] == x:
        cnt += 1
        start += 1
        continue
    # 두 수의 합이 x 보다 작다면 큰 값을 더해야함
    elif a[start] + a[end] < x:
        start += 1
        continue
    # 두 수의 합이 x 보다 크다면 작은 값을 더해야 함
    else:
        end -= 1
        continue

print(cnt)