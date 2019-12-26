## Automating the creation of a Github repository from one terminal command


#### Requirement this is solving for:

> Create a terminal command that automates the steps I take when creating a new project

Command line instruction:

```
create <project_name>
```

The automation should perform the following actions:


**Set up local folder structure**

1. Navigate to the development folder `cd ~/documents/development/.`
2. Create project directory `mkdir new_repo_automation`
3. Navigate to the project folder `cd new_repo_automation`

**Set up Github repository**

4. Create git `git init`
5. Navigate to github.com -> copy the remote of the new repository
6. Add the remote to the local folder `git remote add origin https://github.com/JayFarei/<newproject>.git`
7. Create base readme with `touch README.md`
8. Git add `git add .`
9. Git commit `git commit -m 'initial commit'`
10. Git push `git push --set-upstream origin master`

**Open project with my editor of choice**

11. Open the project folder in atom with `atom .`


## How to use it

1. Get the repository

```
git clone "https://github.com/JayFarei/new_repo_automation.git"
```
```
cd new_repo_automation
```

2. Install the requirements:
```
sudo easy_install pip
```
```
pip install -r requirements.txt
```

for python3, check if you have pip 3 with ` which pip3`, if it still points at 2.7 - do the following:

```
 curl -O https://bootstrap.pypa.io/get-pip.py
 python3 get-pip.py
 which pip3
```
then repeat the above with pip3:
```
pip3 install -r requirements.txt
```

3. Set up bash aliases

I [found](https://apple.stackexchange.com/questions/99688/how-to-persistently-define-aliases-in-terminal) that depending on the terminal you use - you might need to create (or edit if you already have it) both bashrc and bash_profile in your home folder. In my case I have created both - and instead of introducing the function directly there -

```
touch ~/.bashrc
touch ~/.bash_profile
```

Edit both file (`atom ~/.bashrc`) and include the link to the custom alias provided by this repository

Note: if you use zsh - do the same for `atom ~/.zshrc`


```
## Github repository automation
source /users/<username>/documents/development/new_repo_automation/.my_commands.sh
```

Source them:

```
source ~/documents/development/new_repo_automation/.my_commands.sh
source ~/.bashrc
source ~/.bash_profile
source ~/.zshrc
```
Note: every time you do a change you'll have to source it again.

4. Enter your access token from Github

* Obtain your Access token from Github

* Replace `accessToken` in `/users/<username>/documents/development/new_repo_automation/create.py`

* Replace path to match your set up in `create.py` or `.my_commands.sh`

5. Run the command line instruction

Open the terminal - a run the following instruction

```
create <New Project>
```



## Notes in making it:

Navigate to your project folder and create the key files
```
cd ~/documents/development/new_repo_automation
```
```
touch .my_commands.sh
touch create.py
```
Open folder in Atom
```
atom .
```

Create a bashrc file to source your aliases
```
cd
touch ~/.bashrc
```
Link the aliases in the bashrc files

```
atom ~/.bashrc
```

Reference the alias we'll be working on so that it'll be loaded at login

```
## Github repository automation
source ~/documents/development/new_repo_automation/my_commands.sh
```

Note: whenever you make a change to the `.my_commands.sh` you'll have run this instruction `source ~/documents/development/new_repo_automation/.my_commands.sh` are the alias seems to be loaded in memory.


Install dependencies

```
sudo easy_install pip
```

then install the requirements included in the requirements.txt file in the repository

```
sudo pip install -r ~/documents/development/new_repo_automation/requirements.txt
```


**Python script**

You will need the following import:

`import sys`
>  The sys module is included in the standard libraries and contains the functions and other data necessary for your code to perform introspection about the system in which its running.

`import os`
>  The OS module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

`from github import Github`
> Following this https://github.com/PyGithub/PyGithub / this allow you to authenticate to github APIs from a python script

Note: I used mkdir as the tree already exists.

Alternatively, makedirs is a recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory. In our case it has to follow a cd command otherwise it'll generate all directories wherever we are based

Also - to get the first argument after the script for a filename, you could do the following:

```
filename = sys.argv[1]
```


**Bash script**

The script is self explanatory - if you were to do all the instructions individually on your terminal - you'll end up with this set of instructions.

Worth noticing that you will have to use the entire path vs a shortened version (using ~) - I had some issues in my tests with that.
