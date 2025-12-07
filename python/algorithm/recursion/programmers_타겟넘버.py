# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    return recur(numbers, target, 0, 0, 0)

def recur(numbers, target, current_sum, depth, count):

    if depth == len(numbers):
        if current_sum == target:
            return count + 1
        else:
            return count

    count = recur(numbers, target, current_sum + numbers[depth], depth + 1, count)
    count = recur(numbers, target, current_sum - numbers[depth], depth + 1, count)

    return count

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 5

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))  # 2
