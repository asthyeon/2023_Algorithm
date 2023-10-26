import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# n이 주어졌을 때 피보나치 수 F(n) 구하기 (n은 음수 가능)
1. 피보나치 수의 정의
 - F(0) = 0(if n = 0;)
 - F(1) = 1(if n = 1;)
 - F(n) = F(n - 1) + F(n - 2)(if n > 1;)
2. 피보나치 수를 n이 음수인 경우로도 확장하기
 - 위의 식에서 n > 1인 경우에는 성립하는 경우를,
 - if n <= 1 일 때도 성립되도록 정의하기
3. 첫째 줄은 양수는 1, 0이면 0, 음수면 -1 출력
4. 둘째 줄은 F(n)의 (절댓값 / 1,000,000,000) 출력
@ 풀이
(1) dp 사용
"""


# dp 함수
def dynamic_programming(n):
    # 절대값 n
    new_n = abs(n)
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 1
    for i in range(3, new_n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
    if new_n == 0:
        return print(0)
    elif new_n == 1:
        return print(1)
    else:
        return print(dp[new_n] % 1000000000)


# 숫자 n
n = int(input())

# 양수일 때는 1 출력
if n > 0:
    print(1)
# 0일 때는 0 출력
elif n == 0:
    print(0)
# 음수일 때는
else:
    # 홀수일 때는 양수이므로 1 출력
    if abs(n) % 2 == 1:
        print(1)
    # 짝수일 때는 음수이므로 -1 출력
    else:
        print(-1)

dynamic_programming(n)