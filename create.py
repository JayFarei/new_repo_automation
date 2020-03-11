from github import Github
import sys
import os

# You need to retrieve your access token from github and store it under credentials.txt in the project folder

# Loading credentials:
credentials = open ('/users/gabrielefarei/documents/development/new_repo_automation/credentials.txt')

# Github access token
accessToken = credentials.read().rstrip()

# Base folder for development projects
path = "/users/gabrielefarei/documents/development/"

# Obtaining project folder name from CML
folderName = str(sys.argv[1])

# CLI has to be provided as: python create.py arg1 arg2 arg3

# len(create.py) = ['create.py', 'arg1', 'arg2', 'arg3']

if len(sys.argv) > 2:
    # Private boolean
    privateValue = sys.argv[2]

    # Description
    description = str(sys.argv[3])


# New folder structure
newpath = path + folderName

# Accessing github
g = Github(accessToken)
user = g.get_user()

# Creating project folder using folderName
os.mkdir(newpath)


# Creating github repository
repo = user.create_repo(
    folderName,
    description=description, 
    private=privateValue),
print("Succesfully created repository {}".format(folderName))
