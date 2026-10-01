# Mastering Git and GitHub

A structured, hands-on learning journey covering Git fundamentals, commit best practices, GitHub workflows, Pull Requests, and automation. This repository is organized as a series of labs that build on each other, taking you from basic version control to real-world collaboration workflows.

## Project Structure

- `lab_o1/` — Introduction to Git and GitHub: installation, initialization, branching, and first push.
- `lab_02/` — The Ultimate Guide to Writing a Good Commit Message: commit anatomy, conventional commits, linting, and history hygiene.
- `lab_03/` — Free Hosting For Web Projects: GitHub Pages, Vercel, Netlify, Surge, and Render.
- `lab_04/` — Mastering Git Workflows and Merge Conflict Resolution.
- `lab_05/` — Everyday Git: inspect changes, history, remotes, fetching, and pulling.
- `lab_06/` — Undoing and Recovering: restore, revert, reset, stash, and reflog.
- `lab_07/` — GitHub Collaboration: issues, pull requests, reviews, and repository rules.
- `lab_08/` — GitHub Actions: automate checks and deployments with workflows.
- `lab_09/` — Tags and Releases: versioning and publishing project releases.
- `lab_10/` — Advanced Git Tools: cherry-pick, bisect, submodules, and Git LFS.
- `30-day-git-challenge/` — Challenge topics are outlined; hands-on exercises are coming soon.

## Usage

Open `index.html` locally or visit the deployed site, then follow the labs in order. Each lab has a standalone `index.html` page and a `README.md` with the lesson text.

## Deploying as GitHub Pages

This project deploys as a static site to GitHub Pages through the workflow in `.github/workflows/static.yml`. It runs on pushes to `main` and can also be started manually from the Actions tab. No build step or package installation is required.

In **Settings → Pages**, select **GitHub Actions** as the build and deployment source. The workflow publishes the site at `https://<your-username>.github.io/<repo-name>/`. Page and asset links are relative so they work under this repository path.

## License

See [LICENSE](LICENSE) for details.
