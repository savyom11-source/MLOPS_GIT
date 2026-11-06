a="Welcome"
#git init -to initiate git into folder
#git add . / <file_name> - to add files from untracked to stagged state
#git commit -m "" - To commit changes with messages to local repop
#git restore --staged <file> - To rollback recent commit move from staged state to untracked state
#.gitignore file-> To ignore unwanted file to track just mention file names
# git log --oneline -> To see all commit details 
#git log --stat ->to show no of lines of change in every commit
#git log -p --> To see exact code changes
# git show <sha id>-> To see how code was looking before that particular commit
# git diff -> To show changes in file under staged stage without commit
# git checkout <6 digit shha id>->. To rollback to specific commit

#Branching and  MERGING start
#git branch <branch name>-> to create new branch from head or add <sha ID at the end to create branch from specific commit>
# git branch -> To see list of branches
# git checkout <branch name>-> to go to specific branch
#git branch -d/D <branch name> -> to delete branch name
# git branch --oneline --all --graph -> To see tree stracture commit for all branches
#git merge <branch name> -> To merge with mastr branch and make sure you are inn master branch

#GIT REMOTE  REPO START HERE
# git remote add origin <repo url> --> to add repo from git hub
#git pull origin master- to pull from branch
# git push origin master - to push to branch
#git clone <Repo URL> --> to clone existing public repo
print (a)