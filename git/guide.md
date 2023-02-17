### Add to stage
```
git add <file>
```

### Add stage to repository 
```
git commit -m "<message>"
```


### To unstage (Remove New Files from Staged Files)
```
git restore --staged <file>
```


### To discard changes in working directory (Remove Existing Files from Staged Files)
```
git restore <file>
```

### Move stage to last commit -> The command can also be used to restore the content in the index with --staged, or restore both the working tree and the index with --staged --worktree.
```
git restore --staged --worktree <file>
or
git reset --hard HEAD 
```

### If you have happened to stage files using 'git add [fileName]' and you want to untrack them from the stage, you can use the following command:
```
git rm -r --cached [fileName]
```

### Git log of commits 
```
git log --oneline 
```

### Git reset
![reset](./reset.png)
* --soft: **uncommit changes**, changes are left staged (index).
* --mixed (default): **uncommit + unstage changes**, changes are left in working tree.
* --hard: uncommit + **unstage + delete changes**, nothing left.

### Explain more git reset
* --hard should be easy to understand, it restores everything
* --mixed (default) :
    - unstaged files: don't change
    - staged files: move to unstaged
    - commit files: move to unstaged
* --soft:
    - unstaged files: don't change
    - staged files: dont' change
    - commit files: move to staged

```
git reset [--soft, --mixed, --hard] <ref>
```