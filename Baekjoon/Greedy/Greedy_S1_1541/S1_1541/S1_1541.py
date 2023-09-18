import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들기
1. 수는 0으로 시작할 수 있다
2. 연산자는 +, -로 이루어져 있음
"""

# 식
formula = input().rstrip()

# 숫자와 식 구분하기
calculator = []
stack = ''
result = 0
for i in formula:
    if i.isdigit():
        stack += i
    # 피연산자인경우 스택에 넣은 것을 숫자로 만들고 초기화
    elif i == '+':
        calculator.append(int(stack))
        calculator.append('+')
        stack = ''
    else:
        calculator.append(int(stack))
        calculator.append('-')
        stack = ''
else:
    calculator.append(int(stack))

minus = 0
tmp = 0
for j in range(len(calculator)):
    if j == 0:
        result += calculator[j]
    else:
        if calculator[j - 1] == '-':
            result -= tmp
            tmp = 0
            tmp += calculator[j]
            minus = 1
        elif calculator[j - 1] == '+':
            if minus == 1:
                tmp += calculator[j]
            else:
                result += calculator[j]
        else:
            continue
else:
    result -= tmp

print(result)





