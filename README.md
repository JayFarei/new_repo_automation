## Automating the creation of a Github repository from one terminal command


#### Requirements:

Create a terminal command that automates the steps I take when creating a new project

Command line instruction:

```
create new_repo_automation
```

Should perform the following actions:


Local folder structure
------
1. Navigate to the development folder `cd ~/documents/development/.`
2. Create project directory `mkdir new_repo_automation`
3. Navigate to the project folder `cd new_repo_automation`

Set up Github repository
------
4. Create git `git init`
5. Navigate to github.com -> copy the remote of the new repository
6. Add the remote to the local folder `git remote add origin https://github.com/JayFarei/new_repo_automation.git`
7. Create base readme with `touch README.md`
8. Git add `git add .`
9. Git commit `git commit -m 'initial commit'`
10. Git push `git push --set-upstream origin master`

Open project with my editor of choice
------
11. Open the project folder in atom with `atom .`
