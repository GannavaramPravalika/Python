N=int(input())
5
 if(N % 2 != 0):
...     print("Weird")
... else:
...     if(N % 2 == 0 and N >= 2 and N <= 5):
...              print("Not Weird")
...     elif(N % 2 == 0 and N >= 6 and N <= 20):
...             print("Weird")
...     elif(N % 2 == 0 and N > 20):
...             print("Not Weird")
...
Not Weird