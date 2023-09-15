import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 곰곰티콘이 사용된 횟수 구하기
1. ENTER 는 새로운 사람이 채팅방에 입장했음을 나타냄
2. 그 외는 채팅을 입력한 유저의 닉네임을 나타냄
3. 새로운 사람이 입장한 이후 '처음' 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사함
4. 첫번째 주어지는 문자열은 무조건 ENTER
@ 풀이
(1) 새로운 사람이 들어오면 입력받고
(2) 옛날 사람이 채팅치면 곰곰횟수 늘리지 않기
'''

# 채팅방의 기록 수 N
N = int(input())
# 닉네임 딕셔너리
nicks = {}
# 곰곰티콘 출력 횟수
cnt = 0

# 문자열 입력(ENTER or 유저의 닉네임)
for _ in range(N):
    message = input().rstrip()

    # 엔터가 아니고
    if message != 'ENTER':
        # 딕셔너리에 없다면 추가후 곰곰티콘 카운팅
        if message not in nicks:
            nicks[message] = message
            cnt += 1
    # 엔터라면 딕셔너리 초기화
    else:
        nicks.clear()

print(cnt)

