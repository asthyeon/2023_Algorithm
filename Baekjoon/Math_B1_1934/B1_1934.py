import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# A 와 B 의 최소 공배수 구하기

'''

T = int(input())
for tc in range(1, T + 1):
    # 자연수 A, B
    A, B = map(int, input().split())

    # 유클리드 호제법 사용
    # 최대공약수 함수
    def GCD(A, B):
        # B 가 참일 동안(자연수 일 때, a % b != 0)
        while(B):
            A, B = B, (A % B)
        return A

    # 최소공배수 함수
    def LCM(A, B):
        result = (A * B) // GCD(A, B)
        return result

    print(LCM(A, B))