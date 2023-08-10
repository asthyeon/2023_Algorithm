import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 심사위원이 투표 결과가 주어졌을 때 누가 우승하는가?
# 심사위원의 수 V
V = int(input())
# 투표 수
A_vote = 0
B_vote = 0
vote = input()
for i in range(V):
    if vote[i] == 'A':
        A_vote += 1
    else:
        B_vote += 1

if A_vote > B_vote:
    print('A')
elif A_vote < B_vote:
    print('B')
elif A_vote == B_vote:
    print('Tie')