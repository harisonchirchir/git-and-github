# The Ultimate Guide to Writing a Good Commit Message

This lab focuses on one of the most important soft skills in software development: writing clear, consistent, and meaningful Git commit messages. A good commit message is more than a formality; it is a communication tool that tells the story of your project, helps teammates understand changes quickly, and makes debugging and maintenance far easier. By the end of this lab, you will understand the structure of a strong commit message, how to apply conventions like Conventional Commits, and how to maintain a clean, professional project history.

### Important of good commit messages

1. **Project clarity and maintainability:** Good commit messages act as a historical record that explains why changes were made. This makes it easier for anyone working on the project to understand its evolution, onboard quickly, and maintain the codebase without relying on memory or scattered documentation.

2. **Efficient debugging and troubleshooting:** When a bug appears, a well-maintained commit history allows you to use tools like `git bisect` to pinpoint exactly when the issue was introduced. Clear commit messages make this process much faster by providing human-readable context at each step.

3. **Professional collaboration and code review:** Teams depend on commit messages to understand what changed before reviewing code, merging branches, or preparing releases. Consistently writing high-quality messages shows discipline, reduces miscommunication, and keeps collaboration smooth across distributed or growing teams.

## Step 1: The Basics of Git Commits Messages

### Documenting Chnages

Every commit is a snapshot of your work. Writing clear commit messages is essential because they serve as the primary documentation of why a change was made. Good commit messages help you and your team understand the project's history, debug issues, and maintain code quality over time.

### Anatomy of a Commit Message

A well-written commit message should contain the following elements:

1. **Title:** A short, imperative summary of the change (ideally under 50 characters).

2. **Body:** A longer explanation of what changed and why. This is where you provide context, reasoning, and any important details that the title cannot convey.

3. **Footer:** Optional section for metadata, such as breaking change notes, issue references, or co-author credits.

### Utilizing Components Effectively

Here are some tips on how to use each part of the commit structure effectively:

1. **Title:** Make it descriptive and action-oriented. Use the imperative mood, such as "Add user authentication" rather than "Added user authentication" or "Adds user authentication". This keeps the commit history consistent and readable.

2. **Body:** Explain the motivation behind the change. Describe the problem you are solving and how the change addresses it. If the change is non-obvious, provide enough detail so someone unfamiliar with the context can understand why it was necessary.

3. **Footer:** Use this space for references like `Fixes #123` or `BREAKING CHANGE: removed old API endpoint`. This ensures that commit history is linked directly to project management tools and that breaking changes are clearly communicated.

## Step 2: Convectional Commits: Enforcing Consistency in Commit Messages

Conventional Commits is a lightweight convention for writing commit messages that enables automated tooling, changelog generation, and semantic versioning. Every commit message follows a structured format that makes the history machine-readable and human-friendly.

1. **Types:** The first word of the commit message indicates the kind of change. Common types include `feat` for new features, `fix` for bug fixes, `docs` for documentation, `style` for formatting changes, `refactor` for code restructuring, `test` for adding tests, and `chore` for maintenance tasks.

2. **Scope:** An optional parenthetical section that indicates which part of the codebase is affected. For example, `feat(auth): add login rate limiting` immediately tells a reviewer that the change is specific to the authentication module.

3. **Description:** A short, imperative sentence explaining what the change does. Keep it concise but informative.

4. **Body:** An optional longer explanation providing additional context, reasoning, or implementation details. Use this when the change is complex or requires background knowledge.

5. **Footer:** An optional area for metadata, such as `BREAKING CHANGE:` notes or issue references. This is especially important for libraries and APIs where consumers need to know about backward-incompatible changes.

Implemeting Conventional commits brings several advantages to development teams:

1. **Enhanced Readability:** The standardized format makes it easy to scan commit history and understand the nature of each change at a glance.

2. **Automated Tooling Comptibility:** Tools can parse conventional commits to generate changelogs, determine version bumps, and trigger deployment pipelines.

3. **Improved Collaboration:** Team members communicate more clearly when every commit message follows the same predictable structure.

## Step 3: Best Practices for Writing Commit Messages

Writing great commit messages is a habit that comes from following simple rules. The goal is to make every commit self-contained, informative, and easy to review.

1. **Keeping it concise yet descriptive:** Aim for a title under 50 characters and a body wrapped at 72 characters per line. Be direct but thorough. A good commit message should explain what changed and why, without forcing the reader to inspect the diff.

2. **Focusing on "what" and "why":** Describe the reason for the change, not just the mechanics. Instead of saying "Updated index.js", say "Refactor index.js to improve error handling for invalid user input". Context is everything.

3. **Using the imperative mood:** Write the title as if you are giving an instruction: "Add payment validation" instead of "Added payment validation". This keeps the commit history consistent and professional.

4. **Reviewing and revising before finalizing:** Before you commit, read your message out loud. If it sounds awkward or unclear, rewrite it. A few extra seconds of editing prevents hours of confusion later.

5. **Leveraging commit message templates:** Use a `.gitmessage.txt` file or Git hooks to enforce a template. This reduces friction and ensures that every contributor follows the same conventions.

6. **Avoiding ambiguity:** Stay away from vague language. "Fix stuff" or "WIP" are not acceptable final commit messages. Be specific about what was fixed and why.

7. **Linking to relevant issues:** Reference issue trackers, Jira tickets, or pull request IDs directly in the footer or body. For example, `Closes #42` automatically closes the issue when the commit is merged.

## Step 4: Commit Message Linting and Validation Tools

In visual studio code, you can use the following extensions to help you write better commit messages:

1. **Commitizen:** A command-line tool that walks you through each part of a conventional commit message, ensuring you do not miss required fields. It acts as an interactive wizard for commits.

2. **Commitlint:** A linter for commit messages that enforces rules such as character limits, allowed types, and required sections. It can be integrated into Git hooks using `husky` or `lint-staged` to block invalid commits.

3. **GitLens:** An extension that enriches the Git experience in VS Code with inline blame annotations, commit search, and rich commit details. It makes reviewing commit history and writing meaningful messages much easier by showing context directly in the editor.

## Step 5: Mantaining a Clean Commit History

A clean commit history is a valuable asset. It makes code review easier, simplifies debugging, and helps new team members understand how the project evolved. Just like clean code, a clean history requires intention and discipline.

### The Value of Structural Commits History

A structured commit history:

1. Makes it easy to identify when a bug was introduced using `git bisect`.
2. Enables safe reverts of individual features without affecting unrelated changes.
3. Improves code review by giving reviewers a logical narrative of the work.
4. Supports automated changelogs and release notes.

### Techniques for Commit History Optimization

1. **Interactive Rebasing:** Use `git rebase -i` to reorder, squash, or edit commits before merging. This allows you to clean up messy local history, fix incorrect messages, and group related changes into single coherent commits.

2. **Logical Grouping with Fixup and squash:** When making incremental fixes during code review, use `git commit --fixup <commit-hash>` or `git commit --squash <commit-hash>` to mark small follow-up commits that will automatically be combined during an interactive rebase.

## Conclusion

A great commit message is a small investment that pays off every time someone reads your project history. By following conventions, being descriptive, and using the right tools, you turn commits into a powerful form of communication.

`Dive Deeper` - Explore tools like `git rebase -i`, `git notes`, and advanced `git log` formatting to further refine your workflow. Consider integrating commitlint and commitizen into your team's CI pipeline to maintain consistency across all contributors.

Mastering commit messages is a fundamental step toward becoming a more disciplined and collaborative developer.

---

**Next Lab:** Ready to level up? Continue to [Lab 03](../lab_03/README.md)
