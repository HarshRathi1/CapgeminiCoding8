'''Write a program with a function rotate(arr[],d,n) that rotates arr of size n by d elements
input:
n=6
arr=[3,9,2,6,24,11]
d=2
output:
24 11 3 9 2 6(Rotating two time)'''
n=int(input())
arr=list(i for i in input().split())
d=int(input())
def rotate(arr,d,n):
    a = []
    for i in range(n):
        a.append(arr[i - d])
    return a
print(rotate(arr,d,n))