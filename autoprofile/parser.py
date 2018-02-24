import json,csv,sqlite3,requests,random
from requests.exceptions import HTTPError
from random import choice
from string import ascii_lowercase

cats = ["Animal.txt", "Artifact.txt", "Computer.txt", "Food.txt", "Fungus.txt","Geo.txt", "Person.txt", "Plant.txt","Sport.txt"]

#gets a city with its state
def getCities(c):
  with open(c, newline='') as csvfile:
    citiesReader = csv.DictReader(csvfile)
    ret = []
    #TODO: RANK CITIES BY POPULATION
    for row in citiesReader:
      ret.append([row['city'],row['state_name']])
    return ret

#block of code for the first name, also key is the gender
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

#gets a random line in a file
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line  

def getUrls(s):
  ret = []
  filestr = "../Models/Dummy Accounts/Image URL Datasets/"
  for q in s:
    with open(filestr+q,errors="ignore") as f:
      c = choice([3,4])
      for i in range(c):
        try:
          r = requests.get(random_line(f))
          f.seek(0)
          ret.append(r.url)
          r.raise_for_status()
        except HTTPError:
          print("Sah dude this link aint GUCci gang", r.url)
  print(ret)
  return ret

#MAKES a user class so that data manipulation is easier
class User:
  def __init__(self):
    fNames = getNames('firstnames.csv','name')
    lNames = getNames('lastnames.csv','name')
    gender = getNames('firstnames.csv','gender')
    cities = getCities('uscitiesv1.3.csv')
    randName = choice(range(len(fNames)))
    randCity = choice(range(len(cities)))
    self.fName = fNames[randName]
    self.gend  = gender[randName]
    self.lName = lNames[choice(range(len(lNames)))]
    self.city  = cities[randCity][0]
    self.state = cities[randCity][1]
    self.email = getRandStr(choice(range(4,20)))+choice(["@gmail.com","@onet.pl","@yahoo.com","@yolo.swag","@gucci.gang","@hotmail.com"])
    self.pw    = getRandStr(choice(range(4,20)))
    self.urls  = getUrls(random.sample(set(cats),3))
  
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

#Stores each "random" entry into a db.  
def storeInDb(num):
  conn = sqlite3.connect('people.db')
  #c = conn.cursor()

  # Create table
  #c.execute('''CREATE TABLE people (First Name, Last Name, Gender, City, State, Email, Password)''')

  #for i in range(num):
  u = User()
    #c.execute("INSERT INTO people VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(u.fName,u.lName,u.gend,u.city,u.state,u.email,u.pw))
      
  # Save (commit) the changes
  #conn.commit()

  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  #conn.close()
  
def main():
  storeInDb(100)

main()
