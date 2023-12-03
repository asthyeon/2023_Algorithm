import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
"""

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
cnt = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
       5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for r in result:
    cnt[int(r)] += 1

for i in range(10):
    print(cnt[i])
