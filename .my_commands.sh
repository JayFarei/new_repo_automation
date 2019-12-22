#!/bin/bash

function create() {
     cd
     python /users/gabrielefarei/documents/development/new_repo_automation/create.py $1
     cd /users/gabrielefarei/documents/development/$1
     git init
     git remote add origin git@github.com:jayfarei/$1.git
     touch README.md
     git add .
     git commit -m "Initial commit"
     git push -u origin master
     atom .
   }