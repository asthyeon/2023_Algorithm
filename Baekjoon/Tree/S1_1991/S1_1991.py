import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이진 트리를 입력 받아 전위 순회, 중위 순회, 후위 순회한 결과 출력
1. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨짐
2. 항상 A가 루트 노드가 됨
3. 자식 노드가 없는 경우 .으로 표현
"""

# 이진 트리의 노드의 개수 N
N = int(input())

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)

# 노드 연결 상황
for _ in range(N):
    break