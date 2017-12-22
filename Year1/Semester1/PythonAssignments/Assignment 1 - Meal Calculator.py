#Program due September 17, 2015
#Coded by Kevin Lopez
#This program will calculate the total price of a meal after having the data entered by the user
#get the price and tips, force them to be floats because its only fun if i force my will on the code
price=float(input("Please enter the price"))
tip=float(input("Please enter the amount to tip"))
#this function is gonna set up all the values while doing calculations
#everything done in this code is in this function
def pricecalc():
    tax = (price*0.13)
    tax=round(tax,2)
    pricetax = (price*1.13)
    pricetax=round(pricetax,2)
    tipx=tip*0.01*price
    tipx=round(tipx,2)
    print("Meal",price)
    print("Tip",tipx)
    print("Tax",tax)
    final =float(tax+tipx+price)
    final=round(final,2)
    print("Total",final)
    return
#Calling the function does everything
pricecalc()
