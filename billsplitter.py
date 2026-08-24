import random

nr_friends = int(input("Enter the number of friends joining (including you):"))
names_dict = {}

if nr_friends < 1:
    print("No one is joining for the party")
else :
    for x in range(nr_friends):
        x = input("Enter the name of every friend (including you), each on a new line:")
        names_dict[x] = 0
    bill_total = int(input("Enter the total bill value:"))
    shared_amt = round(bill_total / nr_friends, 2)

    for y in names_dict:
        names_dict[y] = shared_amt

    lucky_answer = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    if lucky_answer == "No":
        print("No one is going to be lucky")
        print(names_dict)
    elif lucky_answer == "Yes":
        random_key = random.choice(list(names_dict))
        print(f"{random_key} is the lucky one!")

        shared_amt = round(bill_total / (nr_friends - 1), 2)
        for y in names_dict:
            names_dict[y] = shared_amt
        names_dict[random_key] = 0
        print(names_dict)









