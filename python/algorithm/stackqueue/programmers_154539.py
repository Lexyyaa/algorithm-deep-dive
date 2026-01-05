## https://school.programmers.co.kr/learn/courses/30/lessons/154539


def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 기본값: 끝까지 못 찾으면 -1

    stack = []  # "아직 뒷 큰수 못 찾은 인덱스" 보관 (값 자체가 아니라 인덱스)

    for i in range(n):
        # 지금 numbers[i]가, 스택에 쌓인 애들의 "뒷 큰수"가 될 수 있는지 확인
        # 스택 top이 가리키는 값보다 '크면', 그 애의 뒷 큰수는 바로 numbers[i]
        while stack and numbers[stack[-1]] < numbers[i]:
            j = stack.pop()
            answer[j] = numbers[i]

        # i는 아직 뒷 큰수를 모르는 상태로 스택에 대기
        stack.append(i)

    # stack에 남은 인덱스들은 끝까지 더 큰 수를 못 만난 것
    # answer가 -1 그대로면 OK
    return answer
