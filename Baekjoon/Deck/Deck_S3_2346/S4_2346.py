import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# N 개의 풍선이 원형으로 놓여 있음
1. 1번 풍선 터쳐
2. 풍선 안의 종이값만큼 이동후 터쳐
3. 양수 오른쪽, 음수 왼쪽, 이미 터진 풍선 스킵
# 터진 풍선 번호 나열
'''

N = int(input())

# 풍선 번호
numb = list(map(int, input().split()))

# 풍선 리스트
arr = []
for i in range(1, N):
    arr.append(i + 1)

# 현재 위치
top = 0

# 덱 형성
deck = [1]

while len(deck) < N:
    # 종료조건 추가
    if len(deck) == N - 1:
        deck.append(arr[0])
        break
    # 이동 값 먼저 빼내기
    move = numb.pop(top)
    # 인덱스 맞추기
    if top == len(numb):
        top = 0
    elif top < 0:
        top = len(arr) - 1
    # 이동값이 양수일 때
    if move > 0:
        for j in range(move - 1):
            top += 1
            # 초기화
            if top == len(arr):
                top = 0
    # 이동값이 음수일 때
    else:
        for k in range(abs(move)):
            top -= 1
            if top < 0:
                top = len(arr) - 1
    # 이동한 지점의 값을 덱에 넣기
    deck.append(arr.pop(top))

print(*deck)

