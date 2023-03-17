#!/bin/bash

function create() {
     cd
     if (($# > 1 )); 
     then
        python3 /Users/gabrielefarei/Development/new_repo_automation/create.py $1 $2
     else 
        python3 /Users/gabrielefarei/Development/new_repo_automation/create.py $1 
     fi 
     
     cd /Users/gabrielefarei/Development/$1
     git init
     git remote add origin git@github.com:jayfarei/$1.git
     touch README.md
     git add .
     git commit -m "Initial commit"
     git push -u origin master
     code .
}

