To creates a new Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository
```sh 
git init
```

To clone remote repository to local repository
```sh
git clone <repo>
```

To fetch or download lasted remote repository changes and update the local code from master branch
```sh
git pull
```

To upload local repository command to remote repository
```sh
git push 
```

To set author identity (Your email and name)
```sh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

To see config for system level
```sh
git config --list --show --origin
```

To see history details
```sh
git log
```

To revert changes and restore file
```sh
git restore -- <filename>
        or
git checkout -- <filname>
```

To move file freom working directory to staging area
```sh
git add
```

To know status in Git
```sh
git status
```

To know which branch you are working 
```sh
git branch
```

To fetch update from another branch
```sh
git pull origin <branch name>
```

To stash all files
```sh
git stash -a
```

To know how many stash we have 
```sh
git stash list
```


