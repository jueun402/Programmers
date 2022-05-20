def solution(record):
    userInfo = {} # user의 정보를 담는 dictionary 
    result = [] # action 결과 
    
    # action에 따라 user의 id를 담고(enter or leave), 변경(change)한다.
    for r in record:
        act = r.split(" ")
        
        if act[0] == 'Enter':
            user, name = act[1], act[2]
            userInfo[user] = name
            result.append([act[0],user]) # act, userid
    
        elif act[0] == 'Change':
            user,name = act[1], act[2]
            userInfo[user] = name  # user의 이름을 변경해준다. 
        
        else: # leave
            user = act[1]
            result.append([act[0],user]) # act, userid
            
    # action 결과를 출력해준다. 
    answer = []
    for r in result:
        act, user= r
        if act =='Enter':  answer.append(userInfo[user]+"님이 들어왔습니다.")
        elif act =='Leave':  answer.append(userInfo[user]+"님이 나갔습니다.")
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)
#-----------------문제 설명 ----------------------------
# 카카오 코테를 풀면서 느끼는 점은, 문제를 잘 이해하면 풀이가 쉬워진다는 것이다! 
# 백준을 풀면서 이해가 안가서 한참을 고민하다가 못 푼 문제가 많았는데, 카카오는 굉장히 친절하다. 카카오 사랑합니다.
 
''''

1. 가상의 닉네임 
2. [닉네임] 님이 들어옴 => [닉네임] 님이 나감 
3. 닉네임 변경 
    - 채팅방 나감 => 새로운 닉네임
    - 채팅방에서 닉네임 변경 
    - 기존에 채팅방에 출력 닉네임도 전부 변경 

muzi 들어옴
prodo 들어옴 
muzi 나감 

muzi 나간후 prodo로 들어옴 
prodo 님이 들어옴
prodo 님이 들어옴 (찐프로도)
prodo 님이 나감 
prodo 님이 들어옴 

이름 중복 허용해줌 

prodo가 ryan으로 이름 변경 

prodo 님이 들어옴
ryan 님이 들어옴 (찐프로도)
prodo 님이 나감 
prodo 님이 들어옴 

==> 닉네임 변경 기록이 담긴 문자열 배열 record가 매개변수로 주엉짐 
==> 최종적으로 방 개설 사람이 보게되는 문자열 배열 형태로 return 


record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]	


result = ["Prodo님이 들어왔습니다.", 
            "Ryan님이 들어왔습니다.", 
            "Prodo님이 나갔습니다.", 
            "Prodo님이 들어왔습니다."]
'''

