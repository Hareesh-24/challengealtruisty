def count_treasures(s):
    x=list()
    q = int(input("no.of queries:"))
    for i in range(q):
        start,end=map(int, input().split())
        x.append(s[start-1:end].count('T' or 't'))
    for i in range(len(x)):
        print(x[i])

s = input("enter the string:").strip()
count_treasures(s)

