from github import Github
import sys
import os

# You need to retrieve your access token from github and store it under credentials.txt in the project folder

# Loading credentials:
credentials = open ('credentials.txt')

# Github access token
accessToken = credentials.read()

# Base folder for development projects
path = "/users/gabrielefarei/documents/development/"

# Obtaining project folder name from CML
folderName = str(sys.argv[1])

# New folder structure
newpath = path + folderName

# Accessing github
g = Github(accessToken)
user = g.get_user()

# Creating project folder using folderName
os.mkdir(newpath)



# Creating github repository
repo = user.create_repo(folderName)
print("Succesfully created repository {}".format(folderName))
