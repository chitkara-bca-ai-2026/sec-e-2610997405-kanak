 
# student fee calculator 
name = input("enter the name of the student: ")
dep = input("enter the department of the student: ")
roll_no = int(input("enter the roll no of the student: "))
t_fees =  int(input("enter the tution fees of the student: "))
e_fees = int(input("enter the examination fees of the student: "))
lib_fees = int(input("enter the library fees of the student: "))
total_fees = t_fees + e_fees + lib_fees
print("total fees: ",total_fees)
discount = int(input("enter the discount provided: "))
fees_after_discount = total_fees - discount
print("fees after discount: ",fees_after_discount)
anual_fees = fees_after_discount * 2
print("anual fees: ",anual_fees)
monthly_fees = anual_fees//12
print("monthly fees: ",monthly_fees)

 