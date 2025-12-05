## https://www.acmicpc.net/problem/10872

#### 야야야  이력서 어따났어 이따가 오빠한테 줘야함 미리 나에게 모내놓기로 정리해놔!!!!!!

def factorial(n):
    ## 자 팩토리얼에서 종료조건은 뭐냐면
    ## n이 0 이나 1 일때 return 1
    ## 팩토리얼은 점화식으로 나타내면 f(n) = n * f(n-1) 이잖아요?
    ## 그걸 이제 코드에 고대로 녹여주면 됩니다
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n - 1)

n = int(input())

print(factorial(n))