def min_swap(a,b):
    swap=0
    if sorted(a)!=sorted(b):
        return -1
    u=len(a)
    c=list(a)
    for i in range(u):
        if c[i]!=b[i]:
            j=i
            while j<n and c[j]!=b[i]:
                j+=1
            while j>i:
                c[j],c[j-1]=c[j-1],c[j]
                j-=1
                swap+=1
    return swap





n=int(input())
a=input().strip()
b=input().strip()
z=min_swap(a,b)
print(z)
