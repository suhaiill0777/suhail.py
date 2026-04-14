age = int(input("Enter your age: "))

if age < 12:
    print("Ticket Price: ₹100 (Child)")
elif age > 60:
    print("Ticket Price: ₹150 (Senior)")
else:
    print("Ticket Price: ₹200 (Adult)")