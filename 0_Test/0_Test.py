import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 총 K 번 회전시킨 이후에 네 톱니바퀴의 점수의 합 출력
1. 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 일렬로 놓여 있음
2. 톱니는 N극 or S극을 나타냄
3. 가장 왼쪽톱니바퀴가 1번, 2번, 3번, 4번
4. 이 때 톱니바퀴를 총 K번 회전시키려고 함(시계 방향, 반시계 방향 존재)
5. 톱니바퀴를 회전할 때 옆의 톱니바퀴와 서로 맞닿은 극이 다르면 반대방향으로 회전
6. 서로 맞닿은 극이 같으면 회전 X
"""


# 시계방향 회전 함수
def spin_clockwise(number, spin, one, two, three, four):
    global new_one
    global new_two
    global new_three
    global new_four
    print(f'numbers {numbers[1]}, {numbers[2]}, {numbers[3]}, {numbers[4]}')
    print(f'three {three}')
    print(f'clockwise {number} {numbers[number]}')
    new = ''
    for i in range(8):
        if i == 0:
            new += numbers[number][-1]
            continue
        new += numbers[number][i - 1]
    spin[number] = 1
    print(f'clockwise {number} {new}')
    # 1번 톱니일 때
    if number == 1:
        # 2번 톱니가 회전했다면 종료
        if spin[2] == 1:
            new_one = new
            return
        # 2번 톱니가 회전하지 않았다면
        else:
            # 2번 톱니와 극이 다르다면
            if one[2] != two[6]:
                # 2번 반시계방향 회전
                spin_counterclockwise(2, spin, one, two, three, four)
            new_one = new
            return
    # 2번 톱니일 때
    elif number == 2:
        # 1번 톱니가 회전하지 않았다면
        if spin[1] == 0:
            # 1번 톱니와 극이 다르다면
            if two[6] != one[2]:
                # 1번 반시계방향 회전
                spin_counterclockwise(1, spin, one, two, three, four)
        # 3번 톱니가 회전하지 않았다면
        if spin[3] == 0:
            # 3번 톱니와 극이 다르다면
            if two[2] != three[6]:
                # 3번 반시계방향 회전
                spin_counterclockwise(3, spin, one, two, three, four)
        new_two = new
        return
    # 3번 톱니일 때
    elif number == 3:
        # 2번 톱니가 회전하지 않았다면
        if spin[2] == 0:
            # 2번 톱니와 극이 다르다면
            if three[6] != two[2]:
                # 1번 반시계방향 회전
                spin_counterclockwise(2, spin, one, two, three, four)
        # 4번 톱니가 회전하지 않았다면
        if spin[4] == 0:
            # 4번 톱니와 극이 다르다면
            if three[2] != four[6]:
                # 4번 반시계방향 회전
                spin_counterclockwise(4, spin, one, two, three, four)
        new_three = new
        return
    # 4번 톱니일 때
    else:
        # 3번 톱니가 회전했다면 종료
        if spin[3] == 1:
            new_four = new
            return
        # 3번 톱니가 회전하지 않았다면
        else:
            # 3번 톱니와 극이 다르다면
            if four[6] != two[2]:
                # 3번 반시계방향 회전
                spin_counterclockwise(3, spin, one, two, three, four)
            new_four = new
            return


# 반시계방향 회전 함수
def spin_counterclockwise(number, spin, one, two, three ,four):
    global new_one
    global new_two
    global new_three
    global new_four
    print(f'counterclockwise {number} {numbers[number]}')
    new = ''
    for i in range(8):
        if i == 7:
            new += numbers[number][0]
            break
        new += numbers[number][i + 1]
    spin[number] = 1
    print(f'counterclockwise {number} {new}')
    # 1번 톱니일 때
    if number == 1:
        # 2번 톱니가 회전했다면 종료
        if spin[2] == 1:
            new_one = new
            return
        # 2번 톱니가 회전하지 않았다면
        else:
            # 2번 톱니와 극이 다르다면
            if one[2] != two[6]:
                # 2번 시계방향 회전
                spin_clockwise(2, spin, one, two, three, four)
            new_one = new
            return
    # 2번 톱니일 때
    elif number == 2:
        # 1번 톱니가 회전하지 않았다면
        if spin[1] == 0:
            # 1번 톱니와 극이 다르다면
            if two[6] != one[2]:
                # 1번 시계방향 회전
                spin_clockwise(1, spin, one, two, three, four)
        # 3번 톱니가 회전하지 않았다면
        if spin[3] == 0:
            # 3번 톱니와 극이 다르다면
            if two[2] != three[6]:
                # 3번 시계방향 회전
                print(f'three {three}')
                spin_clockwise(3, spin, one, two, three, four)
        new_two = new
        return
    # 3번 톱니일 때
    elif number == 3:
        # 2번 톱니가 회전하지 않았다면
        if spin[2] == 0:
            # 2번 톱니와 극이 다르다면
            if three[6] != two[2]:
                # 1번 반시계방향 회전
                spin_clockwise(2, spin, one, two, three, four)
        # 4번 톱니가 회전하지 않았다면
        if spin[4] == 0:
            # 4번 톱니와 극이 다르다면
            if three[2] != four[6]:
                # 4번 반시계방향 회전
                spin_clockwise(4, spin, one, two, three, four)
        new_three = new
        return
    # 4번 톱니일 때
    else:
        # 3번 톱니가 회전했다면 종료
        if spin[3] == 1:
            new_four = new
            return
        # 3번 톱니가 회전하지 않았다면
        else:
            # 3번 톱니와 극이 다르다면
            if four[6] != two[2]:
                # 3번 반시계방향 회전
                spin_clockwise(3, spin, one, two, three, four)
            new_four = new
            return


# 점수 계산 함수
def calculator(numbers, one, two, three, four):
    global total
    # 점수 리스트
    scores = [0, 1, 2, 4, 8]
    for i in range(1, 5):
        if numbers[i][0] == '1':
            total += scores[i]


# 1 ~ 4번 톱니바퀴 상태(12시 방향부터 시계방향 순서대로 주어짐)
one = input().rstrip()
two = input().rstrip()
three = input().rstrip()
four = input().rstrip()
# 바뀐 톱니 상태
new_one = one
new_two = two
new_three = three
new_four = four
# 전체 점수
total = 0
# 톱니바퀴 번호 부여
numbers = {1: one, 2: two, 3: three, 4: four}
# 회전횟수 K
K = int(input())
print(one, two, three, four)
# K번 회전시킨 방법
for _ in range(K):
    # 톱니 회전 유무
    spin = [0] * 5
    # 톱니바퀴 번호 number, 방향 direction(1: 시계, -1: 반시계)
    number, direction = map(int, input().split())
    if direction == 1:
        spin_clockwise(number, spin, one, two, three, four)
    else:
        spin_counterclockwise(number, spin, one, two, three, four)
    # 톱니상태 바꾸기
    one = new_one
    two = new_two
    three = new_three
    four = new_four
    print(one, two, three, four)

# 점수 계산
calculator(numbers, one, two, three, four)
print(total)