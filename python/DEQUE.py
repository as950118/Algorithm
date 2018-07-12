from collections import deque

Deque = deque([0])
print(Deque)
Deque.append(1)
print("Deque Right Append :\t", Deque)
Deque.appendleft(-1)
print("Deque Left Append :\t", Deque)
Deque.extend([2, 3])
print("Deque Right Extend :\t", Deque)
Deque.extendleft([-2, -3])#WARING ## extnedleft[-3, -2] ==> [-2, -3, ~~ ]
print("Deque Left Extend :\t", Deque)
Deque.remove(0)#Value, Not Position
print("Deque Remove Value :\t", Deque)
Deque_Right = Deque.pop()#No Arguments, Last Right Value Pop and Remove
print("Deque Right Pop :\t", Deque, "\tDeque Right :\t", Deque_Right)
Deque_Left = Deque.popleft()#No Arguments, Last Left Value Pop and Remove
print("Deque Left Pop :\t", Deque, "\t\tDeque Left :\t", Deque_Left)
Deque.rotate(1)
print("Deque Rotate :\t\t", Deque)
Deque.rotate(1)
print("Deque Rotate :\t\t", Deque)
Deque.rotate(-1)
print("Deque Rotate :\t\t", Deque)
Deque.rotate(-1)
print("Deque Rotate :\t\t", Deque)
