import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램 만들기
1. N 개의 수열 및, N - 1 개의 연산자가 주어짐
2. 연산자: +, -, *, /
3. 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만들 수 있음
4. 주어진 수의 순서를 바꿔선 안됨
5. 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
6. 나눗셈은 몫만 취함
7. 음수를 양수로 나눌 때는 양수로 바꾼뒤 몫을 취하고, 그 몫을 음수로 바꾸기
8. 결과값 및 중간에 계산되는 식의 결과도 항상 -10억 <= 결과 <= 10억
@ 풀이
(1) 백트래킹으로 풀기
"""


# 백트래킹 함수
def backtracking(result, idx, plus, minus, multiply, divide):
    global maximum
    global minimum
    # 재귀를 종료할 기저조건(모든 연산자를 다 사용한 경우)
    if plus == minus == multiply == divide == 0:
        if maximum < result:
            maximum = result
        if minimum > result:
            minimum = result
            return

    if plus:
        idx += 1
        result += A[idx]
        plus -= 1
        backtracking(result, idx, plus, minus, multiply, divide)
        plus += 1
        result -= A[idx]
        idx -= 1
    if minus:
        idx += 1
        result -= A[idx]
        minus -= 1
        backtracking(result, idx, plus, minus, multiply, divide)
        minus += 1
        result += A[idx]
        idx -= 1
    if multiply:
        idx += 1
        result *= A[idx]
        multiply -= 1
        backtracking(result, idx, plus, minus, multiply, divide)
        multiply += 1
        result = int(result / A[idx])
        idx -= 1
    if divide:
        idx += 1
        if result < 0:
            result = (-result // A[idx]) * -1
        else:
            result = result // A[idx]
        divide -= 1
        backtracking(result, idx, plus, minus, multiply, divide)
        divide += 1
        result *= A[idx]
        idx -= 1


# 수의 개수 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))
# 각 연산자의 개수(+, -, *, /)
plus, minus, multiply, divide = map(int, input().split())

# 최대치 및 최소치 변수
maximum = -1000000000
minimum = 1000000000
# 계산결과
result = A[0]
# 수열의 인덱스
idx = 0

backtracking(result, idx, plus, minus, multiply, divide)

print(maximum)
print(minimum)