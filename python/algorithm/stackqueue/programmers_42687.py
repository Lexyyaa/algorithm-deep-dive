## https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    queue = deque()

    index = 0
    for p in priorities:
        if index == location:
            queue.append((p, True))   # 내가 찾는 문서
        else:
            queue.append((p, False))  # 다른 문서
        index += 1

    printed_count = 0  # 출력된 문서 수

    while len(queue) > 0:
        current = queue.popleft()  # 맨 앞 문서 꺼냄

        # 뒤에 더 중요한 문서가 있는지 검사
        has_higher_priority = False
        for q in queue:
            if current[0] < q[0]:      # 현재 문서보다 중요도가 높은 문서 발견
                has_higher_priority = True
                break

        if has_higher_priority:
            # 중요도가 더 높은 문서가 있으면 뒤로 보냄
            queue.append(current)
        else:
            # 출력
            printed_count += 1

            # 내가 찾는 문서라면 종료
            if current[1] == True:
                return printed_count


from collections import deque

def solution(priorities, location):
    # (우선순위, 내가 찾는 문서인지)
    queue = deque((p, i == location) for i, p in enumerate(priorities))

    printed = 0

    while queue:
        priority, is_target = queue.popleft()

        # 뒤에 더 높은 우선순위가 하나라도 있는지
        if any(priority < q[0] for q in queue):
            queue.append((priority, is_target))
        else:
            printed += 1
            if is_target:
                return printed

### 요로케 파이써닉한 코드로 할 수 도 있다!