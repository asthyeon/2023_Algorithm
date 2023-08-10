import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 두 양의 정수가 주어졌을 때 첫 번째가 두 번째보다 큰가?
while True:
    A, B = map(int, input().split())

    if A > B:
        print('Yes')
    elif A <= B:
        if A == 0 and B == 0:
            break
        else:
            print('No')