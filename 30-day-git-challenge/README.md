# 30-Day Git Challenge

This challenge is designed to help you practice Git and GitHub step by step. Each day focuses on one core topic so you can build confidence through repetition and hands-on work.

## How to use this challenge

1. Pick one day at a time.
2. Complete the exercise in your own practice repository.
3. Use the linked lab or command examples whenever you need a reference.
4. Keep a short log of what you learned in a `notes.md` file or commit message.

## Day-by-day plan

### Day 1 — Install and configure Git

Goal: Set up Git locally with your name and email.

Tasks:
- Install Git
- Confirm it works with `git --version`
- Configure `user.name` and `user.email`

Solution reference:
- [Lab 01 — Introduction to Git and GitHub](../lab_o1/)

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Day 2 — Create your first repository

Goal: Learn how to initialize a repo and inspect the hidden Git metadata.

Tasks:
- Create a new folder
- Run `git init`
- Check the `.git` folder exists

Solution reference:
- [Lab 01 — Introduction to Git and GitHub](../lab_o1/)

```bash
mkdir git-practice
cd git-practice
git init
ls -la
```

### Day 3 — Track your first changes

Goal: Understand `git status`, `git add`, and `git commit`.

Tasks:
- Create a `README.md`
- Check status
- Add files
- Commit with a clear message

Solution reference:
- [Lab 01 — Introduction to Git and GitHub](../lab_o1/)

```bash
git status
git add README.md
git commit -m "Add README for project setup"
```

### Day 4 — Write a good commit message

Goal: Practice commit clarity and structure.

Tasks:
- Make 2–3 commits using a clear subject and body
- Explain what changed and why

Solution reference:
- [Lab 02 — The Ultimate Guide to Writing a Good Commit Message](../lab_02/)

```bash
git commit -m "feat: add landing page"
```

### Day 5 — Use `.gitignore`

Goal: Prevent junk files from being tracked.

Tasks:
- Create a `.gitignore`
- Ignore `.env`, `node_modules`, `.DS_Store`, and logs
- Commit the file

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
touch .gitignore
printf "node_modules/\n.env\n.DS_Store\n" >> .gitignore
git add .gitignore
git commit -m "Add project ignore rules"
```

### Day 6 — Inspect project history

Goal: Learn how to read Git history.

Tasks:
- View log entries
- Use `--oneline`
- Check commit authors and dates

Solution reference:
- [Lab 05 — Everyday Git](../lab_05/)

```bash
git log --oneline --decorate --graph --all
git log --oneline -n 5
```

### Day 7 — Undo small mistakes

Goal: Understand `git restore` and `git checkout` safely.

Tasks:
- Modify a file
- Restore it without committing
- Revert a recent commit if necessary

Solution reference:
- [Lab 06 — Undoing and Recovering](../lab_06/)

```bash
git restore README.md
git revert HEAD
```

### Day 8 — Understand reset vs revert

Goal: Learn the difference between discarding and undoing commits.

Tasks:
- Make a bad commit
- Practice `git reset --soft` and `git revert`
- Explain the difference

Solution reference:
- [Lab 06 — Undoing and Recovering](../lab_06/)

```bash
git reset --soft HEAD~1
git revert HEAD
```

### Day 9 — Work with branches

Goal: Create and switch branches safely.

Tasks:
- Create a feature branch
- Commit changes there
- Switch back to main

Solution reference:
- [Lab 04 — Mastering Git Workflows](../lab_04/)

```bash
git checkout -b feature/login-page
git checkout main
```

### Day 10 — Merge a branch

Goal: Learn how to merge without losing progress.

Tasks:
- Merge a feature branch into `main`
- Review the commit history afterwards

Solution reference:
- [Lab 04 — Mastering Git Workflows](../lab_04/)

```bash
git checkout main
git merge feature/login-page
```

### Day 11 — Resolve merge conflicts

Goal: Fix conflicts carefully and keep the correct code.

Tasks:
- Create conflicting edits on the same line
- Resolve them with Git markers removed
- Commit the resolution

Solution reference:
- [Lab 04 — Mastering Git Workflows](../lab_04/)

```bash
git status
git add resolved-file
git commit -m "Merge feature branch with conflict resolution"
```

### Day 12 — Use stashing

Goal: Save work temporarily without committing.

Tasks:
- Change files
- Run `git stash`
- Restore with `git stash pop`

Solution reference:
- [Lab 06 — Undoing and Recovering](../lab_06/)

```bash
git stash
git stash list
git stash pop
```

### Day 13 — Create and push a repo to GitHub

Goal: Link a local project to a remote repository.

Tasks:
- Create a GitHub repo
- Add the remote
- Push the `main` branch

Solution reference:
- [Lab 01 — Introduction to Git and GitHub](../lab_o1/)

```bash
git remote add origin git@github.com:YOUR-USER/YOUR-REPO.git
git push -u origin main
```

### Day 14 — Clone and inspect a remote

Goal: Learn how to copy a repo and view its branch setup.

Tasks:
- Clone a public repo
- Check remotes and branches
- Pull updates

Solution reference:
- [Lab 05 — Everyday Git](../lab_05/)

```bash
git clone https://github.com/owner/repo.git
cd repo
git remote -v
git pull origin main
```

### Day 15 — Fork a repository

Goal: Understand the open-source contribution workflow.

Tasks:
- Fork a repo on GitHub
- Clone your fork
- Create a feature branch and push it

Solution reference:
- [Lab 07 — GitHub Collaboration](../lab_07/)

```bash
git checkout -b update-docs
git push -u origin update-docs
```

### Day 16 — Open a pull request

Goal: Practice the standard GitHub review workflow.

Tasks:
- Push a branch
- Open a PR
- Add a title and description

Solution reference:
- [Lab 07 — GitHub Collaboration](../lab_07/)

```bash
git push -u origin feature-branch
```

### Day 17 — Use GitHub issues

Goal: Track bugs, tasks, and improvements.

Tasks:
- Create an issue
- Add labels and a clear description
- Link it to a branch or PR if needed

Solution reference:
- [Lab 07 — GitHub Collaboration](../lab_07/)

### Day 18 — Work with tags and releases

Goal: Mark milestones in your project history.

Tasks:
- Create a lightweight tag
- Create an annotated tag
- Push tags to GitHub

Solution reference:
- [Lab 09 — Git Tags, Versioning, and GitHub Releases](../lab_09/)

```bash
git tag v1.0.0
git tag -a v1.1.0 -m "Release 1.1.0"
git push origin --tags
```

### Day 19 — Use git log filters

Goal: Search history quickly and understand project evolution.

Tasks:
- Use `--grep`, `--author`, `--since`, and `--stat`
- Find commits by keyword

Solution reference:
- [Lab 05 — Everyday Git](../lab_05/)

```bash
git log --oneline --grep "feature"
git log --author "Your Name" --oneline
git log --since="2024-01-01" --oneline
```

### Day 20 — Use `git blame`

Goal: Trace who changed a line and when.

Tasks:
- Run `git blame` on a file
- Identify the cause of a change

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
git blame README.md
```

### Day 21 — Rebase a branch

Goal: Learn how a rebase can rewrite a branch history.

Tasks:
- Create a branch with multiple commits
- Rebase it on top of the latest `main`
- Resolve conflicts carefully

Solution reference:
- [Lab 04 — Mastering Git Workflows](../lab_04/)

```bash
git checkout feature-branch
git rebase main
```

### Day 22 — Cherry-pick a commit

Goal: Apply one commit from another branch to your current branch.

Tasks:
- Create a commit on one branch
- Cherry-pick it into another branch

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
git cherry-pick <commit-sha>
```

### Day 23 — Practice `git stash` with multiple changes

Goal: Save and restore complex work safely.

Tasks:
- Modify two files
- Stash them
- Switch branches
- Restore changes

Solution reference:
- [Lab 06 — Undoing and Recovering](../lab_06/)

```bash
git stash push -m "WIP: feature work"
git stash list
git stash pop
```

### Day 24 — Create a feature branch with a clean review flow

Goal: Practice branch hygiene before a pull request.

Tasks:
- Create a branch from `main`
- Commit small logical changes
- Push and open a PR

Solution reference:
- [Lab 07 — GitHub Collaboration](../lab_07/)

### Day 25 — Fix a bug with a hotfix branch

Goal: Simulate a production fix without disturbing the main work.

Tasks:
- Create a `hotfix` branch
- Fix the issue
- Merge it after review

Solution reference:
- [Lab 04 — Mastering Git Workflows](../lab_04/)

### Day 26 — Use `git bisect`

Goal: Find the commit that introduced a bug.

Tasks:
- Mark a known-good and known-bad commit
- Run `git bisect`
- Identify the faulty commit

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
git bisect start
git bisect bad
git bisect good <good-commit>
```

### Day 27 — Work with submodules

Goal: Learn how Git repositories can include other repos.

Tasks:
- Add a submodule
- Initialize and update it
- Commit the parent repo changes

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
git submodule add https://github.com/owner/repo.git vendor/repo
```

### Day 28 — Use Git LFS for large files

Goal: Track large assets efficiently.

Tasks:
- Install Git LFS
- Track `*.png` or `*.zip`
- Commit the assets

Solution reference:
- [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/)

```bash
git lfs install
git lfs track "*.png"
git add .gitattributes
```

### Day 29 — GitHub Actions basics

Goal: Automate checks when you push code.

Tasks:
- Add a simple workflow
- Run a shell command such as `echo` or `npm test`
- Inspect the Actions tab

Solution reference:
- [Lab 08 — Automating Workflows with GitHub Actions](../lab_08/)

### Day 30 — Final project challenge

Goal: Use a disposable GitHub repository to simulate a small team workflow from setup through a versioned release.

1. Create a GitHub repository with a README, clone it, and make an initial commit on `main`.
2. Create `feature/project-summary`. Change a README line, commit it, and push the branch.
3. On `main`, edit that same line differently, commit, and push the change. This intentional divergence is only for the disposable practice repository.
4. Switch to the feature branch, fetch, and merge `main`. Resolve the README conflict, remove the markers, stage, and commit the resolution.
5. Push the branch and open a pull request targeting `main`. Describe and review the change, then merge it.
6. Update local `main`, create an annotated `v1.0.0` tag on the merged commit, push the tag, and publish a GitHub Release with notes.

```bash
git switch -c feature/project-summary
# Edit and commit the README change on the feature branch.
git add README.md
git commit -m "feat: add project summary"
git push -u origin feature/project-summary

git switch main
# Edit the same README line differently, then commit it on main.
git add README.md
git commit -m "docs: clarify project purpose"
git push origin main

git switch feature/project-summary
git fetch origin
git merge main
# Resolve README.md, remove conflict markers, then:
git add README.md
git commit -m "Merge main and resolve README conflict"
git push

# After the pull request is merged on GitHub:
git switch main
git pull origin main
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
```

Expected result: a reviewed pull request is merged to `main`, the conflict is resolved cleanly, and the merged commit has a `v1.0.0` GitHub Release.

Hints:
- Inspect changes with `git status` and `git diff`; verify no conflict markers remain before committing.
- If needed, use `git merge --abort` to cancel the practice merge.
- Before tagging, check `git log --oneline -1` and inspect the tag with `git show v1.0.0`.

Solution references: [Lab 01](../lab_o1/), [Lab 04](../lab_04/), [Lab 07](../lab_07/), and [Lab 09](../lab_09/).

## Quick solution map

If you want the fastest path to the answer, use these references:

- Setup and basics: [Lab 01](../lab_o1/)
- Commit quality: [Lab 02](../lab_02/)
- Branching and conflicts: [Lab 04](../lab_04/)
- Everyday Git commands: [Lab 05](../lab_05/)
- Recovery and safety: [Lab 06](../lab_06/)
- Collaboration and PRs: [Lab 07](../lab_07/)
- GitHub Actions: [Lab 08](../lab_08/)
- Tags and releases: [Lab 09](../lab_09/)
- Advanced Git tools: [Lab 10](../lab_10/)

## Recommended workflow

- Complete 5 days at a time
- Repeat the challenge with a different repository
- Use real pull requests when possible
- Keep each commit focused and meaningful

This 30-day challenge is meant to build confidence through repetition, not perfection. The goal is to keep practicing until the Git commands become natural.
