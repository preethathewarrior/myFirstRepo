#program to check a number can be divided by 4 before it is less than or
# equal to 12
num=int(input("Enter the number:"))
while num<13:
    if num%4==0:
        print(num,",","is divisible by 4")
        break
    else:
        print("not divisible by 4")
        break
    num+=4


