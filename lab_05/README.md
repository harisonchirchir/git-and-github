# Everyday Git: Inspecting Changes and Working with Remotes

This lab covers the commands used throughout a normal Git workday. You will inspect the working tree before changing it, review commit history, connect local and remote repositories, and synchronize branches without confusing fetch, pull, and push.

## Step 1: Understand the three local states

Git work happens across three local states:

1. **Working tree** — the files you are currently editing.
2. **Staging area (index)** — the exact changes selected for the next commit.
3. **Repository history** — commits already recorded in the current repository.

Use `git status` frequently. It tells you which files are modified, staged, untracked, or involved in an unfinished merge or rebase.

~~~bash
git status
git status --short
~~~

The short form uses status codes: `??` means untracked, ` M` means modified but unstaged, and `M ` means staged. The first column describes the staging area; the second describes the working tree.

## Step 2: Review changes before staging and committing

Inspect the exact changes rather than staging blindly:

~~~bash
git diff                 # Unstaged changes
git diff --staged        # Staged changes
git diff -- README.md    # Changes in one file
~~~

Stage only the files or hunks that belong in the commit:

~~~bash
git add README.md
git add -p               # Interactively choose change hunks
git diff --staged
git commit -m "Document remote workflow"
~~~

`git add .` is convenient, but check `git status` first so generated files, credentials, or unrelated edits do not enter the commit.

## Step 3: Read and search project history

~~~bash
git log --oneline --graph --decorate --all
git show <commit>
git log --oneline -- README.md
git log -S"search text" --oneline
~~~

`git log` shows commits, `git show` displays a commit and its changes, and path-limited or `-S` searches help locate when a file or piece of text changed. Use `git diff <base>..<target>` to compare two commits or branches.

## Step 4: Connect local and remote repositories

A **remote** is a named URL for another copy of the repository. `origin` is a conventional name, not a special Git keyword.

~~~bash
git remote -v
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote show origin
~~~

If you have not cloned the repository, `git clone <url>` creates a local copy and configures its remote automatically. A fork-based project commonly uses `origin` for your fork and `upstream` for the original:

~~~bash
git remote add upstream https://github.com/OWNER/REPOSITORY.git
git fetch upstream
~~~

## Step 5: Fetch, pull, and push

`git fetch` downloads remote commits and updates remote-tracking references such as `origin/main`, but does not change your current branch or files. Inspect the incoming changes, then integrate them:

~~~bash
git fetch origin
git log --oneline HEAD..origin/main
git diff HEAD..origin/main
git merge origin/main
~~~

`git pull` fetches and integrates in one command. Depending on configuration, it may merge or rebase; teams should agree on a policy. To explicitly rebase your current private feature branch on the remote main branch:

~~~bash
git pull --rebase origin main
~~~

Push your local branch to publish commits. The first push commonly sets its upstream:

~~~bash
git push -u origin <branch-name>
git push
~~~

An upstream links a local branch to its remote-tracking branch, making later `git pull` and `git push` commands shorter. If a push is rejected because the remote has new commits, fetch and integrate those commits before trying again—do not force-push shared history.

## Step 6: Practice the daily loop

1. Run `git status` and inspect the current branch.
2. Fetch the remote and review new commits.
3. Create or switch to a short-lived feature branch.
4. Make a focused change; inspect it with `git diff`.
5. Stage the intended files or hunks and inspect with `git diff --staged`.
6. Commit with a clear message, then push the branch and open a pull request.

The purpose of these checks is to make every commit intentional and every synchronization predictable.

---

**Next Lab:** Continue to [Lab 06 — Undoing Changes and Recovering Work](../lab_06/).
