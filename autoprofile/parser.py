import json,csv,sqlite3
from random import choice
from string import ascii_lowercase

#Import all cities, sort by population
def getCities(c):
  with open(c, newline='') as csvfile:
    citiesReader = csv.DictReader(csvfile)
    ret = []
    #TODO: RANK CITIES BY POPULATION
    for row in citiesReader:
      ret.append([row['city'],row['state_name']])
    return ret

#block of code for the first name
def getNames(c,k):
  with open(c, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ret = []
    for row in reader:
      ret.append(row[k])
    return ret

#returns a random string of length l
def getRandStr(l):
  return ''.join(choice(ascii_lowercase) for i in range(l))

#Stores each "random" entry into a db.  
def storeInDb(cities,fNames,lNames):
  conn = sqlite3.connect('people.db')
  
def main():
  cities = getCities('uscitiesv1.3.csv')
  fNames = getNames('firstnames.csv','name')
  lNames = getNames('lastnames.csv','name')
  gender = getGender('firstnames.csv','gender')
  rcity = choice(range(len(cities)))
  rname = choice(range(len(fnames)))
  storeInDb(cities,fNames,gender,lNames)

main()
##fo = open(firstname + " " + lastname + ".txt", "wb+")
