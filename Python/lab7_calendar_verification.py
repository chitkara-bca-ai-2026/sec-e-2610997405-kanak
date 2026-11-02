# CALENDAR VERIFICATION SYSTEM

print("===============================")
print(" CALENDAR VERIFICATION SYSTEM")
print("===============================")

year = int(input("enter the year: "))
if year<=0:
    print("invalid year! must be positive")
else: 
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("leap year")
            else:
                print("common year")
                print("reason : century year but not divisible by 400 ")      
        else:
            print("leap year")
            print("reason : divisible by 4 but not century year")
    else:
        print("common year")
        print("reason : not divisible by 4")
    if year=="leap year":
        print("february has 29 days ")
        print("this year hase 366 days ")
    else:
        print("february has 28 days")
        print("this year has 365 days")        

        
        

 

 
