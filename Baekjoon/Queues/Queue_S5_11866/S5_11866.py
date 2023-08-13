import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
1. 1번 부터 N 번 까지 원형으로 앉아 있음
2. 순서대로 K번째 사람 제거
3. 남은 사람들로 N 명의 사람이 제거될 때까지 반복
4. 원에서 사람들이 제거되는 순서 구하기
'''

N, K = map(int, input().split())

# 원을 만들 리스트 형성
arr = []
for i in range(N):
    arr.append(i + 1)

# queue 형성
queue = []

# 현재 위치
top = -1

# 큐의 길이가 N 과 같아질 때까지 반복
while len(queue) < N:
    # 위치를 1개씩 세면서
    for i in range(K):
        top += 1
        # 현재 위치가 남은 인원 수 와 같아지면 초기화
        if top == len(arr):
            top = 0
    queue.append(arr[top])
    # 인원을 지운 만큼 현재 위치도 -1
    del arr[top]
    top -= 1

# 출력
print('<', end = '', sep = '')
for i in range(N - 1):
    print(f'{queue[i]}, ', end = '')
print(queue[-1], '>', sep = '')
