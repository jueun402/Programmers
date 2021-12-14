# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    first = [1, 2, 3, 4, 5]*2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] *1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000


    cnt = [0,0,0,0]

    for i in range(len(answers)):
        if answers[i] == first[i]:
            cnt[1] +=1 
        if answers[i] == second[i]:
            cnt[2] +=1
        if answers[i] == third[i]:
            cnt[3] +=1 

    result = []
    for i in range(1,4):
        if cnt[i] == max(cnt):
            result.append(i)

    return result