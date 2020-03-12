#!/bin/bash

function create() {
     cd
     if (($# > 1 )); 
     then
        python3 /users/gabrielefarei/documents/development/new_repo_automation/create.py $1 $2
     else 
        python3 /users/gabrielefarei/documents/development/new_repo_automation/create.py $1 
     fi 
     
     cd /users/gabrielefarei/documents/development/$1
     git init
     git remote add origin git@github.com:jayfarei/$1.git
     touch README.md
     git add .
     git commit -m "Initial commit"
     git push -u origin master
     code .
   }
