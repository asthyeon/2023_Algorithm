import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 택배 배달과 수거하기
[출력: ]
1. n개의 집에 택배 배달
2. 배달할 물건은 모두 크기가 같음
3. i번째 집은 창고에서 i만큼 거리가 떨어져 있음
4. i번째 집은 j번째 집과 거리(j - i)만큼 떨어져 있음
5. 트럭에는 택배를 cap개 실을 수 있음
6. 트럭 하나로 모든 배달과 수거를 마치는 최소 거리 파악하기
7. 각 집에 배달 및 수거할 때 원하는 개수만큼 배달 및 수거 가능
@ 풀이[1시간 30분 안에 못품]
(1) 그냥 풀어보기 
(2) 최대한 뒤에서부터 해결을 미리 해놓아야 뒤에 다시 안옴
(3) 누적합 이용하여 풀기
"""


# 트럭 최대 적재 cap, 배달 집 수 n
# 각 집에 배달할 택배 리스트 deliveries, 회수 리스트 pickups
def solution(cap, n, deliveries, pickups):
    print(deliveries)
    print(pickups)
    deliveries.sort()
    pr
    # 뒤에서부터 반복해야 하므로 재정렬
    deliveries = deliveries.sort(reverse=True)
    pickups = pickups.sort(reverse=True)
    # 최소 거리
    answer = 0
    # 현재 배달, 회수해야 하는 택배 수
    now_d = 0
    now_p = 0

    print(deliveries)
    print(pickups)

    # 뒤에서부터 반복
    for now in range(n):
        # 이번에 배달해야하는 택배 및 회수 수 더하기
        now_d += deliveries[now]
        now_p += pickups[now]
        # 이번 배달하거나 회수해야할 것이 남아있는지 확인하고 남았다면 반복
        while now_d > 0 or now_p > 0:
            # 최대 가능 개수를 통해서 확인하기
            now_d -= cap
            now_p -= cap
            # 반복한 거리만큼 최소 거리에 더하기(왕복이므로 곱하기 2)
            answer += (n - now) * 2

    return answer

solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])