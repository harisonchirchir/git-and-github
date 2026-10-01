# Advanced Git Tools and Repository Management

This lab introduces tools for moving individual commits, finding the change that introduced a bug, investigating line history, working on multiple branches at once, and managing repositories with dependencies or large binary assets. These features are valuable, but use them only when they fit the project's needs.

## Step 1: Apply one commit with cherry-pick

`git cherry-pick` applies the changes from an existing commit onto the current branch and creates a new commit:

~~~bash
git switch release-branch
git cherry-pick <commit>
~~~

This is useful for backporting a focused fix to a release branch. The new commit has a different commit ID because its parent is different. If conflicts occur, resolve and stage the files, then run `git cherry-pick --continue`; use `git cherry-pick --abort` to cancel.

Avoid cherry-picking broadly between branches when a normal merge is more appropriate; repeated cherry-picks can duplicate changes and complicate history.

## Step 2: Find a regression with bisect

`git bisect` uses binary search across commit history to locate the commit that introduced a problem. You identify a known-good commit and a known-bad one, then test the revisions Git checks out:

~~~bash
git bisect start
git bisect bad
git bisect good <known-good-commit>
~~~

At each step, run the test or reproduce the bug, then label the checked-out commit `git bisect good` or `git bisect bad`. When Git identifies the first bad commit, inspect it and end the session:

~~~bash
git bisect reset
~~~

You can automate the test with `git bisect run <test-command>` when the command returns zero for good commits and nonzero for bad ones. Ensure the test is reliable and works across older revisions.

## Step 3: Investigate file history with blame

~~~bash
git blame -L 20,40 path/to/file
git show <commit>
~~~

`git blame` shows the commit and author associated with each line. Use it to find context, not to assign fault: a line's last edit may not explain why the code exists. Follow up by reading the commit, pull request, and related discussion.

## Step 4: Work on multiple branches with worktrees

A worktree checks out another branch into a separate directory while sharing the same repository data:

~~~bash
git worktree add ../project-hotfix hotfix/urgent-fix
git worktree list
~~~

When finished, remove that working directory from Git's worktree registry:

~~~bash
git worktree remove ../project-hotfix
~~~

The target branch generally cannot be checked out in two worktrees at the same time. Save or commit any work before removing a worktree.

## Step 5: Know when submodules are appropriate

Submodules record a specific commit from another Git repository inside the parent repository. They are useful when a dependency must remain an independently versioned repository, but add steps for cloning, updating, and collaboration:

~~~bash
git submodule add https://github.com/OWNER/DEPENDENCY.git vendor/dependency
git clone --recurse-submodules <repository-url>
git submodule update --init --recursive
~~~

The parent project stores a pointer to a submodule commit, not a copy of its complete history. Contributors need access to the submodule repository and must commit changes there before updating the pointer in the parent.

## Step 6: Use Git LFS for large files

Git stores complete snapshots efficiently for text, but frequently changing large binaries can make repository history grow quickly. Git LFS replaces tracked large files in Git commits with small pointer files and stores the actual content through an LFS server. Hosting providers may impose storage and bandwidth quotas.

~~~bash
git lfs install
git lfs track "*.psd"
git add .gitattributes
git add design.psd
git commit -m "Track design assets with Git LFS"
~~~

Commit `.gitattributes` so other contributors know which file patterns use LFS. Git LFS does not automatically shrink binary files already committed in history; migrating existing history is a separate, disruptive operation that requires coordination.

## Choosing the right tool

- Use **cherry-pick** for a small, specific commit on another branch.
- Use **bisect** when you can identify good and bad revisions and reliably test between them.
- Use **blame** to find a line's history and then investigate its broader context.
- Use **worktrees** when separate simultaneous checkouts improve your workflow.
- Use **submodules** for independently versioned repositories with clear ownership.
- Use **Git LFS** for large binary assets, after reviewing hosting quotas and team setup.

## Practice

1. Cherry-pick a test commit onto a temporary branch; inspect the new commit.
2. Run `git bisect` on a small example with a known regression.
3. Use `git blame` to locate a change, then read its full commit context.
4. Create and remove a temporary worktree.
5. Explain how submodule pointers and Git LFS pointer files differ from ordinary tracked files.

---

**All labs:** Return to the [Mastering Git and GitHub home page](../).
