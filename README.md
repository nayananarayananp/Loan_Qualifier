# Loan_Qualifier
### Create Repo
Created a repo via Github UI to add as remote
https://github.com/nayananarayananp/Loan_Qualifier.git

### Switch to local git repo called Loan_Qualifier
```
(base)
nayan@NayanaWork MINGW64 ~
$ cd Fintech-Workspace/Challenge/Loan_Qualifier/
(base)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ conda activate dev
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=openssl
http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
core.autocrlf=input
core.fscache=true
core.symlinks=false
core.editor="C:\\Program Files (x86)\\Notepad++\\notepad++.exe" -multiInst -notabbar -nosession -noPlugin
pull.rebase=false
credential.helper=manager-core
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
gui.recentrepo=C:/Users/nayan/Fintech-Workspace/Challenge/Loan_Qualifier
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
gui.wmstate=zoomed
gui.geometry=793x172+8012+264 338 400
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
```

### Organize folders in starter code
Checked git status showing the organized starter code
```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        app.py
        data/
        qualifier/

nothing added to commit but untracked files present (use "git add" to track)
(dev)
```

### Add starter code files to git
```
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git add .
warning: CRLF will be replaced by LF in .gitignore.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in README.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in app.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/filters/credit_score.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/filters/debt_to_income.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/filters/loan_to_value.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/filters/max_loan_size.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/utils/calculators.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/utils/fileio.py.
The file will have its original line endings in your working directory
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
```

### Check the files got added
```
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   app.py
        new file:   data/daily_rate_sheet.csv
        new file:   qualifier/filters/credit_score.py
        new file:   qualifier/filters/debt_to_income.py
        new file:   qualifier/filters/loan_to_value.py
        new file:   qualifier/filters/max_loan_size.py
        new file:   qualifier/utils/calculators.py
        new file:   qualifier/utils/fileio.py

(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
```

### Git commit
Tried committing to repo but my ID was not configured. Hidden actual name and email below
```
$ git commit -m "Initial Commit of Loan_Analyzer Challenge"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'nayan@NayanaWork.(none)')
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git config --global user.email "n***************@gmail.com"
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git config --global user.name "N***** *********"
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
```

Commit files with message
```
$ git commit -m "Initial Commit of Loan_Analyzer Challenge"
[master (root-commit) 05708a5] Initial Commit of Loan_Analyzer Challenge
 10 files changed, 290 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 app.py
 create mode 100644 data/daily_rate_sheet.csv
 create mode 100644 qualifier/filters/credit_score.py
 create mode 100644 qualifier/filters/debt_to_income.py
 create mode 100644 qualifier/filters/loan_to_value.py
 create mode 100644 qualifier/filters/max_loan_size.py
 create mode 100644 qualifier/utils/calculators.py
 create mode 100644 qualifier/utils/fileio.py
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)

$ git status
On branch master
nothing to commit, working tree clean
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
```
## Git push
Try pushing to github but repo created from web is not configured yet
```
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

(dev)
```

Add remote git repo to map to local following instructions 

```
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git remote add origin https://github.com/nayananarayananp/Loan_Qualifier.git
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (master)
$ git branch -M main
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
```

git push to remote repo
```
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 16 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (16/16), 4.11 KiB | 1.37 MiB/s, done.
Total 16 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/nayananarayananp/Loan_Qualifier.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
```

Check git status
```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
(dev)
```
### Run program
After this, completed the challenge code in `app.py` for `save_qualifying_loans` function and updated `utils/fileio.py` to add a `save_csv` function.

Running the program with code completed
```
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ python app.py
? Enter a file path to a rate-sheet (.csv): data/daily_rate_sheet.csv
? What's your credit score? 750
? What's your current amount of monthly debt? 1000
? What's your total monthly income? 3000
? What's your desired loan amount? 50000
? What's your home value? 300000
The monthly debt to income ratio is 0.33
The loan to value ratio is 0.17.
Found 15 qualifying loans
? Enter a file name to save the qualifying loans : qualifying_loans_300k
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ python app.py
? Enter a file path to a rate-sheet (.csv): data/daily_rate_sheet.csv
? What's your credit score? 750
? What's your current amount of monthly debt? 1000
? What's your total monthly income? 3000
? What's your desired loan amount? 500000
? What's your home value? 300000
The monthly debt to income ratio is 0.33
The loan to value ratio is 1.67.
Found 0 qualifying loans
? Enter a file name to save the qualifying loans : qualifying_loans_500k
(dev)
```

### Capture terminal history
```
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ history 100 > terminal_history.txt
(dev)
```
Attached to [](./terminal_history.txt)

### Final commit and push
Add all changes using git add
```
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   app.py
        modified:   qualifier/utils/fileio.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        data/qualifying_loans_300k.csv
        data/qualifying_loans_500k.csv
        terminal_history.txt

no changes added to commit (use "git add" and/or "git commit -a")
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ git add .
warning: CRLF will be replaced by LF in README.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in app.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in qualifier/utils/fileio.py.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in data/qualifying_loans_300k.csv.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in data/qualifying_loans_500k.csv.
The file will have its original line endings in your working directory
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        modified:   app.py
        new file:   data/qualifying_loans_300k.csv
        new file:   data/qualifying_loans_500k.csv
        modified:   qualifier/utils/fileio.py
        new file:   terminal_history.txt

(dev)
```
Finally, committed with a message and git push to finish the challenge.

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        modified:   app.py
        new file:   data/qualifying_loans_300k.csv
        new file:   data/qualifying_loans_500k.csv
        modified:   qualifier/utils/fileio.py
        new file:   terminal_history.txt

(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ git commit -m "Push with challenge code and documentation complete"
[main d1c7c5e] Push with challenge code and documentation complete
 6 files changed, 367 insertions(+), 5 deletions(-)
 rewrite README.md (63%)
 create mode 100644 data/qualifying_loans_300k.csv
 create mode 100644 data/qualifying_loans_500k.csv
 create mode 100644 terminal_history.txt
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
$ git push
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 16 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (11/11), 4.60 KiB | 1.53 MiB/s, done.
Total 11 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/nayananarayananp/Loan_Qualifier.git
   05708a5..d1c7c5e  main -> main
(dev)
nayan@NayanaWork MINGW64 ~/Fintech-Workspace/Challenge/Loan_Qualifier (main)
```
All files pushed to remote.