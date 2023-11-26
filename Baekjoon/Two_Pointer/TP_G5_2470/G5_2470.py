import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 두 용액
[출력: 0에 가장 가까운 용액을 만들어내는 두 특성값을 오름차순으로 출력(두 개이상일시 아무거나)
1. 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액 만들기
@ 풀이
(1) 투 포인터 사용
"""

# 전체 용액의 수 N
N = int(input())
# 용액의 특성값들
values = list(map(int, input().split()))
values.sort()

# 투 포인터로 0에 가까운 수 찾기
answer = 10000000000000000
num1 = 0
num2 = 0
start = 0
end = N - 1
while start < end:
    # 두 수를 더한 값이 0에 더 가까우면 교체
    if answer > abs(values[start] + values[end]):
        answer = abs(values[start] + values[end])
        num1 = values[start]
        num2 = values[end]
        # 0일 경우 바로 종료
        if answer == 0:
            break
    # 합이 음수면 작은 수를 늘리기
    if values[start] + values[end] < 0:
        start += 1
    # 합이 양수면 큰 수를 줄이기
    else:
        end -= 1

print(num1, num2)

