"""
description: https://www.hackerrank.com/challenges/ctci-bubble-sort
"""

def fibonacci(n):
    # Write your code here.
    if n==0:
        return 0
    if n==2 or n==1:
        return 1


    else:
        l=[]
        l.append(0)
        l.append(1)
        l.append(1)
        for i in range(3,n+1):
            l.append(l[i-1]+l[i-2])
        return l[n]
n = int(input())
print(fibonacci(n))