## stack => push, peek, pop 

# stack 구현 
class Stack(list):
    
    push = list.append  
    # stack의 가장 마지막에 있는 데이터 보여주는 함수
    def peek(self):
        return self[-1]


s = Stack()
s.push(1)
s.push(5)
s.push(10)

print("my stack is :",s) # my stack is : [1, 5, 10]
print("Popped value is :",s.pop()) # Popped value is : 10
print("my stack is :",s) # my stack is : [1, 5]
print("peeked value is :",s.peek())

# stack의 활용 
'''
example 1) 페이지 담기 

    이전페이지      현재페이지      다음페이지
                    네이버
    네이버          구글
    네이버 구글     유튜브
    네이버          구글            유튜브
                    네이버          유튜브 구글

example 2) 깊이우선 탐색(DFS) '''