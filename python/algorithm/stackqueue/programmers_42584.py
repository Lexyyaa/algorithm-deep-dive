## https://school.programmers.co.kr/learn/courses/30/parts/12077
## https://school.programmers.co.kr/learn/courses/30/parts/12081

## https://school.programmers.co.kr/learn/courses/30/lessons/42584

## 주식가격

prices = [1,2,3,2,3]

## [4,3,1,1,0]

def solution(prices):
    result=[]
    for i in range(len(prices)) :
        time = 0
        now = prices[i]
        for j in range(i+1,len(prices)) :
            if now <= prices[j] :
                time += 1
            else :
                time += 1
                break
        result.append(time)
    return result


