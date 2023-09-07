from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque(range(1,N+1))

list1 = deque()
while len(queue)>0:
    list1.append(queue.popleft())
    if len(queue)>=1:
        queue.append(queue.popleft())
    if len(queue)==1: 
        list1.append(queue.popleft())
        break
    
print(*list1)