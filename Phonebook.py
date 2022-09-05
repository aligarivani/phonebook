import os
from collections import Counter
contacts = []
while True:
    print("\t\t\t\t>>>>Welcome To Countact Python<<<<")
    print("""
          1. creact new
          2. update contact by name
          3. update contact by phone
          4 . remove 
          5 . show all
          <Press Enter For Exit>\n""")
    try:
        num = int(input("enter number for action =  "))
    except:
        break
    if num == 1:
        name = input("Enter name = ")
        phone = input("Enter Phone Number = ")
        x = 0
        for i in phone:
            x += 1
        n = Counter(phone)
        if x < 11:
            print("phone number need 12 number pls try again")
            phone = input("Enter Phone Number = ")
        contacts.append([name, phone])
        input("contact add press enter to back menu")
    if num == 2:
        cheng = input("what is name =")
        x = 0
        for i in contacts:
            if i[0] == cheng:

                print(i)
                phone1 = input("Enter new Phone Number = ")
                contacts[x] = [name, phone1]
            x += 1
    if num == 4:
        remov = input("what is name =")

        d = 0
        for i in contacts:
            if i[0] == remov:
                contacts[d].remove(name)
                contacts[d].remove(phone)
                input("remove done press enter to back menu")
            d += 1

    if num == 5:
        os.system('cls')
        for i in contacts:
            print(i)
            input("")

    if num == 3:
        cheng = input("what is phone =")
        x = 0
        for i in contacts:
            if i[1] == cheng:

                print(i)
                name1 = input("Enter new name = ")
                contacts[x] = [name1, phone]
            x += 1

print(contacts)
print("by by see you later")
