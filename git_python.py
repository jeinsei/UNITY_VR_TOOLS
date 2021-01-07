from github import Github
from git import Repo
from getpass import getpass
import schedule
import time
from phue import Bridge
from playsound import playsound


# adress IP du Bridge Philips
b = Bridge("192.168.1.10")
# connect le script au pont en cliquant une fois sur le bouton du pont
b.connect()
# retourne les infos du Bridge
b.get_api()
# Récupère toutes les lights du pont
lights = b.lights


# Joue un son dans le dossier parent

# set toutes les lumieres sur ON et la lumière / éclairage et saturation voulu
# for l in lights:
#     print(l.name)
#     l.on = True
#     l.brightness = 254
#     l.saturation = 254
#     l.hue = 44000
#     playsound('/Users/noe/Desktop/GIT_API/xp.mp3')


lights[1].on = True
lights[1].brightness = 254
lights[1].saturation = 254
lights[1].hue = 44000
playsound('/Users/noe/Desktop/GIT_API/xp.mp3')

# Permet de récuperer les différents input

while True:
    _user = input("YOUR GITHUB USERNAME ")
    
    if(_user == "juliennoe"):
        print("VALIDATION AUTHENTIFICATION")
        lights[1].on = True                                          
        lights[1].brightness = 254
        lights[1].saturation = 254
        lights[1].hue = 50000
        playsound('/Users/noe/Desktop/GIT_API/gamecube.mp3')
        break
    else:
        print("VALIDATION FAIL")
        lights[1].on = True                                          
        lights[1].brightness = 254
        lights[1].saturation = 254
        lights[1].hue = 500
        playsound('/Users/noe/Desktop/GIT_API/sardoche.mp3')
        



_token = getpass("YOUR GITHUB TOKEN ")
_repoTarget = input("YOUR GITHUB REPOSITORY NAME ")

# récupère les infos de l'api GITHUB par rapport au token
g = Github(_token)
userGit = g.get_user()

        
# set dans des variables les infos de l'API GITHUB
repo = g.get_repo("juliennoe" + "/" + _repoTarget)
repos = userGit.get_repos()
labels = repo.get_labels()
contents = repo.get_contents("")
branch = g.get_repo(_user + "/" +_repoTarget).get_branch("master")
commit = repo.get_commit(sha="master")
commitSaveValue = 0
repoSaveValue = 0

#print(commitSaveValue)
#print(repoSaveValue)

print("WAITING UPDATE")


lights[1].on = True
lights[1].brightness = 254
lights[1].saturation = 120
lights[1].hue = 15000

# Sauvegarde le nombre de commit initial
def SaveInitialCommitCount():
    return repo.get_commits().totalCount
    
commitSaveValue = SaveInitialCommitCount()
# print(commitSaveValue)
# print("SAVE COMMITS COUNT")

# Sauvegarde le nombre de repo initial
def SaveInitialRepoCount():
    return userGit.get_repos().totalCount

repoSaveValue = SaveInitialRepoCount()
# print(repoSaveValue)
# print("SAVE REPO COUNT")

# Check avec l'update le nombre de commit
def SaveUpdateCommitCount():
    return repo.get_commits().totalCount

# Check avec l'update le nombre de repo 
def SaveUpdateRepoCount():
    return userGit.get_repos().totalCount

# Boucle pour checker en temps réel le nombre de commit et repo
while True:

    #print(commitSaveValue)
    SaveUpdateCommitCount()
    #print(SaveUpdateCommitCount())

    #print(repoSaveValue)
    SaveUpdateRepoCount()
    #print(SaveUpdateRepoCount())

    if SaveUpdateCommitCount() > commitSaveValue:
        print("UPGRADE COMMIT ...")
        lights[1].on = True
        lights[1].brightness = 254
        lights[1].saturation = 255
        lights[1].hue = 25000
        playsound('/Users/noe/Desktop/GIT_API/pavard.mp3')
        time.sleep(5)
        pass
        
        print("UPGRADE COMMIT DONE")
        print("WAITING UPDATE")
        commitSaveValue = SaveUpdateCommitCount()

        lights[1].on = True
        lights[1].brightness = 254
        lights[1].saturation = 120
        lights[1].hue = 15000
        pass
    
    if SaveUpdateRepoCount() > repoSaveValue:
        print("UPGRADE REPO ...")
        lights[1].on = True
        lights[1].brightness = 254
        lights[1].saturation = 255
        lights[1].hue = 60000
        playsound('/Users/noe/Desktop/GIT_API/lepers.mp3')
        time.sleep(5)
        pass
        
        print("UPGRADE REPO DONE")
        print("WAITING UPDATE")
        
        repoSaveValue = SaveUpdateRepoCount()
        lights[1].on = True
        lights[1].brightness = 254
        lights[1].saturation = 120
        lights[1].hue = 15000
        pass

    time.sleep(1)

# print(repo)
# print(userGit.name)
# print(userGit.login)
# print(repo.get_topics())
# print(labels)
# print(list(repo.get_branches()))
# print(branch.commit)
# print(commit.commit.author.date)
# print(commit.commit.message)
# print(commit.commit.sha)





