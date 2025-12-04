
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

n = 6
times = [7,10]
min_time= 0 # 최소시간은 0부터 시작
### 이진탐색은 가능한 범위 안에서 정답을 좁혀나가는 과정임... 수학적으로 최소값의 하한은 0이기 때문에 0으로 설정!
### 그렇다면 왜 min(times)* n 으로 하면 안되는가?
### n = 6 , times [1,2,3] 인 경우를 생각해보자 최소시간은 3 이다... ㅇㅋ?


min_time= 0 # 이진탐색에서 사용할 최소시간 설정
max_time = max(times) * n # 제일 오래걸리는 심사관이 다 심사할때까지 걸리는 시간
result_time = max_time # result_time을 최대시간으로 초기화하는 이유는 최소시간을 찾기 위해서임
while min_time <= max_time :
    mid_time = (min_time + max_time) // 2
    ## 중간값을왜 찾음? 최소시간과 최대시간 사이에서 가능한 시간을 반으로 나누어서 탐색하기 위해서임
    total_people = 0
    for time in times :
        total_people += mid_time // time
        # mid_time을 time 으로 나눈몫을 구함 -> mid_time 안에 각 심사관이 몇명까지 심사할 수 있는지 계산함
    if total_people >= n : # mid_time 안에 n명을 다 심사할 수 있는 경우
        result_time = mid_time
        max_time = mid_time - 1 # 범위 좁히기!
    else : # mid_time 안에 n명을 다 심사할 수 없는 경우
        min_time = mid_time + 1 # 범위 좁히기!

## while 문의 조건을 탈출하면 (min>max 가 되면) 결과를 출력함!
print(result_time)


"""
def solution(n, times):
    min_time= 0
    max_time = max(times) * n # 제일 오래걸리는 심사관이 다 심사할때까지 걸리는 시간
    result_time = max_time
    while min_time <= max_time :
        mid_time = (min_time + max_time) // 2
        total_people = 0
        for time in times :
            total_people += mid_time // time
        if total_people >= n : # mid_time 안에 n명을 다 심사할 수 있는 경우
            result_time = mid_time
            max_time = mid_time - 1
        else : # mid_time 안에 n명을 다 심사할 수 없는 경우
            min_time = mid_time + 1

    return result_time
"""