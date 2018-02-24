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
def storeInDb(cities,fNames,gender,lNames,num):
  conn = sqlite3.connect('people.db')
  c = conn.cursor()

  # Create table
  c.execute('''CREATE TABLE people
               (First Name, Last Name, Gender, City, State, Email, Password)''')

  for i in range(num):
    randName = choice(range(len(fNames)))
    randCity = choice(range(len(cities)))
    fName = fNames[randName]
    gend  = gender[randName]
    lName = lNames[choice(range(len(lNames)))]
    city  = cities[randCity][0]
    state = cities[randCity][1]
    email = getRandStr(choice(range(4,20)))+choice(["@gmail.com","@onet.pl","@yahoo.com","@yolo.swag","@gucci.gang","@hotmail.com"])
    pw    = getRandStr(choice(range(4,20)))
    print("INSERT INTO people VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(fName,lName,gend,city,state,email,pw))
    c.execute("INSERT INTO people VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(fName,lName,gend,city,state,email,pw))
      
  # Save (commit) the changes
  conn.commit()

  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  conn.close()
  
def main():
  cities = getCities('uscitiesv1.3.csv')
  fNames = getNames('firstnames.csv','name')
  lNames = getNames('lastnames.csv','name')
  gender = getNames('firstnames.csv','gender')
  storeInDb(cities,fNames,gender,lNames,100)

main()
##fo = open(firstname + " " + lastname + ".txt", "wb+")
