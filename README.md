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
4. Create base readme with `touch README.md`

Set up Github repository
------
5. Create git `git init`
6. Navigate to github.com -> create a new repository (same name) -> enter `git remote add origin https://github.com/JayFarei/new_repo_automation.git`
7. `git add .`
7. Create first commit with `git commit -m 'initial commit'`
8. Push the commit with `git push --set-upstream origin master`

Start working on it
------
9. Open the project folder in atom with `atom .`
