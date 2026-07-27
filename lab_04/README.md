# Mastering Git Workflows and Merge Conflict Resolution

This lab bridges the gap between basic Git usage and real-world team collaboration. You will learn how to choose and apply the right branching model for your project, when to merge versus rebase, and how to resolve merge conflicts calmly and methodically. By the end of this lab, you will be comfortable working in teams where multiple people are changing the same codebase at the same time.

## Why branching workflows matter

Branching is more than just creating a separate line of development. The strategy you choose determines how your team integrates work, releases software, and handles mistakes. Without a clear workflow, branches become chaotic, merges turn into nightmares, and code review loses meaning. A solid workflow keeps the main branch stable, makes releases predictable, and reduces the time spent fixing integration problems.

### Choosing the right workflow for your team

1. **Team size and experience** — Small teams with experienced developers often prefer trunk-based development with short-lived branches. Larger teams or teams with junior developers usually benefit from the guardrails of Git Flow or a protected main branch.

2. **Release frequency** — If you ship continuously, Git Flow may be too heavy. Trunk-based development or GitHub Flow fit continuous deployment models better.

3. **Project complexity** — Libraries and SDKs often use Git Flow because they need stable release branches and hotfix isolation. Web applications and startups often prefer simpler workflows that move faster.

4. **Tooling and platform** — Some platforms, such as GitHub, encourage GitHub Flow. Others, such as GitLab, have features optimized for Git Flow. Choose a workflow that feels native to your hosting platform.

## Step 1: Understanding Branching Models

Before resolving conflicts, you need to understand the environment in which conflicts happen. Different branching models create different types of merges and different conflict frequencies.

### Git Flow

Git Flow is a structured branching model that uses long-lived branches such as `main`, `develop`, `feature`, `release`, and `hotfix`. It is designed for projects with scheduled release cycles.

1. `main` — Contains only production-ready code. Every commit on `main` is a deployable release.

2. `develop` — The integration branch where feature branches are merged. It represents the next release under development.

3. `feature/*` — Branched from `develop` and merged back into `develop` when a feature is complete.

4. `release/*` — Branched from `develop` when preparing a new release. Only bug fixes and release tasks are added here.

5. `hotfix/*` — Branched from `main` when a critical bug is found in production. Merged back into both `main` and `develop`.

Git Flow gives you clear separation between ongoing development, releases, and emergency fixes. It is powerful but comes with overhead, making it better suited for projects with formal release schedules.

### GitHub Flow

GitHub Flow is a simpler model that uses a single `main` branch and short-lived feature branches. It is ideal for projects that deploy continuously.

1. `main` is always deployable and contains the latest approved code.

2. For every change, create a descriptive branch from `main`.

3. Commit changes to the branch and open a pull request early.

4. Discuss, review, and test the changes on the pull request.

5. Merge the branch into `main` and deploy immediately.

Because branches are short-lived and `main` is always clean, merge conflicts are usually smaller and easier to resolve. GitHub Flow works well for web applications, documentation sites, and teams practicing continuous deployment.

### Trunk-Based Development

Trunk-based development is the simplest model at its core: everyone commits to a single shared branch called `trunk` or `main`, or creates very short-lived branches that are merged within hours or days.

1. Developers either commit directly to `main` or create branches that live for less than a day.

2. Feature flags hide incomplete work so that the main branch always remains deployable.

3. Pull requests are tiny, focused, and reviewed quickly.

4. Continuous integration runs on every change to catch conflicts and regressions early.

Trunk-based development demands strong automated testing and a culture of keeping changes small. It is the preferred model for high-performing engineering organizations because it eliminates long-lived integration branches and reduces merge debt.

### Forking Workflow

The forking workflow is the standard for open-source projects. Each contributor works on their own copy of the repository.

1. A contributor forks the central repository to their own GitHub account.

2. They clone their fork locally and create feature branches.

3. Changes are pushed to their fork, and a pull request is opened against the original repository.

4. Maintainers review the pull request and merge it when approved.

This model gives maintainers tight control over who can merge code. Contributors do not need write access to the central repository, which makes it safe for public projects with many unknown contributors.

## Step 2: Merging vs Rebasing

Merging and rebasing are two ways to integrate changes from one branch into another. They produce different histories and are appropriate in different situations.

### How merging works

Merging creates a new commit that ties together the histories of two branches. The original commits from both branches are preserved exactly as they were.

1. Switch to the target branch, usually `main`, and pull the latest changes.
2. Run `git merge feature-branch`.
3. If there are no conflicts, Git creates a merge commit automatically.
4. If there are conflicts, Git pauses and asks you to resolve them before completing the merge.

Merging is safe and non-destructive. It is the correct choice when you are integrating shared branches or working in a team where other people rely on the published history.

### How rebasing works

Rebasing rewrites the branch history by moving the entire branch to begin on the tip of another branch. Instead of creating a merge commit, replays each commit from your branch on top of the target branch.

1. Switch to your feature branch.
2. Run `git rebase main` to replay your changes on top of the latest `main`.
3. If conflicts appear, resolve them one at a time.
4. Use `git rebase --continue` after each conflict resolution.
5. Use `git rebase --abort` if you want to cancel the rebase and return to the original state.

Rebasing produces a clean, linear history that is easier to read with `git log`. It is excellent for private feature branches before merging.

### When to rebase and when not to

1. **Rebase private branches** — If you are the only person working on a branch, rebase onto the latest `main` frequently to keep your branch up to date.

2. **Never rebase shared branches** — If multiple people are using a branch, rebasing rewrites public history and causes confusion for everyone else. In that case, use `git merge` instead.

3. **Rebase before merging** — A common pattern is to rebase your feature branch onto `main` locally, then merge it with a fast-forward or a clean merge commit on GitHub.

4. **Use `--force-with-lease` carefully** — After rebasing a branch that already exists on the remote, you may need to force-push. Use `git push --force-with-lease` instead of `git push --force` to avoid overwriting other people's work.

## Step 3: Merge Conflict Resolution

Conflicts happen when two branches change the same part of a file in incompatible ways. They are inevitable in team development, and knowing how to handle them is essential.

### What causes conflicts

1. Two developers edit the same line of code in parallel on different branches.
2. One developer edits a file while another developer deletes it.
3. Both branches rename the same file to different names.
4. Large refactors on long-lived branches increase the chance that overlapping changes will collide.

### Understanding conflict markers

When Git stops because of a conflict, it inserts conflict markers into the affected files. The markers show both versions of the conflicting content and make it clear what needs to be resolved.

1. `<<<<<<< HEAD` — Marks the beginning of the incoming changes from your current branch.
2. `=======` — Separates the two conflicting sections.
3. `>>>>>>> branch-name` — Marks the end of the incoming changes from the branch being merged.

### Resolving conflicts step by step

1. Identify the conflicting files by running `git status`. Git lists them under `both modified`.

2. Open each conflicting file and look for the conflict markers. Read both sides carefully to understand what each change intended to do.

3. Edit the file to remove the conflict markers and produce the correct final content. You can choose one side, combine both sides, or write something entirely new if both changes need adaptation.

4. Stage the resolved file with `git add <file-name>`.

5. After all conflicts are resolved and staged, complete the merge or rebase by running `git commit` or `git rebase --continue`.

### Using a merge tool

For complex conflicts, a visual merge tool can be easier than editing markers manually.

1. Configure a merge tool such as VS Code, Meld, or KDiff3.
2. Run `git mergetool` to open the conflicting files in the tool.
3. The tool presents both changes side by side and lets you pick hunks or specific lines.
4. Save the resolved file and close the tool.
5. Stage the resolved file with `git add`.
6. Complete the merge or rebase.

### Preventing unnecessary conflicts

1. Pull the latest changes from the target branch before starting new work.
2. Keep branches short-lived. The longer a branch lives, the more likely it is to diverge and conflict.
3. Communicate with your team about who is working on which files.
4. Break large changes into smaller pull requests that are easier to merge.
5. Rebase your feature branch onto the latest `main` regularly while you are working.

## Step 4: Advanced Conflict Scenarios

Not all conflicts are simple line-by-line overlaps. Some require careful judgment and specific Git tools.

### Rename and delete conflicts

1. If one branch renames a file and another branch modifies it, Git may report a conflict.
2. Decide whether the file should keep the new name, the old name, or both.
3. Use `git rm` or `git add` to resolve the tree state, then `git commit` to finish.

### Directory-level conflicts

1. If both branches add files with the same name in the same directory but with different casing on case-insensitive systems, Git may struggle to represent the conflict.
2. Rename one of the files to a temporary unique name, merge, then rename it to the final desired name.

### Submodule conflicts

1. If your repository uses Git submodules, a conflict in the submodule pointer means the superproject references different commits for the same submodule.
2. Enter the submodule directory, choose the correct commit or create a new merge commit inside the submodule, then update the superproject pointer and stage the change.

## Step 5: Writing Conflict-Free Collaboration Habits

The best conflict is the one you never have to resolve. Good habits drastically reduce conflict frequency and severity.

### Daily habits

1. **Pull before you push** — Always fetch and rebase or merge the latest `main` into your branch before opening a pull request.

2. **Keep PRs small** — Small pull requests are easier to review, merge, and revert. They also collide less with other people's work.

3. **Communicate hot files** — If you know you are about to make large changes to a central file, let the team know so they can coordinate.

4. **Use descriptive branch names** — Clear names help reviewers understand the scope of a branch and reduce accidental overlap.

5. **Resolve conflicts immediately** — Do not let branches drift apart for days. Rebase daily if the branch will live for more than a few hours.

## Step 6: Collaboration and Code Review

Conflict resolution is only one part of teamwork. The rest depends on how you communicate changes and review each other's work.

### Writing good pull request descriptions

1. Explain what the pull request changes and why.
2. Reference the issue or task that motivated the work.
3. Add screenshots or recordings for frontend and design changes.
4. Mark the pull request as ready for review only when it is complete and self-explanatory.

### Responding to review feedback

1. Read feedback carefully and ask clarifying questions instead of defending your code blindly.
2. Make requested changes in small, atomic commits on the same branch.
3. If you disagree, explain your reasoning with links to documentation, tests, or user impact.
4. Keep the tone professional. The goal is to improve the codebase, not to win an argument.

## Summary and Final Thoughts

Branching workflows and conflict resolution are the backbone of professional Git usage. A good workflow keeps `main` stable, makes releases predictable, and reduces the friction of team collaboration. Merge conflicts are not failures; they are natural signals that multiple people are improving the same project. By choosing the right model, rebasing thoughtfully, and resolving conflicts methodically, you turn Git from a source of frustration into a powerful coordination tool.

`Dive Deeper` — Explore interactive rebasing (`git rebase -i`) for cleaning up branch history, `git rerere` for automatically reusing recorded conflict resolutions, and `git worktree` for working on multiple branches simultaneously without switching back and forth.

Mastering workflows and conflicts is what separates Git beginners from Git professionals. Keep practicing, and collaboration will feel easier with every repository you touch.

---

**Next Lab:** Ready to level up? Continue to [Lab 05](../lab_05/)
