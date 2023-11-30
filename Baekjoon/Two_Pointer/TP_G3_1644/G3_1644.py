import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 소수의 연속합
[출력: 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수 출력
1. 자연수가 주어졌을 때 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수 구하기
2. 한 소수는 반드시 한 번만 덧셈에 사용됨
@ 풀이
(1) 소수를 구하고 그 소수들에서 투 포인터 사용하기
(2) 소수를 어떻게 구할것인가 => 에라토스테네스의 체
"""

# 자연수 N
N = int(input())

# N이 1일때 종료하기
if N == 1:
    print(0)
    exit()

# 에라토스테네스의 체
# 처음엔 모든 수가 소수인 것으로 가정
arr = [True for _ in range(N + 1)]
for i in range(2, (int(N ** 0.5) + 1)):
    # i 가 소수인 경우(남은 수인 경우)
    if arr[i] == True:
        # i 를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1
# 모든 소수 저장하기
primes = []
for k in range(N + 1):
    if k > 1 and arr[k]:
        primes.append(k)

# 투 포인터
start = 0
end = 0
total = primes[start]
cnt = 0
# end가 소수리스트 마지막이 될 떄까지
while end < len(primes):
    # 해당 값이면 회수 +1 및 시작점 줄이기
    if total == N:
        cnt += 1
        total -= primes[start]
        start += 1
    # 해당 값보다 작으면 끝점 늘리기
    elif total < N:
        end += 1
        if end == len(primes):
            break
        total += primes[end]
    # 해당 값보다 크다면 시작점 줄이기
    else:
        total -= primes[start]
        start += 1

print(cnt)