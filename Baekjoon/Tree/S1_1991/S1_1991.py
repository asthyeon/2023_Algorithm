import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이진 트리를 입력 받아 전위 순회, 중위 순회, 후위 순회한 결과 출력
1. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨짐
2. 항상 A가 루트 노드가 됨
3. 자식 노드가 없는 경우 .으로 표현
@ 풀이
(1) 알파벳을 숫자로 변환
"""

# 알파벳을 숫자로 변환할 딕셔너리
alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
             'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
             'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
             'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
             'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# 숫자를 알파벳으로 변환할 딕셔너리
numbers = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
           6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
           11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
           16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
           21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}


# 전위순회 함수
def preorder(n, ch1, ch2):
    if n:
        print(numbers[n], end='')
        preorder(ch1[n], ch1, ch2)
        preorder(ch2[n], ch1, ch2)


# 중위순회 함수
def inorder(n, ch1, ch2):
    if n:
        inorder(ch1[n], ch1, ch2)
        print(numbers[n], end='')
        inorder(ch2[n], ch1, ch2)


# 후위순회 함수
def postorder(n, ch1, ch2):
    if n:
        postorder(ch1[n], ch1, ch2)
        postorder(ch2[n], ch1, ch2)
        print(numbers[n], end='')


# 이진 트리의 노드의 개수 N
N = int(input())

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)

# 노드 연결 상황
for _ in range(N):
    p, c1, c2 = map(str, input().split())
    if c1 != '.':
        ch1[alphabets[p]] = alphabets[c1]
    if c2 != '.':
        ch2[alphabets[p]] = alphabets[c2]

preorder(1, ch1, ch2)
print()
inorder(1, ch1, ch2)
print()
postorder(1, ch1, ch2)