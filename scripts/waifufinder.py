import csvmanipulation
import csv
from bs4 import BeautifulSoup 
import requests
from urllib import request
import os
import urllib
import time

#testing amount change variable based on amount of characters loaded.
test = 1000

souplist = list()
max = 106309
header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',

    }
for i in range(test):
    try:
        url = ('https://www.animecharactersdatabase.com/characters.php?id=' + str(i))
        urlsearch = ('characters.php?id=' + str(i))
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        print('reading page ' + str(i))
        souplist.append(soup)
    except:
        print('Scanning interrupted')
        print('sorting...')
        test = i
        time.sleep(1)
        break
    #allows for errors without fatal breakdowns
        

def characterget(soup, amount):
    links = list()
    characters = list()
    for i in range(amount):
        print('Sorting page:' + str(i))
        if 'Female' not in str(soup[i]): 
            pass
            print('male')
        else:
            for link in soup[i].find_all('p'):
                for ele in link.find_all('a'):
                    links.append(str(ele))    

    for e in links:
        if 'characters.php?id=' in e and 'indexed as' not in e:
            scrap, person = e.split('>', 1)
            person, scrap = person.split('<')
            characters.append(str(person))
    return characters

def features(soup,amount):
    links = list()
    hairs = list()
    eyes = list()
    ages = list()
    attr = list()
    hairslen = list()
    for i in range(amount):
        if 'Female' not in str(soup[i]):
            pass
        else:
            for link in soup[i].find_all('p'):
                for ele in link.find_all('span'):
                        for elee in ele:
                            attr.append(elee)
    for f in attr:
        gender, age = f.split(' ', 1)
        age, other = age.split(' ', 1)
        ages.append(str(age))
        w, eye = other.split('with ', 1)
        eye, other = eye.split(' eyes', 1)
        eye = str(eye + '-eyes')
        eyes.append(eye)
        w2, other = other.split('and ', 1)
        try:
            hair, other = other.split(' that', 1)
        except:
            hair = 'fatal error'
            other = 'fatal error'
        hairs.append(str(hair))
        try:
            other, hairlen = other.split('To ')
        except:
            try:
                other, hairlen = other.split('is ')
            except:
                other = 'fatal'
                hairlen = 'fatal'
        hairslen.append(hairlen)
    return ages, hairs, hairslen, eyes

def animefinder(soup, amount):
        links = list()
        anime = list()
        for i in range(amount):
            if 'Female' not in str(soup[i]): 
                pass
            else:
                counter = 0
                for link in soup[i].find_all('p'):
                    for ele in link.find_all('a'):
                        if ('source.php?id=') in str(ele) and counter == 0:
                            counter +=1
                            links.append(str(ele)) 
                

        for e in links:
            if 'source.php?id=' in e:
                scrap, an = e.split('>', 1)
                an, scrap = an.split('<')
                anime.append(an)
        return anime

names = characterget(souplist, test)
animes = animefinder(souplist, test)
ages, hairs,hairslen, eyes = features(souplist, test)

for i in range(len(names)):
    csvmanipulation.profilebuild(names[i],animes[i],hairs[i],hairslen[i],eyes[i],ages[i])
