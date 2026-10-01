# Undoing Changes and Recovering Work

Mistakes are part of working with version control. This lab explains which Git command to use based on where the change is: in the working tree, in the staging area, in a local commit, or already published to a remote. The safest recovery starts by inspecting the repository state before changing it.

## Step 1: Inspect before undoing

~~~bash
git status
git diff
git diff --staged
git log --oneline --decorate -5
~~~

If the work might matter, save a copy or make a temporary branch before attempting a risky recovery. Avoid destructive commands when you are unsure which files or commits they affect.

## Step 2: Discard or unstage uncommitted changes

Use `git restore` to discard working-tree edits to a tracked file:

~~~bash
git restore <file>
~~~

This replaces the file with the staged version, or with `HEAD` if there is no staged version. The discarded edits are not normally recoverable, so inspect or back them up first.

To remove a file from the staging area while keeping its edits in the working tree:

~~~bash
git restore --staged <file>
~~~

To unstage everything while preserving the working-tree changes:

~~~bash
git restore --staged .
~~~

Untracked files are not removed by `git restore`; review `git status` and delete them intentionally if needed.

## Step 3: Undo a commit safely

`git revert` creates a new commit that reverses an earlier commit. It is usually the safe choice for commits already shared with others:

~~~bash
git revert <commit>
git push
~~~

For a merge commit, Git may require choosing the mainline parent with `git revert -m 1 <merge-commit>`. Confirm which parent represents the line of history you want to keep.

## Step 4: Understand reset

`git reset` moves the current branch pointer and can also change the staging area or working tree:

~~~bash
git reset --soft HEAD~1   # Undo last commit; keep changes staged
git reset --mixed HEAD~1  # Undo last commit; keep changes unstaged (default)
git reset --hard HEAD~1   # Discard commit and working-tree changes
~~~

Use `--soft` or `--mixed` only when rewriting commits that have not been shared. `--hard` discards tracked changes and is destructive. Do not reset published history unless your team explicitly coordinates a history rewrite.

**Rule of thumb:** use `restore` for file-level uncommitted edits, `revert` to undo published commits, and `reset` to reorganize private local history.

## Step 5: Temporarily set aside work with stash

Stash saves tracked modifications so you can switch context. Include untracked files when needed:

~~~bash
git stash push -m "WIP: profile form"
git stash push -u -m "Include new files"
git stash list
git stash show -p stash@{0}
git stash apply stash@{0}
git stash drop stash@{0}
~~~

`apply` keeps the stash entry; `pop` applies it and removes the entry if successful. Stash is temporary storage, not a long-term backup—commit important work.

## Step 6: Recover a lost commit with reflog

The reflog records recent movements of local branch references, including commits no longer visible in the normal history:

~~~bash
git reflog
git show <commit>
git branch recovery <commit>
~~~

Find the commit in the reflog, inspect it, then create a recovery branch before deciding how to restore the work. Reflog entries are local and expire over time; they are not a substitute for a backup.

## Practice: choose the right recovery

1. Edit a file and discard one unwanted edit using `git restore`.
2. Stage a file, then unstage it while keeping the edit.
3. Make a local commit and undo it with `git reset --soft HEAD~1`.
4. Create and push a test commit, then reverse it with `git revert`.
5. Stash a tracked edit, switch branches, and restore the stash.
6. Inspect `git reflog` and explain how a recovery branch could protect a dangling commit.

---

**Next Lab:** Continue to [Lab 07 — GitHub Collaboration](../lab_07/).
