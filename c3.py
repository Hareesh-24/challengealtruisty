def max_bright(arr,k):
    x=arr.copy()
    max_value=0
    x.sort(reverse=True)
    return x[k-1]


arr=[]
k=int(input())
n=int(input())
for i in range(n):
    arr.append(int(input()))
v=max_bright(arr,k)
print(v)
