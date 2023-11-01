l=[10,20,30,40,50]
u=[]
for i in l:
    if i not in u and l.count(i)==l:
        u.append(i)
print(list(u))        
        
