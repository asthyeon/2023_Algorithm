import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램
'''

# 분자와 분모를 뜻하는 두 개의 자연수 두 줄
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

# 최대공약수 함수
def GCD(A, B):
    while A > 1:
        if B == 0:
            break
        A, B = B, (A % B)
    return A

# 최소공배수 함수
def LCM(A, B):
    result = (A * B) // GCD(A, B)
    return result

# 통분하기(분자: A3, 분모: B3)
# 각 분모의 최소공배수로 통분
B3 = LCM(B1, B2)
# 최소공배수가 되기위해 곱한 값만큼 분자에도 곱해서 더해주기
A3 = (A1 * (B3 // B1)) + (A2 * (B3 // B2))
# 분자와 분모의 최대공약수를 구하기
gcd = GCD(A3, B3)
# 분자와 분모를 최대공약수로 나눠서 기약분수로 만들기
A4 = A3 // gcd
B4 = B3 // gcd

print(A4, B4)