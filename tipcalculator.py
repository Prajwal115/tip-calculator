#importing time
import time
#Tip calculator made by Prajwal
print("You just had your lunch, now it's time for the billing")
#taking in the bill using input function and converting it to float
bill = float(input("Please enter the bill amount you have to pay: $ "))
ten = 10/100*bill
fif = 15/100*bill
twe = 20/100*bill

print(f"Please choose a tip percentage - 10% ({ten:.2f}) / 15% ({fif:.2f}) / 20% ({twe:.2f})")

tip = float(input("Enter the tip amount: $ "))
if tip != ten or tip !=fif or tip !=twe:
    print("Invalid amount")

else:
    total = tip+bill
    print("Thanks for your visit here, we will be back with your bill in a few seconds ")
    time.sleep(1)
    print(3*".")
    time.sleep(1)
    print(5*".")
    time.sleep(1)
    print(7*".")
    time.sleep(1)
    print(f"The total bill was: ${bill} and the tip payable is {tip}\nThe total amount payable is ${total:.2f}")
