input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
def findlargest(a,b):
    if a>b:
        return a
    else:
        return b

result = findlargest(input1, input2)
print("The largest number is:", result)
