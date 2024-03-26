a=20
for i in range(2,a+1):
    c=0
    for j in range(i):
        if(i%j==0):
            c=1
            break
    if(i>1 and c == 0):
        print(i)
