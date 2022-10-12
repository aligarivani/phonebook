
import sys
import csv


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


def view():
    data = []
    with open("data.csv") as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    return data


def remove(i):
    def save(j):
        with open("data.csv", 'w', newline="") as file:
            write = csv.writer(file)
            write.writerows(j)
    new_list = []
    phone = i
    with open('data.csv','r') as file:
        read = csv.reader(file)
        for row in read:
            new_list.append(row)
            for element in row:
                if element == phone:
                    new_list.remove(row)
    save(new_list)


def update1(i):

    def update_newlist(j):
        with open('data.csv', 'w', newline="") as file:
            write = csv.writer(file)
            write.writerows(j)
    new_list = []
    phone = i[0]

    with open("data.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == phone:
                    name = i[1]
                    gender = i[2]
                    tel = i[3]
                    email = i[4]

                data = [name, gender, tel, email]
                index = new_list.index(row)
                new_list[index] = data
    update_newlist(new_list)


def search(i):
    data = []
    phone = i
    with open('data.csv', 'r') as file:
        read = csv.reader(file)
        for row in read:
            for element in row:
                if element == phone:
                    data.append(row)
    return data
