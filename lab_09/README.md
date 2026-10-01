# Git Tags, Versioning, and GitHub Releases

Commits record development history; tags give important commits stable names, often for software versions. GitHub Releases build on tags to publish release notes and downloadable files. This lab covers lightweight and annotated tags, semantic versioning, and a safe release sequence.

## Step 1: Understand tags

A **lightweight tag** is a simple name pointing to a commit. An **annotated tag** stores metadata such as the tagger, date, and message; it is generally preferred for releases.

~~~bash
git tag
git tag -a v1.0.0 -m "Release 1.0.0"
git show v1.0.0
git tag -a v0.9.0 <commit> -m "Release 0.9.0"
~~~

Tags are not automatically included when pushing an individual branch. Publish one tag or all local tags explicitly:

~~~bash
git push origin v1.0.0
git push origin --tags
~~~

Avoid moving or reusing published release tags. Teammates and automation may depend on the tag continuing to identify the same commit.

## Step 2: Apply semantic versioning

Semantic Versioning uses `MAJOR.MINOR.PATCH`:

- **MAJOR** for incompatible public changes.
- **MINOR** for backward-compatible functionality.
- **PATCH** for backward-compatible fixes.

For example, `v2.4.1` is the first patch release after version `2.4.0`. Pre-release identifiers such as `v2.5.0-rc.1` indicate a release candidate. Choose a versioning policy appropriate to the project and document what counts as a breaking change.

## Step 3: Prepare and publish a release

1. Ensure the intended code is merged into the release branch and all checks pass.
2. Review the changes since the previous release: `git log --oneline v1.0.0..HEAD`.
3. Update version metadata and changelog if the project uses them; commit those updates.
4. Create an annotated tag on the intended release commit.
5. Push the tag to GitHub.
6. Create a GitHub Release for that tag, summarize user-facing changes, list breaking changes and migration steps, and attach built artifacts only when needed.

~~~bash
git log --oneline v1.0.0..HEAD
git tag -a v1.1.0 -m "Release 1.1.0"
git push origin v1.1.0
~~~

The GitHub Releases page can generate notes from merged pull requests and associated issues when repository settings and metadata support it. Review generated notes before publishing; automation can omit context or include unintended details.

## Step 4: Inspect and correct tags carefully

~~~bash
git tag --list "v1.*"
git show --no-patch v1.1.0
git ls-remote --tags origin
~~~

If a tag was created incorrectly and has **not** been shared, delete and recreate it locally:

~~~bash
git tag -d v1.1.0
git tag -a v1.1.0 <correct-commit> -m "Release 1.1.0"
~~~

If a tag has already been pushed, coordinate with maintainers before changing it. Deleting and recreating a published release tag can cause collaborators' local references and release artifacts to disagree.

## Practice

1. Inspect repository history and identify a commit suitable for a practice release.
2. Create an annotated pre-release tag and inspect it with `git show`.
3. Push the tag to a test repository and create a GitHub Release with concise notes.
4. Explain why a release tag should not be silently moved to a different commit.

---

**Next Lab:** Continue to [Lab 10 — Advanced Git Tools and Repository Management](../lab_10/).
