# Queue  => put, peek get - FIFO

# 직접 구현

class Queue(list):
    put = list.append
    
    def peek(self):
        return self[0]
        
    def get(self):
        return self.pop(0)


q = Queue()
q.put(1)
q.put(5)
q.put(10)

print("my queue is : ", q) # my queue is :  [1, 5, 10]
print("removed value is :",  q.get()) # removed value is : 1
print("my queue is : ", q) # my queue is :  [5, 10]
print("peeked value is :", q.peek()) # peeked value is : 5
print("my queue is : ", q) # my queue is :  [5, 10]


# python 구현된 클래스 import 

from queue import Queue

q = Queue()
q.put(1)
q.put(5)
q.put(10)
print("my queue is :",q) # my queue is : <queue.Queue object at 0x000001ECBF0CDF60>
print("removed value is :",q.get()) # removed value is : 1
print("my queue is :",q) # my queue is : <queue.Queue object at 0x000001ECBF0CDF60>
print("peeked value is :", q.peek()) # peeked value is : 5
print("my queue is :",q) # my queue is : <queue.Queue object at 0x000001ECBF0CDF60>

# python list를 큐로 활용 

q = []
# put
q.append(1)
q.append(5)
q.append(10)


print("my queue is :",q) 
print("removed value is :",q.pop(0)) # removed value is : 1
print("my queue is :",q) 
print("peeked value is :", q[0] ) # peeked value is : 5
print("my queue is :",q) 


# Queue의 활용 
'''
example 1) 프린터 인쇄 대기열
    1) 문서 1
    2) 문서 2
    3) 문서 3
    -> 문서 3  문서 2  문서 1

example 2) 너비우선 탐색(BFS) '''