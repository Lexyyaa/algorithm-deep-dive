## https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    # 오른쪽(전체)에 있는 토핑 개수 카운트
    right = Counter(topping)
    # 오른쪽 토핑 - 종류 수
    right_kinds = len(right)

    # 왼쪽 토핑 - 종류만 관리
    left = set()
    answer = 0

    # 마지막에서 자르면 오른쪽이 비므로(len-1까지 이동) 컷은 len-2까지만 의미 있음
    for i in range(len(topping) - 1):
        t = topping[i]

        # i번째 토핑을 오른쪽에서 왼쪽으로 "이동"
        left.add(t)

        right[t] -= 1
        if right[t] == 0:
            # 해당 토핑이 오른쪽에서 사라지면 종류 수 감소
            right_kinds -= 1

        # 현재 컷 위치에서 양쪽 종류 수가 같으면 카운트
        if len(left) == right_kinds:
            answer += 1

    return answer
