name=input("enter file name")
file=open(name,"r")
a=file.read()
c=[]
for i in a:
    if(i not in "aeiouAEIOU"):
        b=i
        c+=[b]
name1=input("enter file name")
file1=open(name1,"w")
file1.write(c)
file1.close()
