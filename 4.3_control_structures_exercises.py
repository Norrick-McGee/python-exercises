# 1. prompt the user for a day of the week, print out whether the day is Monday or not

day = input("Sup fam, gimme a day of the week, and I'm gonna tell you if it's a Monday or not\n")

if day.lower() == 'monday':
    print("yea, that's a Monday\n")
else:
    print("this ain't it, cheif \n")


# 2. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = input("Aiight, now I'm gonna check if the day of the week you tell me is a weekday or weekend \n")
if day.lower() == 'saturday' or day.lower() == 'sunday':
    print("nice, that's a weekend.\n")
elif day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or day.lower == 'thursday' or day.lower() == 'friday':
    print("lame sauce, that puts the weak in weakday, bro\n")
else:
    print("Either you giving me a madeup day, or you typed something wrong\n")


# 3. create variables for
#
# - the number of hour worked in one week
# - the hourly rate
# - how much the week's paycheck will be

hours_worked = float(input("So, how many hours you work in a week? \n"))
hourly_rate = float(input("And like, what's your hourly rate?\n"))
print("\nAiight fam, lemme do a quick calc on how much you gonna be making for this check")
print("$" + str(hours_worked * hourly_rate))

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

if hours_worked > 40:
    ot_hours = hours_worked - 40
    reg_cash = 40 * hourly_rate
    ot_cash = ot_hours * hourly_rate * 1.5
    print("but if we calcualte for OT you'd be actually making")
    print("$" + str(reg_cash + ot_cash) + "\n")

# While loop practice
i = 5
while(i <= 15):
    print(i)
    i += 1

i = 0
while(i <= 100):
    print(i)
    i+=2

i = 100
while(i >= -10):
    print(i)
    i-=5

i = 2
while(i <= 1_000_000):
    print(i)
    i = i **2

i = 100
while(i >= 5):
    print(i)
    i -= 5


your_val = int(input("please input an int\n"))
for i in range(10):
    print(f"{your_val} x {i+1} = {(i+1)*your_val}")


for i in range(10):
    print(str(i) * i)

your_val = "not a digit"
while True:
    your_val = input("Please give me a value that is an odd number between 1 to 50\n")
    if your_val.isdigit() and int(your_val) % 2 != 0 and int(your_val) < 50 and int(your_val) > 0:
        break

print(f"the value to skip is {your_val}")
for i in range(50):
    if i % 2 != 0 and i != int(your_val):
        print(f"Here is an odd number: {i}")
    elif i == int(your_val):
        print(f"YIKES! Skipping {your_val}")
#
while True:
    your_val = input("please input a postive int that is greater than 0:\n")
    if your_val.isdigit() and int(your_val) > 0 and int(your_val) %2 == 0:
        break
    print("that wasn't a valid choice")
for i in range(int(your_val)+1):
    print(i)


##### FIZZ BUZZ ######

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)

## power tables ###
your_val = 'string'
while True:
    your_val = input("we gon' print out some squares and cubes \n what number should we go upto?\n")
    if your_val.isdigit():
        break
your_val = int(your_val)
print("number | squared | cubed")
print("------------------------")
for i in range(your_val + 1):
    print(f"{i}     | {i*i}      | {i*i*i}")

v = 'string'
while True:
    v = input("exit at anytime by typing 'exit' \ngive me your grade as a value from 0 to 100\n")
    if v.isdigit() and int(v) >= 0 and int(v) <= 100:
        v = int(v)
        if v >= 88 and v <= 100: print("A")
        if v >= 80 and v <=87: print("B")
        if v >= 67 and v <=79: print("C")
        if v >= 60 and v <= 66: print("D")
        if v <= 59: print("You flunked")
        print()
    elif v.lower() == 'exit':
        break

## BOOK SEARCH ## 

books = [{"title":"how to win friends and influence people", "author": "Dale Carnegie", "genre":"Non-Fiction"}]
books.append({"title":'Flatland', "author":'Edwin Abbott Abbott', 'genre':'Science Fiction'})
books.append({"title":"Flatterland", 'author':'Ian Stewart', 'genre':'Science Fiction'})

genre = input("What Genre would you like to search for\n")
print(f"Books with the genre: {genre}")
for i in books:
    if i['genre'] == genre:
        print(i['title'])
