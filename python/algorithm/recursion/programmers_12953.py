## https://school.programmers.co.kr/learn/courses/30/lessons/12953
"""
이것참,,,
gcd라는 함수를,,, 난 알고있어요,,
"""

import math

def solution(arr):
    # 첫 번째 숫자로 시작
    answer = arr[0]

    # 두 번째 숫자부터 하나씩 최소공배수 계산
    for i in range(1, len(arr)):
        answer = answer * arr[i] // math.gcd(answer, arr[i])

    return answer
