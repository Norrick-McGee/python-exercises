import functions_exercises as fe
import itertools as it
import json

def money_str_to_float(str):
    str = str.replace('$','')
    str = str.replace(',','')
    return float(str)

def highest_balance_user(list_of_dict):
        list_of_balances = []
        list_of_users_with_max_bal = []
        for i in list_of_dict:
            list_of_balances.append(money_str_to_float(i['balance']))
        for i in list_of_dict:
            if money_str_to_float(i['balance']) == max(list_of_balances):
                list_of_users_with_max_bal.append(i['name'])
        if len(list_of_users_with_max_bal) == 1:
            return list_of_users_with_max_bal[0]
        else:
            return list_of_users_with_max_bal

def lowest_balance_user(list_of_dict):
    list_of_balances = []
    list_of_users_with_bot_balance = []
    for i in list_of_dict:
        list_of_balances.append(money_str_to_float(i['balance']))
    for i in list_of_dict:
        if money_str_to_float(i['balance']) == min(list_of_balances):
            list_of_users_with_bot_balance.append(i['name'])
    if len(list_of_users_with_bot_balance) == 1:
        return list_of_users_with_bot_balance[0]
    else:
        return list_of_users_with_bot_balance

def fruit_counts(list_of_dict):
    fruit_counts = {}
    for i in list_of_dict:
        fruit_counts[i['favoriteFruit']] = 0
    for i in list_of_dict:
        fruit_counts[i['favoriteFruit']] += 1
    return fruit_counts

def max_in_dict(dict_of_ints):
    """ Takes a Dictionary that has String Keys and Numerical values and returns the key(s) which has the highest Numerical Value"""
    list_of_vals =[]
    list_of_max_keys = []
    for i in dict_of_ints:
        list_of_vals.append(dict_of_ints[i])
    max_val= max(list_of_vals)
    for i in dict_of_ints:
        if dict_of_ints[i] == max_val:
            list_of_max_keys.append(i)
    if len(list_of_max_keys) == 1:
        return list_of_max_keys[0]
    else:
        return list_of_max_keys

def min_in_dict(dict_of_ints):
    """ Takes a Dictionary that has String Keys and Numerical values and returns the key(s) which has the lowest Numerical Value"""
    list_of_vals =[]
    list_of_min_keys = []
    for i in dict_of_ints:
        list_of_vals.append(dict_of_ints[i])
    min_val = min(list_of_vals)
    for i in dict_of_ints:
        if dict_of_ints[i] == min_val :
            list_of_min_keys.append(i)
    if len(list_of_min_keys) == 1:
        return list_of_min_keys[0]
    else:
        return list_of_min_keys

def dict_of_users_and_message(dict_of_ints):
    dict_of_users_and_message = {}
    for i in dict_of_ints:
        dict_of_users_and_message[i['name']] = i['greeting']
    return dict_of_users_and_message

def unread_messages_for_user(dict):
    dict_of_unreads = {}
    for i in dict:
        dict_of_unreads[i] = int(dict[i].replace(f"Hello, {i}! You have","").replace("unread messages.","").strip())
    return dict_of_unreads

def sum_dict(dict):
    sum = 0
    for i in dict:
        sum += dict[i]
    return sum



print(fe.is_vowel('a'))
print(f"price after tip is: ${fe.calculate_tip(5):.2f}")
print(f"{fe.twelveto24('11:44am')}")


print(list(it.combinations(['a','b','c'] + ['1','2','3'], 2)))

print(len(list(it.combinations('abcd',2))))

data = json.load(open('profiles.json'))

total_users = len(data)
print(f'number of users: {total_users}')

def count_actives(list_of_dict):
    count = 0
    for i in list_of_dict:
        #print(i['isActive'])
        if i['isActive']:
            count += 1
    return count

active_users = count_actives(data)
print(f'number of active users: {active_users}')

inactive_users = total_users - active_users

print(f'number of inactive_users: {inactive_users}')

def sumbalances(list_of_dict):
    sum = 0
    for i in list_of_dict:
        sum += money_str_to_float(i['balance'])

    return sum

print(f'total balance for all users: ${sumbalances(data)}')

print(lowest_balance_user(data))
print(highest_balance_user(data))

print(fruit_counts(data))
print(max_in_dict(fruit_counts(data)))
print(min_in_dict(fruit_counts(data)))

user_msgs = unread_messages_for_user(dict_of_users_and_message(data))
print(user_msgs)
print(sum_dict(user_msgs))
