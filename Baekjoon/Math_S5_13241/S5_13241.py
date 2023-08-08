import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 유클리드 호제법 이용하기
# 정수 B 에 0 보다 큰 정수인 N 을 곱해 정수 A 를 만들 수 있다면, A 는 B 의 배수이다
# A 와 B 의 최소 공배수 출력하기
'''

# A, B 입력
A, B = map(int, input().split())

# 최대 공약수 함수
def GCD(A, B):
    while(B):
        A, B = B, (A % B)
    return A

# 최소 공배수 함수
def LCM(A, B):
    result = (A * B) // GCD(A, B)
    return result

print(LCM(A, B))