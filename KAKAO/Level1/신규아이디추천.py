import re

def solution(new_id):

    # 01. 소문자 치환 
    answer = new_id.lower()

    # 02. 소문자, 숫자, -, _ . 제외한 모든 문자 제거 
    comp = re.compile('[^a-z0-9-_.]')
    answer = comp.sub('',answer)

    # 03. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    comp = re.compile('\.\.+')
    answer = comp.sub('.',answer)

    # 04. 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    comp = re.compile('^\.|\.$')
    answer = comp.sub('',answer)

    # 05. 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not len(answer): 
        answer = 'a'

    # 06. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.

    if len(answer) > 15:
        answer = answer[:15]

    comp = re.compile('\.$')
    answer = comp.sub('',answer)

    # 07. new_id의 길이가 2자 이하라면, 
    # new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    for i in range(3-len(answer)):
        answer = answer+answer[-1]   

    return answer


#---------------------- 정규 표현식 이해  --------------------# 

[a-zA-Z0-9]

\d == [0-9]
\D == [^0-9]
\s == whilespace 문자와 매치, [ \t\n\r\f\v]
\S == whiltespace 문자가 아닌것과 매치 == [^ \t\n\r\f\v]
\w == 문자 + 숫자와 매치 == [a-zA-Z0-9_]
\W == 문자 + 숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일

Dot(.) == \n을 제외한 모든 문자와 매치 
a.b == a+모든문자+b == aaaaaab acdsdfasgb (o)
a[.]b == a.b , a00000b (x)


반복(*) : 최소 0번 이상 반복
ca*t = caaaaaaaaaaaaat = ct = cat

반복(+) : 최소 1번 이상 반복
ca+t = cat = caat != ct

반복({m,n},?)
m부터 n까지 매치, 
{3,} : 반복횟수가 3 이상 
{,3} : 반복 횟수가 3 이하 
{1,} : +
{0,} : * 
ca{2}t = caat
ca{2,5}t = caat or caaat or caaaat or caaaaat 

? : {0,1}의 의미 
ab?c : b가 있어도 되고 없어도 된다의 의미 

import re

p = re.compile('ab*')

match() : 문자열 처음부터 정규식과 매치되는지 조사 
search() : 문자열 전체를 검색해 정규식과 매치되는지 조사
findall() : 매치되는 모든 문자열을 리스트로 돌려줌
finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다. 



p = re.compile('[a-z]+')
m = p.findall('3 python')
print(m)

