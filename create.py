from github import Github
import sys
import os
import argparse


## Importing value from the CLI

parser = argparse.ArgumentParser( description='Repository preferences' )

# Defining arugments to parse from the command line
parser.add_argument('repo_name', action="store", 
                    help='repository name in one string without spaces')

parser.add_argument('-p', action='store_false', default=True,
                    dest='public_repo',
                    help='Set a repository to public')

results = parser.parse_args()

repoName = results.repo_name
publicRepo = results.public_repo ## 0 when flag, 1 when no flag


# Retrieving the access token from github and stored it under credentials.txt in the project folder

# Loading credentials:
credentials = open ('/users/gabrielefarei/documents/development/new_repo_automation/credentials.txt')

# Github access token
accessToken = credentials.read().rstrip()

# Base folder for development projects
path = "/users/gabrielefarei/documents/development/"

# New folder structure
newpath = path + repoName

# Accessing github
g = Github(accessToken)
user = g.get_user()

# Creating project folder using folderName
os.mkdir(newpath)


# Creating github repository
repo = user.create_repo(
    repoName,
    private=publicRepo),
print("Successfully created repository {}".format(repoName))
