"""
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 
다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    
    total_time = 0 # 걸리는 total 시간 
    qSum = 0 # 다리 weight 

    while truck_weights:
        qSum -= q.popleft() # 빠져나온 트럭 무게 제거 
        total_time+=1 # 트럭은 1씩 움직이므로,  while문이 돌아가는 시간 만큼 time 추가

        if (qSum + truck_weights[0])>weight: # 현재 다리 weight + 다음 트럭 무게가 weight를 넘으면
            q.append(0) # 다리에 다음 트럭 올라갈 수 없으므로 0을 추가 

        else:# 다음 트럭이 올라갈 수 있으면 
            next = truck_weights.pop(0) # 다음 트럭 나옴
            qSum += next  # 다음 트럭 무게 추가 
            q.append(next) # 다음 트럭 queue에 추가 
    
    return total_time + len(q) # 다리를 빠져오지 못한 트럭 + total 시간 


