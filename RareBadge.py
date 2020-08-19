from urllib.request import Request, urlopen
from datetime import datetime
import re, winsound, os
#Makes a list of badges and percentages
Badges = []
Owners = []
temp = []
#Stores the ten lowest percentages and the indexes for the rarest badges
lowestOwners = []
rarestBadges = []
BadgesToStore = 10
#Juice!
keepCounting = True
userID = int(input("Input user ID: "))
url = "https://badges.roblox.com/v1/users/"+str(userID)+"/badges?limit=100&sortOrder=Desc"
cursor = ""
while keepCounting:
    try:
        if cursor == "":
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        else:
            req = Request(url+"&cursor="+cursor, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf-8')
        if "User is invalid or does not exist." in webpage:
            print("Error: User ID is invalid")
            break
        html = re.findall(re.compile(',"awardedCount":(.+?),'), webpage)
        Owners = Owners + html
        temp = temp + html
        html = re.findall(re.compile('{"id":(.+?),'), webpage)
        for i in range(len(html)):
            if i%2 == 0:
                Badges.append(html[i])
        if len(html) == 200:
            regex = '"nextPageCursor":"(.+?)",'
            pattern = re.compile(regex)
            try:
                cursor = re.findall(pattern, webpage)[0]
            except:
                break
        else:
            keepCounting = False
    except:
        continue
temp.sort(key=len)
for i in range(BadgesToStore):
    lowestOwners.append(temp[i])
    BadgeToAdd = 0
    BadgeToAdd = Owners.index(temp[i])
    while Badges[BadgeToAdd] in rarestBadges:
        BadgeToAdd = Owners.index(temp[i], BadgeToAdd+1)
    rarestBadges.append(Badges[BadgeToAdd])
print("This user's top "+str(BadgesToStore)+" rarest badges (n="+str(len(Badges))+") are:")
print(rarestBadges)
print(lowestOwners)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME) # Remove this line if you do not want the program to play a sound when it finishes.
