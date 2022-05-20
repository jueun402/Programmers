# 내 풀이 
import re

def solution(s):
    str_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num_dict = {j:i for i,j in enumerate(str_num)}  # {'zero' : 0, 'one' : 1 ... } 이런 딕셔너리 생성  

    # 숫자가 영어로 표기되어 있는 문자 찾기 
    for num in str_num:
        if num in s:
            # 영어 숫자를 숫자로 변환하기 
            s = re.sub(num, str(num_dict[num]), s)

    return int(s)
#----------------------다른 사람 풀이---------------------------

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    # 딕셔너리를 바로 사용했네! 
    for key, value in num_dic.items():
        # replace를 사용...! 하나 방법 알았따. 
        answer = answer.replace(key, value)
    return int(answer)

#------------------------내 풀이 개선 -------------

def solution(s):
    str_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num_dict = {j:i for i,j in enumerate(str_num)}  # {'zero' : 0, 'one' : 1 ... } 이런 딕셔너리 생성  

    for k, v in num_dict.items():
        s = s.replace(k, v) # s에 있는 key값을 value값으로 바꿔라 
    
    return int(s)