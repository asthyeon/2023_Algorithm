import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 파일 합치기
[출력: 테스트 케이스마다 모든 장을 필요하는데 필요한 최소 비용 출력]
1. 여러 파일을 하나로 합치기
2. 두 파일을 합칠 때 필요한 비용이 두 파일 크기의 합
3. 한 개의 파일을 완성하는데 필요한 비용의 총 합 구하기
4. 파일을 합치는 순서를 조정하기
@ 풀이
(1) dp 이용
"""


# dp 함수
def dynamic_programming():
    dp = []
    
    
    

T = int(input())
for tc in range(1, T + 1):
    # 소설 장 수 K
    K = int(input())
    # 각 소설 장의 크기
    sizes = list(map(int, input().split()))