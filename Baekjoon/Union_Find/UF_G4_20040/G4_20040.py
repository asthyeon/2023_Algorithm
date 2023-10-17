import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 게임 진행 상황이 주어지면 사이클이 완성되었는지, 몇 번째 차례에서 완성되었는지 출력
1. 사이클 게임: 두 명의 플레이어가 차례대로 돌아가며 진행
2. 선 플레이어가 홀수 번째 차례, 후 플레이어가 짝수 번째 차례
3. 게임 시작시 0 부터 n-1 까지 고유한 번호가 부여된 평면 상의 점 n개가 주어짐
4. 이 중 어느 세 점도 일직선 위에 놓이지 않는다.
5. 매 차례마다 플레이어는 두 점을 선택해서 이를 연결하는 선분을 그음
6. 이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차 가능
7. 게임을 진행하다가 처음으로 사이클을 완성하는 순간 게임 종료
 - 사이클: 임의의 선분의 한 끝점에서 출발, 모든 선분을 한 번씩 지나 출발점으로 되돌아옴
8. 사이클이 완성되지 않았다면 0 출력
@ 풀이
(1) 유니온 파인드 사용
"""


# find 함수
def find(x):
    if points[x] == x:
        return x
    points[x] = find(points[x])
    return points[x]


# union 함수
def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        points[y] = x
    # 루트 노드가 같을 때 사이클이 완성되므로 그대로 출력 후 종료
    elif x == y:
        print(j)
        exit()
    else:
        points[x] = y


# 점의 개수 n, 진행된 차례의 수 m
n, m = map(int, input().split())

# 각 점들
points = [i for i in range(n)]

# 선분 긋기
for j in range(1, m + 1):
    p1, p2 = map(int, input().split())
    
    # 유니온 함수 사용
    union(p1, p2)

# 사이클이 완성되지 않았을 경우 0 출력
print(0)