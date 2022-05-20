#--------------------- 풀이 1 --------------------# 

# 첫번째 시도 => 런타임 에러 ㅠㅠ 

def solution(N, stages):

    stages.sort() # stage sort 
    answer = { x: 0 for x in range(1,N+2) } # stages에 1~N+1까지 담겨있음 

    # stage마다 user count 
    for key,_ in answer.items():
        answer[key] = stages.count(key)

    # 실패율 
    result = []

    for i in range(1,N+1):
        # 분자 : n번 도전 횟수 
        n_try = answer[i]
        
        # 분모 : n보다 큰 수 
        n_more = 0
        
        for j in range(i,N+2):
            n_more +=answer[j]
        print(n_try,n_more, n_try/(n_more+n_try))
        
        result.append([n_try/(n_more+n_try),i])   

    # 스테이지 번호를 실패율의 내림차순으로 정렬 , 크기가 동일하면 오름차순부터  
    result.sort(key=lambda x :(-x[0],x[1]))

    return [i for _,i in result]

#--------------------- 풀이 2 --------------------# 

# 두번째 시도 => dp를 사용해서 연산 시간을 단축 => 성공 ! 
def solution(N, stages):

    stages.sort() # stage sort 
    answer = { x: 0 for x in range(1,N+2) } # stages에 1 ~ N+1까지 담겨있음 

    # stage마다 user count 
    for key,_ in answer.items():
        answer[key] = stages.count(key)

    # 실패율 
    result = []
    dp = [0]*(N+2)
    
    for i in range(N,0,-1):
        # 분자 : i번 도전 횟수 
        n_try = answer[i]
        
        # dp[i] = i보다 큰 수 
        dp[i] = answer[i+1] + dp[i+1]

        # 분모 : i보다 큰 수 + i번 도전 횟수 
        n_more = dp[i] + n_try
        
        try:
            result.append([n_try/n_more,i])
        except:
            # zero division
            result.append([0,i])     

    result.sort(key=lambda x :(-x[0],x[1]))

    return [i for _,i in result]


