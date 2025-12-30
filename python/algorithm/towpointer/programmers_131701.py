## https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    n = len(elements)

    # 원형을 선형으로 다루기 위해 2배로 늘린다.
    doubled = elements + elements

    # 누적합(prefix sum) 생성: prefix[i] = doubled[0] ~ doubled[i-1] 합
    prefix = [0] * (2 * n + 1)
    for i in range(2 * n):
        prefix[i + 1] = prefix[i] + doubled[i]

    sums = set()

    # 길이 L = 1 ~ n
    for L in range(1, n + 1):
        # 시작점 i = 0 ~ n-1 (원래 배열에서 시작 가능한 위치만)
        for i in range(n):
            # 구간합: doubled[i] ~ doubled[i+L-1]
            s = prefix[i + L] - prefix[i]
            sums.add(s)

    return len(sums)


def solution(elements):
    n = len(elements)
    doubled = elements + elements  # 원형을 선형으로 처리

    sums = set()

    # 윈도우 길이 L을 1부터 n까지
    for L in range(1, n + 1):
        # 첫 윈도우(시작점 0)의 합
        window_sum = sum(doubled[0:L])
        sums.add(window_sum)

        # 시작점을 1 ~ n-1로 슬라이딩
        # 이전 윈도우: [i-1, i-1+L)
        # 다음 윈도우: [i, i+L)
        for i in range(1, n):
            # 왼쪽 끝 하나 빼고, 오른쪽 새로 들어오는 값 하나 더함
            window_sum -= doubled[i - 1]
            window_sum += doubled[i + L - 1]
            sums.add(window_sum)

    return len(sums)
