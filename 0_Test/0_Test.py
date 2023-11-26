import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
"""

T = int(input())
for _ in range(1, T + 1):
    # ox
    ox = input().rstrip()

    idx = 0
    total = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            idx += 1
            total += idx
        else:
            idx = 0

    print(total)