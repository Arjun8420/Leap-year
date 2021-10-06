#Program to check if a given number is Leap Year or not

Year = int(input("Enter the Year = "))

if((Year%4) == 0 and (Year%100) != 0) or ((Year%100) == 0 and (Year%400) == 0) :
    print(Year,"is a Leap Year")
else :
    print(Year,"is not a Leap Year")
