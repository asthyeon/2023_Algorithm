import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 그릇 높이 계산
1. 그릇을 바닥에 놓을 때 높이 10cm
2. 두 개의 그릇을 같은 방향으로 포개면 높이 + 5cm
3. 반대방향으로 쌓으면 높이 + 10cm
4. '(' = 그릇이 바닥에 바로 놓인 상태
5. ')' = 그릇이 거꾸로 놓인 상태
"""

# 그릇 입력
dishes = input().rstrip()
height = 10
for i in range(1, len(dishes)):
    if dishes[i - 1] != dishes[i]:
        height += 10
    else:
        height += 5

print(height)