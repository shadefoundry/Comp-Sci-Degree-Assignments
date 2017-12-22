__author__ = 'link491'
#Program due September 24, 2015
#Coded by Kevin Lopez
#Design and write a Python program which asks, from the user,
#information about the whether and then uses logic to inform the user on how to dress.
#From the user, you must ask for at least the following information:
#   The temperature (degrees C)
#   The wind speed (m/s)
#   The chance of precipitation (as a percentage)
#   The relative humidity (as a percentage)
#   Whether it is sunny (this can just be a boolean. Read in a value of True or False)

#From that information, inform the user on how to dress.
#Use logic and if-statements to decide what a user should wear, given any weather conditions.
#It is up to you to decide the logic for choosing.
#You must have at least 5 different conditions that you check.
#You must have a comment at the top of your .py file.

temp = int(input("What is the temperature? (in degrees celcius)"))
wind = int(input("What is the wind speed in m/s? (just a number will suffice)"))
rain = int(input("What is the chance of precipitation? (just a number will suffice)"))
humidity = int(input("What is the humidity %? (just a number will suffice)"))
sun = input("Is there sun? (y or n)")

#---------------------------------------------------------------------------------------------------------------------#
# All possibilities when it's cold                                                                                    #
#---------------------------------------------------------------------------------------------------------------------#

if 0>=temp:
    #shits cold
    if 0<=wind<=5:
        #shits not windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's pretty nice outside. It's sunny and there's no bullshit"
                          "but its still pretty cold, so you should wear a winter jacket"
                          "at the very least. Consider gloves as well.")
                else:
                    print("It's cold and grey outside. Wear a jacket and gloves.")
            else:
                #shits humid
                if sun == "y":
                    print("it's pretty sunny and really humid. There isn't too much"
                          "chance of precipitation or wind, but it is cold. You should"
                          "still wear a jacket at the very least, but gloves and face mask"
                          "are unnecessary.")
                else:
                    print("It's grey and humid... You must live in the paradox"
                          "dimension. Anyway, there's no rain or wind, but it's still"
                          "cold, so wear a jacket and gloves.")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("sunny, not humid, rainy, not windy, cold")
                    print("Oh great, another resident in the paradox dimension."
                          "Wear a jacket, boots and gloves.")
                else:
                    print("not sunny, not humid, rainy, not windy, cold")
                    print("It's cold and theres precipitation, wear a jacket"
                          "gloves and a hat")
            else:
                #shits humid
                if sun == "y":
                    print("Oh great, another resident in the paradox dimension."
                          "Wear a jacket, boots and gloves.")
                else:
                    print("It's cold and theres precipitation, wear a jacket"
                          "gloves and a hat")
    else:
        #shits windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's cold and windy, nothing else matters."
                          "Wear a face mask, jacket and gloves.")
                else:
                    print("It's cold and windy, nothing else matters."
                          "Wear a face mask, jacket and gloves.")
            else:
                #shits humid
                if sun == "y":
                    print("It's cold, wet and sunny. Wear boots and a winter jacket.")
                else:
                    print("Today is a miserable day. Wear boots gloves and a jacket.")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("Oh great, another resident in the paradox dimension."
                          "Wear a jacket, boots and gloves.")
                else:
                    print("Oh boy, the worst kind of day. You'd be better off just staying inside,"
                          "but if you MUST go out, I'd recommend boots, gloves, a jacket, a face mask and"
                          "a couple shots of whiskey.")
            else:
                #shits humid
                if sun == "y":
                    print("Oh great, another resident in the paradox dimension."
                          "Wear a jacket, boots and gloves.")
                else:
                    print("Its cold, windy and wet. Wear a hat, some gloves, a jacket"
                          "and boots.")

#---------------------------------------------------------------------------------------------------------------------#
# All possibilities when it's chilly                                                                                  #
#---------------------------------------------------------------------------------------------------------------------#

if 14>=temp>0:
    #shits chilly
    if 0<=wind<=5:
        #shits not windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's not too bad outside, you could do with a pair of jeans"
                          "and a t-shirt")
                else:
                    print("It's not too bad outside, you could do with a pair of jeans"
                          "and a t-shirt")
            else:
                #shits humid
                if sun == "y":
                    print("It's not too bad outside, you could do with a pair of jeans"
                          "and a t-shirt")
                else:
                    print("It's not too bad outside, you could do with a pair of jeans"
                          "and a t-shirt")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's not too bad outside, a sweater and umbrella will do fine.")
                else:
                    print("It's not too bad outside, a sweater and umbrella will do fine.")
            else:
                #shits humid
                if sun == "y":
                    print("It's not too bad outside, a sweater and umbrella will do fine.")
                else:
                    print("It's not too bad outside, a sweater and umbrella will do fine.")
    else:
        #shits windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's pretty nice out there, jeans and a t-shirt will be fine")
                else:
                    print("It's pretty nice out there, jeans and a t-shirt will be fine")
            else:
                #shits humid
                if sun == "y":
                    print("It's pretty nice out there, jeans and a t-shirt will be fine")
                else:
                    print("It's pretty nice out there, jeans and a t-shirt will be fine")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's not too bad outside, an umbrella will do fine.")
                else:
                    print("It's not too bad outside, a sweater and umbrella will do fine.")
            else:
                #shits humid
                if sun == "y":
                    print("It's not too bad outside, an umbrella will do fine.")
                else:
                    print("It's not too bad outside, an umbrella will do fine.")

#---------------------------------------------------------------------------------------------------------------------#
# All possibilities when it's warm                                                                                    #
#---------------------------------------------------------------------------------------------------------------------#

if 14>=temp>0:
    #shits chilly
    if 0<=wind<=5:
        #shits not windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
                else:
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
            else:
                #shits humid
                if sun == "y":
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
                else:
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
                else:
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
            else:
                #shits humid
                if sun == "y":
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
                else:
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
    else:
        #shits windy
        if 49>=rain>=0:
            #shits not rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
                else:
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
            else:
                #shits humid
                if sun == "y":
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
                else:
                    print("It's a retty nice day! You can wear shorts and a t-shirt!")
        else:
            #shits rainy
            if 0<=humidity<=30:
                #shits not humid
                if sun == "y":
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
                else:
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
            else:
                #shits humid
                if sun == "y":
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
                else:
                    print("It's pretty warm but rainy, bring shorts and a t-shirt and an umbrella")
