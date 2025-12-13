## https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    used = [False] * len(numbers)
    max_value = ""

    def dfs(path):
        nonlocal max_value

        if len(path) == len(numbers):
            candidate = ''.join(path)
            if candidate > max_value:
                max_value = candidate
            return

        for i in range(len(numbers)):
            if not used[i]:
                used[i] = True
                dfs(path + [nums[i]])
                used[i] = False

    nums = list(map(str, numbers))
    dfs([])
    return max_value

### 이렇게 하면 런타임에러뜸 O(N!)... ㅠㅠ


def solution(numbers):
    # 숫자를 문자열로 변환
    nums = list(map(str, numbers))

    # x+y vs y+x 와 동일한 효과
    # numbers의 최대 자릿수를 고려해서 *3 사용
    nums.sort(key=lambda x: x * 3, reverse=True)

    result = ''.join(nums)

    # [0, 0, 0] 같은 케이스 처리
    return '0' if result[0] == '0' else result


