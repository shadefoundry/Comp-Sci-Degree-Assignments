__author__ = 'link491'
#Write a Tkinter GUI program which allows the user to convert either Fahrenheit to Celsius or Celsius to Fahrenheit, at the user's choosing.

#The GUI program will consist of a single window. That window will consist of:
# -Two radio buttons. One radio button will be labelled "Celsius to Fahrenheit" and the other will be labelled
# "Fahrenheit to Celsius". Only one radio button be selected at any given time.
# -One text entry field with a label beside it, where the user is to type in the temperature they want to convert.
# -Another text entry field, which is where the output of the calculation should be displayed.
# -A button, which is the user is to press when the user wants to perform a conversion.

#Any time the user clicks the button, your program should perform a conversion calculation
#(according to the user's radio button) and display the result in the output text field.

#Your program should be impossible to crash. In the case that the user enters in
#an invalid input (for instance, something which is not an integer), you should display an error message, but should not crash.
from tkinter import *
from tkinter import messagebox

root = Tk()
root.wm_title("Temperature Converter v1.02")

radio_value = IntVar()
v = StringVar()
#the label of the initial input box has 3 spaces at the end of it so you can see my glorious title without
#having to resize the sodding window.
Label(root,text='Enter Temperature as an Integer   ').grid(row=0,column=0)
temperature = Entry(root,textvariable=v)
temperature.grid(row=0,column=1)

temp_input = Entry(root)
temp_input.grid(row=2,column=1)

def calculate_temperature():
    #try the actual code first
    try:
        #set our base temperature
        temptemp= int(v.get())
        change = radio_value.get()
        #if the value of the radio button is 1 we convert from farenheit to celcius
        if change == 1:
            temp_output=round((temptemp * (9/5) + 32))
            temp_input.delete(0, len(temp_input.get()))
            temp_input.insert(0,str(temp_output))
        #otherwise we convert farenheit to celcius
        if change == 2:
            temp_output = round((temptemp - 32) * (5/9))
            temp_input.delete(0, len(temp_input.get()))
            temp_input.insert(0,str(temp_output))
    #if shit hits the fan (which it quite often does)...
    except Exception:
        #we clear out the output window...
        temp_input.delete(0, len(temp_input.get()))
        #... and yell at the clearly retarded user for putting in an invalid value!
        messagebox.showerror('Error','God dammit! I thought I told you to enter an integer!')

c2f = Radiobutton(root,text="Celsius to Fahrenheit", variable=radio_value, value=1).grid(row=1,column=0)
f2c = Radiobutton(root,text="Fahrenheit to Celsius", variable=radio_value, value=2).grid(row=1,column=1)
b = Button(root,text='Calculate',command=calculate_temperature).grid(row=2,column=0)


root.mainloop()

#                                   ||`-.___
#                                   ||    _.>
#                                   ||_.-'
#               ==========================================
#                `.:::::::.       `:::::::.       `:::::::.
#                  \:::::::.        :::::::.        :::::::\
#                   L:::::::         :::::::         :::::::L
#                   J::::::::        ::::::::        :::::::J
#                    F:::::::        ::::::::        ::::::::L
#                    |:::::::        ::::::::        ::::::::|
#                    |:::::::        ::::::::        ::::::::|     .---.
#                    |:::::::        ::::::::        ::::::::|    /(@  o`.
#                    |:::::::        ::::::::        ::::::::|   |    /^^^
#     __             |:::::::        ::::::::        ::::::::|    \ . \vvv
#   .'_ \            |:::::::        ::::::::        ::::::::|     \ `--'
#   (( ) |           |:::::::        ::::::::        ::::::::|      \ `.
#    `/ /            |:::::::        ::::::::        ::::::::|       L  \
#    / /             |:::::::        ::::::::        ::::::::|       |   \
#   J J              |:::::::        ::::::::        ::::::::|       |    L
#   | |              |:::::::        ::::::::        ::::::::|       |    |
#   | |              |:::::::        ::::::::        ::::::::|       F    |
#   | J\             F:::::::        ::::::::        ::::::::F      /     |
#   |  L\           J::::::::       .::::::::       .:::::::J      /      F
#   J  J `.     .   F:::::::        ::::::::        ::::::::F    .'      J
#    L  \  `.  //  /:::::::'      .::::::::'      .::::::::/   .'        F
#    J   `.  `//_..---.   .---.   .---.   .---.   .---.   <---<         J
#     L    `-//_=/  _  \=/  _  \=/  _  \=/  _  \=/  _  \=/  _  \       /
#     J     /|  |  (_)  |  (_)  |  (_)  |  (_)  |  (_)  |  (_)  |     /
#      \   / |   \     //\     //\     //\     //\     //\     /    .'
#       \ / /     `---//  `---//  `---//  `---//  `---//  `---'   .'
#________/_/_________//______//______//______//______//_________.'_________
###VK######################################################################