# GitHub Collaboration: Issues, Pull Requests, and Reviews

Git provides version control; GitHub adds tools for planning, discussing, reviewing, and governing changes. This lab follows a change from a task to a reviewed pull request and explains repository settings that help keep the default branch dependable.

## Step 1: Track work with Issues

Use a GitHub Issue to describe a bug, feature, question, or task. A useful issue includes a clear title, context, steps to reproduce (for a bug), expected behavior, and acceptance criteria. Labels categorize work; milestones group issues and pull requests toward a target.

Reference an issue in a branch or pull request, for example `42-fix-login-validation`. In a pull request description, keywords such as `Closes #42` link and close the issue when the pull request is merged into the default branch.

For team planning, GitHub Projects can organize issues and pull requests in a table, board, or roadmap view. Keep the issue as the durable description of work and use the project view to track status.

## Step 2: Open a focused pull request

1. Create a branch for one change and commit small, understandable updates.
2. Push the branch and open a pull request (PR) against the intended base branch.
3. Explain what changed, why, how it was tested, and any risks. Link related issues.
4. Mark the PR as a draft while it is in progress; request review when ready.
5. Keep discussion and follow-up commits on the same branch so the review stays together.

Use a **draft PR** to get early feedback without signaling that the change is ready to merge. A **review request** asks specific teammates to examine the change.

## Step 3: Review and merge responsibly

Reviewers should examine the diff, check behavior and tests, ask specific questions, and approve only when the change meets the repository's standards. Authors should respond to feedback constructively and resolve conversations once addressed.

Common GitHub merge options:

- **Merge commit** preserves the branch commits and adds a merge commit.
- **Squash and merge** combines the PR commits into one commit on the base branch.
- **Rebase and merge** replays PR commits onto the base branch without a merge commit.

The repository chooses which merge methods are allowed. Choose one team policy and keep commit history consistent. Delete a merged feature branch when it is no longer needed; this does not delete the branch's commits from the merged history.

## Step 4: Protect the default branch

Repository administrators can configure branch protection or repository rulesets to require pull requests, approvals, status checks, resolved conversations, or signed commits before changes land on a branch. They can also restrict force pushes and deletion.

Require checks that genuinely protect quality (for example, tests and linting), and document who can bypass rules in emergencies. Rules and available settings can vary with repository visibility and plan.

## Step 5: Contribute through a fork

When you do not have write access, fork the repository, clone your fork, and keep the original repository as `upstream`:

~~~bash
git clone https://github.com/YOUR-USER/PROJECT.git
cd PROJECT
git remote add upstream https://github.com/OWNER/PROJECT.git
git switch -c fix/issue-42
~~~

Push your branch to `origin` (your fork) and open a PR from that branch to the original repository's target branch. To update your local default branch from the original:

~~~bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
~~~

Check the repository contribution guide and code of conduct before contributing.

## Practice: complete a PR lifecycle

1. Create an issue with a goal and acceptance criteria.
2. Create a feature branch named for the issue and implement the change.
3. Open a draft PR, describe the change and testing, and link the issue.
4. Ask a peer to review; respond to comments and update the branch.
5. Review the required checks and merge method; merge only when requirements pass.

---

**Next Lab:** Continue to [Lab 08 — Automating Workflows with GitHub Actions](../lab_08/).
