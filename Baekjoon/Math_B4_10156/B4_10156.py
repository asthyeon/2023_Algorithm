import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 동수가 부모님께 받아야 하는 돈 출력
# 과자 한개 가격: K, 사려고 하는 과자 수: N, 가진 돈: M
K, N, M = map(int, input().split())

# 받아야 하는 돈
money = (K * N) - M

# 음수이면 0원
if money < 0:
    money = 0

print(money)