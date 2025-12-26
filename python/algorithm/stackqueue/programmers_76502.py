## https://school.programmers.co.kr/learn/courses/30/lessons/76502
def is_valid(s: str) -> bool:
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        # 여는 괄호면 스택에 넣기
        if ch in "([{":
            stack.append(ch)
        else:
            # 닫는 괄호인데 스택이 비어있으면 실패
            if not stack:
                return False

            # 스택의 마지막 여는 괄호가 짝이 맞아야 함
            if stack[-1] != pair[ch]:
                return False

            # 짝 맞으면 pop
            stack.pop()

    # 다 처리했을 때 스택이 비어있으면 올바름
    return len(stack) == 0


def solution(s):
    n = len(s)
    answer = 0

    # n번 회전 시도
    for i in range(n):
        rotated = s[i:] + s[:i]  # i만큼 왼쪽 회전
        if is_valid(rotated):
            answer += 1

    return answer
