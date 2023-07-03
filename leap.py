Year=int(input("Enter the year:"))
if Year%4==0:
    print('This is a leap year')
else:
    print("This is not a leap year")
if Year%100==0:
    print("This is not a leap year")
elif Year%400==0:
    print("This is a leap year")