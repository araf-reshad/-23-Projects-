year = int(input("Enter a year: "))

if (year > 10000 and (year % 10000) % 2800 == 0):  
    print(str(year) + " is NOT a leap year.")  

elif (year % 400 == 0):
    print(str(year) + " is a leap year.")

elif (year % 100 == 0):
    print(str(year) + " is NOT a leap year.")

elif (year % 4 == 0):
    print(str(year) + " is a leap year.")

else:
    print(str(year) + " is NOT a leap year.")
