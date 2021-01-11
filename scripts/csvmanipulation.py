import csv
import sys

'''
deletes attribute from waifu cell
f = [[a for a in x if a != person] for x in f]
'''

def celltest(list, row, column):
    try:
        print(list[row][column])
        return True
    except:
        return False

def name(person, action):
    f = list()
    with open('data/waifus.csv', 'r') as fileread:
        file_reader = csv.reader(fileread)
        for row in file_reader:
            f.append(row)
    fileread.close()
    if action == 'add':
        f.append([person])
        print('added ' + person)
    elif action == 'unadd':
            print(f)
            f=[x.remove(person) if person in x else x for x in f]
            f.remove(None)
            print('removed ' + person )
            print(f)
            
    with open('data/waifus.csv', 'w') as file: 
        file_writer = csv.writer(file)
        try:
            file_writer.writerows(f)
        except:
            pass
    
def anime(person, anime):
    f = list()
    with open('data/waifus.csv', 'r') as fileread:
        file_reader = csv.reader(fileread)
        for row in file_reader:
            f.append(row)
    fileread.close()
    for i in range(len(f)):
        if person in f[i]:
            row = i
    try:
        f[row][1] = anime
    except:
        f[row].append(anime)
    with open('data/waifus.csv', 'w') as file:
        file_writer = csv.writer(file)
        try:
            file_writer.writerows(f)
            print(person + ' was added to ' + anime)
        except:
            pass
def trait(person, trait, ftype):
    f = list()
    with open('data/waifus.csv', 'r') as fileread:
        file_reader = csv.reader(fileread)
        for row in file_reader:
            f.append(row)
    fileread.close()
    for i in range(len(f)):
        if person in f[i]:
            row = i
    if ftype == 'ptrait':
        if celltest(f, row, 2) == False:
            f[row].append(trait)
        else:
            if celltest(f, row, 3) == False:
                f[row].append(trait)
            else:
                print('Ptraits full!!!')
                sys.exit(1)
    elif ftype == 'ltrait':
        if celltest(f, row, 4) == False:
            f[row].append(trait)
        else:
            if celltest(f, row, 5) == False:
                f[row].append(trait)
            else:
                print('Ltraits full!!!')
                sys.exit(1)
    with open('data/waifus.csv', 'w') as file:
        file_writer = csv.writer(file)
        try:
            file_writer.writerows(f)
            print(person + ' was added to ' + anime)
        except:
            pass
def bodybuilder(person, part, description):
    f = list()
    with open('data/waifus.csv', 'r') as fileread:
        file_reader = csv.reader(fileread)
        for row in file_reader:
            f.append(row)
    fileread.close()
    for i in range(len(f)):
        if person in f[i]:
            row = i
    if part == 'hair':
        column = 2
    elif part == 'hairlen':
        column = 3
    elif part == 'eye':
        column = 4
    elif part == 'age':
        column = 5
    try:
        f[row][column] = description
    except:
        f[row].append(description)
    with open('data/waifus.csv', 'w') as file:
        file_writer = csv.writer(file)
        try:
            file_writer.writerows(f)
            print(person + ' was added to ' + anime)
        except:
            pass

def profilebuild(person, f, hair,hairlen, eye, age,):
    name(person, 'add')
    anime(person, f)
    bodybuilder(person, 'hair', hair)
    bodybuilder(person, 'len', hairlen)
    bodybuilder(person, 'eye', eye)
    bodybuilder(person, 'age', age)



        




