a="suhail"
print(a)

age=20
print(age)

num=14.5
print(num)


b=[1,2,3,4,5]
print(b[-1])
b.append(6)
print(b)
b.insert(0,0)
print(b)
b.pop(2)
print(b)
b.pop(0)
print(b)
c=("apple,banana,grapes")
print(c)
d=list(c)
d.append("orange")
print(c)

Age=25
if Age>=18:
    print("you can vote.")
else:  
    print("you cannot vote.")

Age=int(input("enter your age:"))
if (Age>=18):
    print("you can vote.")
else:
    print("you cannot vote.")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if (num1>num2) and (num1>num3):
    print("the largest number is:",num1)
elif (num2>num1) and (num2>num3):
    print("the largest number is:",num2)
else:
    print("the largest number is:",num3)

