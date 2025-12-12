## https://school.programmers.co.kr/learn/courses/30/lessons/12909
## # 올바른 괄호
## 여는 괄호가 있으면 닫는괄호가 있어야하니까
## 여는괄호를 조건으로 잡고 닫는괄호가 있으면 pop 하는 방식으로 진행 ㄱㄱ
def solution(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

