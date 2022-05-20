# 후기 : 고생했다...

def solution(s):
    
    # 5번 test case, 
    # s의 길이가 1일때 1을 return해줘야 한다. ㅠㅠ 
    if len(s) == 1:
        return 1
    
    # 최댓값 설정 
    answer = 10**10

    # 1~ s//2만큼의 간격으로 나눠서 압축 문자열 확인 
    for i in range(1,len(s)//2+1):
        ans = []	
        before = s[0:i] # 초기값 
        k ,cnt = i, 1 # k = i부터 시작 , cnt = 1부터 시작  
        ans.append([cnt,before]) 
        

        for j in range(i+k,len(s)+i,i): # i+k부터 len(s)+i까지 문자열 압축 
            now = s[k:j] # 현재값
            k = j   # 간격 조절 
            
            # 직전 값과 현재 값이 동일하면 
            if now == before:
                cnt = ans[-1][0] +1 # 직전값의 cnt +1  
                before = now  # before을 now로 변경 
                ans[-1] = [cnt,before]   # 직전값을 현재값으로 변경
                continue
            
            # 직전값과 현재값이 다르면 
            else: 
                cnt = 1 # cnt를 1로 변경 
                before = now # before를 now로 변경하고 
                ans.append([cnt,now]) # 새로운 수 부터 문자열 check 
             
        # 압축한 문자열 몇 개 있는지 check    
        result = 0
        for a in ans:
            if a[0] == 1: result +=len(a[1]) # cnt에 1이 있으면 count하지 x
            # 여기서 주의해야 할 것 : cnt가 10일 경우 압축 문자열의 길이는 2이다. 
            else: result +=len(a[1])+len(str(a[0])) # cnt의 문자까지 count 
                    
        # 작은 경우의 수를 check 
        answer = min(result, answer)
        # print(ans,answer)
    
    return answer

#-----------------------------------test-----------------------
s = "xxxxxxxxxxyyy" # 6 
s = 'a' # 1
solution(s)

