def check(age):
    if(age>=18):
        print("eligible for vote")
    elif(age<0):
        raise ValueError("place give age passtive number")
        print("your not eligible for vote ")
age = int(input("enter your age"))
check(age)