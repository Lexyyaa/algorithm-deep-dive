## https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    # 남은 작업 총합이 줄일 수 있는 시간 n 이하라면 전부 0 가능 -> 야근 지수 0
    if sum(works) <= n:
        return 0

    # 최대 힙 구성: heapq는 최소 힙이므로 음수로 넣어서 최대 힙처럼 사용
    max_heap = [-w for w in works]
    heapq.heapify(max_heap)

    # n시간 동안: 가장 큰 작업을 1 줄이기
    for _ in range(n):
        # 현재 가장 큰 작업량 꺼내기(음수이므로 가장 작은 음수가 가장 큰 작업)
        w = -heapq.heappop(max_heap)

        # w는 반드시 1 이상(총합 > n이므로)인데, 방어적으로 0이면 중단
        if w == 0:
            heapq.heappush(max_heap, 0)
            break

        # 1 감소 후 다시 힙에 넣기
        w -= 1
        heapq.heappush(max_heap, -w)

    # 남은 작업량 제곱합 계산 (힙에는 음수로 들어있음)
    return sum((-x) ** 2 for x in max_heap)
