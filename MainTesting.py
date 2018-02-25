# from autoprofile import parser
#
# user = parser.User()
import json,csv,sqlite3,requests,random
from requests.exceptions import HTTPError
from random import choice
from string import ascii_lowercase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from random import randint

subscription_key = "1ce10fd9a4b142f9b31c020ec61d2393"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"


#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
#print(image_caption)

#print(analysis["tags"][0]["confidence"])

def AccountDocTag(URL):
    doc = ""
    try:
        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
        params   = {'visualFeatures': 'Tags'}
        data     = {'url': URL}
        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()
        for ele in analysis["tags"]:
            intWeight = int(round(ele["confidence"]*10))
            tag = ele["name"]+ " "
            for i in range(intWeight):
                doc += tag
    except:
        return ""
    return doc

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
  filestr = "Models/Dummy Accounts/Image URL Datasets/"
  for q in s:
    with open(filestr+q,errors="ignore") as f:
      c = choice([3,4])
      bad = 0
      count = 0
      while(count < c and bad<10):
        try:
          r = requests.get(random_line(f), stream=True)
          f.seek(0)
          r.raise_for_status()
          tempUrl = r.url
          if "unavailable" in tempUrl or "???" in tempUrl or "jpg" not in tempUrl:
              continue
          ret.append(tempUrl)
          count+=1
        except:
            bad+=1
            continue

    f.close()
          #print("Sah dude this link aint GUCci gang", r.url)
  #print(ret)
  return ret

#MAKES a user class so that data manipulation is easier
class User:
  def __init__(self):
    fNames = getNames('autoprofile/firstnames.csv','name')
    lNames = getNames('autoprofile/lastnames.csv','name')
    gender = getNames('autoprofile/firstnames.csv','gender')
    cities = getCities('autoprofile/uscitiesv1.3.csv')
    randName = choice(range(len(fNames)))
    randCity = choice(range(len(cities)))
    day = randint(1,28)
    month = randint(1,12)
    year = randint(1980, 2000)
    urls  = getUrls(random.sample(set(cats),3)+["Person.txt"])
    ori = random.choice([0,1])
    self.fName = fNames[randName].title()
    self.gend  = gender[randName]
    if "m" in self.gend:
        self.gend = "male"
    else:
        self.gend = "female"
    self.lName = lNames[choice(range(len(lNames)))].title()
    self.city  = cities[randCity][0].title()
    self.state = cities[randCity][1].title()
    self.email = getRandStr(choice(range(4,20)))+choice(["@gmail.com","@illinois.edu","@gucci.gang","@yahoo.com","@aol.com","@msn.com","@hotmail.com"])
    self.pw    = getRandStr(choice(range(4,20)))
    self.urlsPrivate = ""
    self.urlsPublic = ""
    self.doc = ""
    self.orientation = ""
    if ori == 0:
        self.orientation = "male"
    else:
        self.orientation = "female"
    for ur in urls:
        tempdoc = AccountDocTag(ur)
        self.doc+= tempdoc
        if "person" in tempdoc:
            self.urlsPrivate += ur+" "
        else:
            self.urlsPublic += ur+" "
    self.age = ""
    if(month<10):
        self.age+="0" + str(month) + "/"
    else:
        self.age+= str(month) + "/"
    if(day<10):
        self.age+="0" + str(day) + "/"
    else:
        self.age+= str(day) + "/"

    self.age+=str(year)

  def printUser(self):
    print(self.fName)
    print(self.lName)
    print(self.age)
    print(self.gend)
    print(self.city)
    print(self.state)
    print(self.email)
    print(self.pw)
    print(self.urlsPrivate)
    print("\n")
    print(self.urlsPublic)
    print(self.doc)

  def printToFile(self, fn):
      with open(fn,"a") as out:
        out.write("INSERT INTO users (firstname, lastname, email, birthday, sex, orientation, location,"+
        " pwdhash, image, private, tags, matched, flag, priv) VALUES ('"+
        self.fName + "', '" + self.lName + "', '" + self.email + "', '" + self.age + "', '" +
        self.gend + "', '" + self.orientation + "', '" + self.city +", " + self.state + "', '" + self.pw +
        "', '" + self.urlsPublic + "', '" + self.urlsPrivate + "', '" + self.doc + "', '', '', '');\n\n\n\n")


        # out.write("FNAME: "+self.fName+"\n")
        # out.write("LNAME: "+self.lName+"\n")
        # out.write("AGE: "+self.age+"\n")
        # out.write("GENDER: "+self.gend+"\n")
        # out.write("ORIENTATION: "+self.orientation+"\n")
        # out.write("LOCATION: "+self.city+", "+self.state+"\n")
        # out.write("EMAIL: "+self.email+"\n")
        # out.write("PASSWORD: "+self.pw+"\n")
        # out.write("PRIVATE URLs: "+self.urlsPrivate+"\n")
        # out.write("PUBLIC URLs: "+self.urlsPublic+"\n")
        # out.write("DOCUMENT: "+self.doc+"\n")
        # out.write("\n")
  # def getUrls(self):
  #     return self.urls
  # def getDoc(self):
  #     return self.doc

# user = User()
# #user.printUser()
# user.printToFile("Users/users.txt")

count = 0
for i in range(30):
    user = User()
    print(count+1)
    user.printToFile("Users/usersNew.txt")
    count +=1
