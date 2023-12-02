import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 가입한 유저의 수 N
N = int(input().rstrip())
array = []
answer = []
for i in range(N):
    # if i == 0:
    #     answer.a
    user = [list(input().rstrip()), i]
    array.append(user)
array.sort()
print(array)

for i in range(1, N):
    cnt = 0
    for j in range(len(array[i][0])):
        if len(array[i - 1][0]) <= j or array[i - 1][0][j] != array[i][0][j]:
            break
        else:
            cnt = j + 1
    print(array[i][0][:cnt + 1])
