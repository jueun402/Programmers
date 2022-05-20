
from collections import defaultdict

def solution(id_list, report, k):
    key =  list(map(lambda x : x.split()[0], report)) # 신고자
    value = list(map(lambda x : x.split()[1], report))  # 신고당한 유저 

    repo_dict = defaultdict(list) # 신고 report 
    stop_user = defaultdict(list) # 정지 유저 

    for i,v in zip(key,value):
        # 이미 동일한 유저를 신고했다면 continue 
        if v in repo_dict[i]:
            continue     
        
        repo_dict[i].append(v)
        stop_user[v].append(i)

    result = {}.fromkeys(id_list,0)

    # stop user를 지목한 user의 길이를 구하자         
    for usr in list(stop_user.items()):
        if len(usr[1])>=k:
            for i in usr[1]:
                result[i] +=1        

    return list(result.values())

#----------------------다른 사람 풀이 참고하기 --------------------# 
# 01. set 활용한 풀이 

id_list = ['muzi', 'frodo', 'apeach', 'neo']
report = ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi', 'apeach muzi']
k=2

answer = [0]*len(id_list)
reports = {x : 0 for x in id_list} # 이렇게 dictionary를 만들 수 있구나!!! 

# 신고 횟수 파악
# set(report)는 천재...이신건가..?
# muzi가 frodo 고르고 또 고르면 report에서 똑같이 나올테니까 set으로 중복 제거,, 
for r in set(report):
    reports[r.split()[1]] +=1

for r in set(report):
    # 신고 횟수가 k번 이상이라면 
    if reports[r.split()[1]] >=k:
        # r.split()[1]을 고른 신고자의 index를 찾아 
        # answer의 인덱스에 넣고 +1 해주기 
        answer[id_list.index(r.split()[0])] += 1
    
print(answer)

# 02. 내 풀이랑 비슷한데 더 효율적인 방법

answer = {x : 0 for x in id_list}
dict = {x : [] for x in id_list}  # key (신고당한사람) : value (신고자) 

for re in report:
    key = re.split()[0]
    val = re.split()[1]
    
    if key not in dict[val]:
        dict[val] = dict[val]+[key]

for id in id_list:
    if len(dict[id]) >=k:
        for i in dict[id]:
            answer[i]+=1
        
list(answer.values())