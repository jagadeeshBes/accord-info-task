name=input("enter file name")
cont=input("enter contant")
file=open(name,"a")
file.write(cont)
file.close()