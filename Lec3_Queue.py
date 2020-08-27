# In this lecture we are going to learn about the implimentation of queues in python
# We cannot use the already present append function to add values because it adds values at the right side of the list which is not compatible with the FIFO (First in First Out) for Queues
# So we need aother method/function which can add value at the left side of list in python

from collections import deque

x = [5,6,7,8,9]
x.append(10)
print(x)

y = deque()
y.appendleft(5)
y.appendleft(6)
y.appendleft(7)
y.appendleft(10)
y.pop()

print(y)

# queue = deque()
# queue.appendleft("Mango")
# print(queue)
