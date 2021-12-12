# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

## 결국 못 풀어서 ㅜ  https://gurumee92.tistory.com/170 이분 풀이 참고 

def solution(prices):
    answer = [0]*len(prices)
    s = []

    for i in range(len(prices)):
        while s and prices[s[-1]] > prices[i]:
            top = s.pop()
            answer[top] = i-top
        s.append(i)


    while s:
        top =s.pop()
        answer[top] = len(prices) -1 -top

    return answer