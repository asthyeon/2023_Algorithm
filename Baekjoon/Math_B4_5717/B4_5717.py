import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 친구는 총 몇 명인가?
while True:
    # 남자 친구 수: M, 여자 친구 수: F
    M, F = map(int, input().split())

    if M == 0 and F == 0:
        break

    friends = M + F

    print(friends)