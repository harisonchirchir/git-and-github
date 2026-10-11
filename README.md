# Mastering Git and GitHub

A hands-on course for learning Git and GitHub, from a first commit through team collaboration, automation, and releases. Start at [Lab 01](lab_o1/), follow the learning path on the [course home page](index.html), or use the [30-day challenge](30-day-git-challenge/) for daily practice.

## Learning path

1. **Foundations:** Labs 01–02 — Git setup, repositories, commits, and clear history.
2. **Everyday work:** Labs 04–06 — workflows, remotes, and recovery. Lab 03 is an optional hosting lesson; take it after Lab 01 or after Lab 08.
3. **Collaboration and delivery:** Labs 07–09 — pull requests, GitHub Actions, and releases.
4. **Advanced tools and practice:** Lab 10, then the 30-day challenge and its capstone.

No previous Git experience is needed. The course requires Git and terminal access; a GitHub account is needed for hosting and collaboration exercises. Each lesson page lists prerequisites, level, estimated time, outcomes, and a checkpoint with a solution hint.

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
- `30-day-git-challenge/` — 30 guided practice days with lesson references and an end-to-end capstone.

## Usage

Open `index.html` locally or visit the deployed site. The lab `index.html` files are the canonical published lessons; each lab `README.md` is a supplementary Markdown edition for reading and offline reference. When changing lesson instructions, keep the key steps, exercise, and answer guidance aligned in both formats. Use the course home page to find lessons by topic or difficulty.

Every published lab follows the same teaching pattern: prerequisites and learning outcomes, the guided lesson, a hands-on checkpoint, a knowledge check with a hint/solution, and previous/next navigation. Run `python3 scripts/check_links.py` and `python3 scripts/check_curriculum.py` before publishing to validate internal links and required lesson elements.

## Deploying as GitHub Pages

This project deploys as a static site to GitHub Pages through the workflow in `.github/workflows/static.yml`. It validates internal links and required curriculum elements, runs on pushes to `main`, and can also be started manually from the Actions tab. No build step or package installation is required.

In **Settings → Pages**, select **GitHub Actions** as the build and deployment source. The workflow publishes the site at `https://<your-username>.github.io/<repo-name>/`. Page and asset links are relative so they work under this repository path.

## License

See [LICENSE](LICENSE) for details.
