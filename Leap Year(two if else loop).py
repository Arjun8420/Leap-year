#Program to check if the input year is a leap year or not

Year = int(input("Enter the Year = "))

if (Year%4) == 0 and (Year%100) != 0 :
    print(Year,"is a Leap Year")
else :
    if ((Year%100) == 0) and ((Year%400) == 0) :
        print(Year,"is a Leap Year")
    else :
        print(Year,"is not a Leap Year")
        
