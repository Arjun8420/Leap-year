#Program to check if a given year is leap year or not

Year = int(input("Enter the Year = "))

if Year%4 == 0 :
    if Year%100 == 0 :
        if Year%400 == 0:
            print(Year,"is a Leap Year")
        else:
            print(Year,"is not a Leap Year")
    else:
        print(Year,"is not a Leap Year")
else:
    print(Year,"is not a Leap Year")
