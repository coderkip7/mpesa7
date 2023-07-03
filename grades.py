marks=int(input("Enter students score:"))
if marks>80 and marks<=100:
    print("You scored an A")
elif marks >60 and marks<=80:
    print("You scored a B")
elif marks>50 and marks<=60:
    print('You scored a C')
elif marks>40 and marks<=50:
    print("You scored a D")
elif marks>0 and marks<=40:
    print("Wachana na shule bana!!!!")
else:
    print("Wrong input")


#create a python program to check if a given year is leap
#The year is divisible by 4 but not 100
#except if its also divisible by 400
