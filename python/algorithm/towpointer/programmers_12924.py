## https://school.programmers.co.kr/learn/courses/30/lessons/12924

"""
 냅다 재귀로 박아볼까 햇지만? n이 최대 10000 인것을 보고 포기했다
 그렇다면 그리디? 하지만 이것은 모든 경우의 수를 찾는것이니까 그리디도 아니다...

 그렇다면,., 문제를 다시한번 살펴보자,,,

 n을 완성하기위한 숫자 구성.,. 그렇다면 수 중에 가장 큰 것은 n 일터이니..

 그렇다면 투포인터를 쓰는 문제로 바라볼 수 있다!

"""

def solution(n):
    answer = 0

    left = 1
    right = 1

    # 구간의 합
    current_sum = 1

    # left가 n을 넘으면 더 이상 의미 있는 구간이 없음
    while left <= n:

        # 현재 구간의 합이 n과 정확히 같으면
        if current_sum == n:
            answer += 1  # 경우의 수 1 증가

            # 다음 경우를 찾기 위해
            # 왼쪽 값을 제거하고 구간을 한 칸 앞으로 이동
            current_sum -= left
            left += 1

        # 현재 합이 n보다 작으면
        elif current_sum < n:
            # 오른쪽을 확장해서 합을 키운다
            right += 1
            current_sum += right

        # 현재 합이 n보다 크면
        else:
            # 왼쪽을 줄여서 합을 줄인다
            current_sum -= left
            left += 1

    return answer
