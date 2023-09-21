import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 길이가 n인 문자열 S가 주어졌을 때, 
  알파벳을 최소로 바꿔서 각 알파벳이 항상 연속해서 k개 이상 등장하게 만들기
  바꿔야 하는 최소 알파벳의 수 출력
1. 문자열은 소문자로만 이루어짐
2. 문자열을 이루고 있는 문자들은 항상 연속해서 k개 이상 등장해야 함
3. 1 <= k <= n <= 2,000
4. 출력 예시
input  : 6 2
         aabccb
Output : 2
input  : 7 3
         adcbbbb
Output : 2
"""

for tc in range(1, 3):
    # 길이 n, 연속 수 k
    n, k = map(int, input().split())

    # 문자열 S
    S = input().rstrip()
