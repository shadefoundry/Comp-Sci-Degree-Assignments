#Program due November 5, 2015
#Coded by Kevin Lopez, ~link491

#Does everything required by the commands given

# Check how many numbers are greater than the input
def num_greater_than(xs,y):
    num = 0
    for i in xs:
        if y<i:
            num+=1
            i+=1
        else:
            i+=1
    return num

# Give a sum of the elements that are less than the input
def sum_of_elements_less_than(xs,y):
    sum=0
    for j in xs:
        if y>j:
            sum+=j
            j+=1
        else:
           j+=1
    return sum

# Check the lists for consecutive duplicates of the current number
def contains_consecutive_duplicates(xs):
    previous=0
    truth=0
    for h in xs:
        if h==previous:
            truth=True
            break
        else:
            truth=False
            previous=h
    return truth

# This be some dank sorcery shit where we add the sum of every nth number together
def sum_of_every_nth(xs,y):
    sum=0
    for a in range (0,len(xs),y):
        sum += xs[a]
    return sum

# This be some more dank sorcery that's going to check the closest value to the already rounded average
def closest_to_average(xs):
    sum=0
    numList=0
    for i in xs:
        sum+=i
        numList+=1
    average=round(sum/numList)
    return min(xs,key=lambda x:abs(x-average))

# Check for the largest even number in the list
def biggest_even_number(xs):
    previous=0
    temp = 0
    for i in xs:
        if i%2 == 0:
            temp = i
            if temp>previous:
                previous = temp
    return previous

# This be even MORE dank sorcery that checks for numbers that occur only one time through the list.
def count_numbers_which_occur_only_once(xs):
    x=0
    for i in xs:
        if xs.count(i) == 1:
            x+=1
    return x

l1 = [29,-13,-6,28,7,26,-1,21,12,-7,17,16,22,31,17,9,12,1,35,6]
l2 = [9,-3,26,19,30,1,-5,3,28,27,-13,-6,28,9,26,-1,21,12,-7,17,16,22,31,17,9,13,1,30,6,15,12,11,27,-14,-4,5,2,-12,23,27,30,7,18,24,13,-8,20,31,19,28,-4,33,15,-8,15,-11,2,13,17,23,-6,26,0,18,27,-7,-12,26,-4,9,19,-9,13,34,12,-8,-9,-2,-12,8,-9,31,6,4,-12,18,8,5,-4,22,-7,-13,14,8,3,6,16,6,-2,27,19,30,1,-5,3,28,27,-13,-6,28,9,26,-1,21,12,-7,17,16,22,31,17,9,13,1,30,6,15,12,12,27,-14,-4,5,2,-12,13,27,30,17,18,24,13,-8,10,41,19,28,-4,13,15,-8,15,-11,2,13,17,23,-6,26,0,14,27,-7,-12,26,-4,9,19,-9,13,34,12,-8,-9,-2,-12,8,-9,31,6,4,-12,18,8,5,-4,22,-7,-13,14,8,3,6,16,6,-2,27,12,14,16]

print(num_greater_than(l1, 5))      # correct output: 15
print(num_greater_than(l2, 0))      # correct output: 143
print(sum_of_elements_less_than(l1, 2))     # correct output: -26
print(sum_of_elements_less_than(l2, 3))     # correct output: -409
print(contains_consecutive_duplicates(l1))  # correct output: False
print(contains_consecutive_duplicates(l2))  # correct output: True
print(sum_of_every_nth(l1, 3))      # correct output: 115
print(sum_of_every_nth(l2, 6))      # correct output: 225
print(closest_to_average(l1))       # correct output: 12
print(closest_to_average(l2))       # correct output: 10
print(biggest_even_number(l1))  # correct output: 28
print(biggest_even_number(l2))  # correct output: 34
print(count_numbers_which_occur_only_once(l1))  # correct output: 16
print(count_numbers_which_occur_only_once(l2))  # correct output: 7

# Thar be Dank Sorcery at work in these waters, lads
#                                       ..
#                                     .(  )`-._
#                                   .'  ||     `._
#                                 .'    ||        `.
#                              .'       ||          `._
#                           .'        _||_            `-.
#                         .'          |====|              `..
#                       .'             \__/               (  )
#                     ( )               ||          _      ||
#                     /|\               ||       .-` \     ||
#                   .' | '              ||   _.-'    |     ||
#                  /   |\ \             || .'   `.__.'     ||   _.-..
#                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
#                \  .' |  |        .-.`    `./      _.-`.    `._.-'
#                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
#                .'    |   |  :   `._..-'.'        `._..'  ||
#               /      |   \  `-._.'    ||                 ||
#              |     .'|`.  |           ||_.--.-._         ||
#              '    /  |  \ \       __.--'\    `. :        ||
#               \  .'  |   \|   ..-'   \   `._-._.'        ||
#`.._            |/    |    `.  \  \    `._.-              ||
#    `-.._       /     |      \  `-.'_.--'                 ||
#         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
#              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
#                  [`--^-..._.'        | |       /....../|  __   __  |
#                   \`---.._|`--.._    | |      /....../ | |__| |__| |
#                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
#                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
#                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
#      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
# .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
# _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
#`.-._  `._  `- `-._  .`-.```-._ ``-..__``.-  -._--.__---._--..-._`...```
#   _.-` ``--..  ..  `.-._  `._  `- `-._ .-_. ._.- -._ --.._`` _.-`LGB`-.