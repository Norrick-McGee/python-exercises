def is_two(num):
    if type(num) == str:
        if num.isdigit():
            num = int(num)
    if type(num) == int:
        if num == 2:
            return True
    else:
        return False

print("if I pass in the string '2': " +str(is_two('2')))
print("if I pass in the int 2: " +str(is_two(2)))
print("if I pass in any non-2 integer or any-non integer: " +str(is_two(2)))


def is_vowel(our_char):
    vowels = ['a','e','i','o','u','y']
    if our_char.lower() in vowels:
        return True
    else:
        return False

def is_consonant(our_char):
    return not is_vowel(our_char)

def cap_first_cons(str):
    if is_consonant(str[0]):
        return str.capitalize()
    else:
        return str

print(cap_first_cons('applesauce'))
print(cap_first_cons('tacobell'))


# 5
def calculate_tip(amt, tip=0.1):
    return amt + (amt*tip)

print(f"${calculate_tip(5):.2f}")
print(f"${calculate_tip(10,.2):.2f}")

#6
def apply_discount(price,discount):
    return price - price*discount

#7
def handle_commas(str):
    str = str.replace(",",'')
    return(int(str))

#8
def get_letter_grade(grade_as_num):
    if v >= 88 and v <= 100: return "A"
    if v >= 80 and v <=87: return "B"
    if v >= 67 and v <=79: return "C"
    if v >= 60 and v <= 66: return "D"
    if v <= 59: return "You flunked"

#9
def remove_vowels(str):
    new_str = []
    for i in str:
        if is_vowel(i):
            continue
        new_str.append(i)
    return ''.join(new_str)

print(remove_vowels('pizzadog'))


#10
def normalize_name(str):
    str = str.strip()
    str = str.lower()
    str = str.replace(' ','_')
    return str

print(normalize_name('SUPER MAN '))

#11
def cumsum(your_list):
    cumsum = []
    cum = 0
    for i in your_list:
        cum += i
        cumsum.append(cum)
    return cumsum

print(cumsum([1,2,3]))
