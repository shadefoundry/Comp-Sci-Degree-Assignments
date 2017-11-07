#Program due September 17, 2015
#Coded by Kevin Lopez, ~link491
#Define a Drink
class Drink:
    def __init__(self,sugar,calories=3.87):
        self.sugar=sugar
#Determine the number of calories and return the value
    def num_calories(self):
        self.calories = self.sugar*3.87
        return self.calories
#Define an alchoholic drink
class Alcoholic(Drink):
    def __init__(self,sugar,alcohol):
        self.alcohol=alcohol
        self.sugar=sugar
#Determine the number of calories and return the value
    def num_calories(self):
        self.calories=self.sugar*3.87+self.alcohol*7
        return self.calories

#What kind of drink does the user want? Must be exact inputs as we haven't actually done error checking yet
drink=input("What kind of drink do you want? (Alchoholic or Non-Alcoholic)")
#How do we handle each input?
if drink=='Alchoholic':
    s = int(input("How much sugar (in grams) is there in the drink?"))
    a = int(input("How much alchohol (in grams) is in the drink?"))
    d = Alcoholic(s,a)
    print(d.num_calories(),"calories")
elif drink=='Non-Alchoholic':
    s = int(input("How much sugar (in grams) is there in the drink?"))
    d = Drink(s)
    print("There are",d.num_calories(),"calories in your",drink,"drink.")
