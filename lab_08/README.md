# Automating Workflows with GitHub Actions

GitHub Actions runs automated workflows in response to repository events or schedules. Continuous integration (CI) commonly checks each proposed change; continuous delivery/deployment (CD) can publish approved changes. Workflows are YAML files stored under `.github/workflows/`.

## Step 1: Understand the workflow model

- A **workflow** is a YAML automation definition.
- An **event** starts it, such as a push, pull request, schedule, or manual dispatch.
- A **job** is a group of steps that runs on a runner.
- A **step** runs a shell command or a reusable action.
- **Artifacts** store and pass build outputs between jobs or make them available after a run.

Workflows can run on GitHub-hosted runners or appropriately configured self-hosted runners. Treat self-hosted runners carefully: untrusted code may execute on them.

## Step 2: Add a basic CI workflow

For a repository of static HTML and Python link-check code, create `.github/workflows/ci.yml`:

~~~yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check internal links
        run: python3 scripts/check_links.py
~~~

On pull requests, the workflow provides a status check that can be required by branch protection. For application repositories, add the appropriate test, lint, and build commands so failures block merging.

Actions are dependencies: pin them to a reviewed release or immutable commit SHA according to your security policy, and keep them updated. The version tags above are readable examples, not immutable pins.

## Step 3: Use secrets and permissions safely

Store sensitive values in GitHub Actions secrets or environment secrets, not in workflow files or source code. Pass a secret only to the step that needs it:

~~~yaml
      - name: Publish
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
        run: ./scripts/publish.sh
~~~

Do not print secret values. Workflows triggered by contributions from forks generally do not receive repository secrets; this is an important security boundary. Avoid privileged `pull_request_target` workflows that check out and execute untrusted pull-request code.

Set the narrowest permissions required. Start with `permissions: contents: read`; grant write access only to jobs that need it. Prefer short-lived, scoped credentials and review third-party actions before using them.

## Step 4: Add a deployment workflow

The repository already includes `.github/workflows/static.yml`, which deploys the static site to GitHub Pages on pushes to `main` and can be started manually. Its deployment permissions (`pages: write` and `id-token: write`) are required for Pages deployment; the separate CI example keeps read-only permissions.

Before enabling deployment, configure **Settings → Pages** to use GitHub Actions. Review workflow run logs and deployment environments when a run fails. For production systems, add environment protection rules and require approval where appropriate.

## Step 5: Debug and improve workflows

1. Open the repository's **Actions** tab and select the failed run.
2. Read the failing job and step logs; reproduce the command locally where possible.
3. Check event filters, YAML indentation, permissions, secrets availability, and runner environment.
4. Re-run only after understanding the failure; do not expose secrets in diagnostic output.
5. Use caching for dependencies when it measurably speeds up builds, and define concurrency to avoid duplicate deployments.

## Practice

1. Add a CI workflow that runs the repository's link checker on pushes and pull requests.
2. Open a PR and verify its check appears in the PR status.
3. Introduce a broken internal link in a local branch, observe the failed check, then correct it.
4. Inspect the Pages workflow permissions and explain why deployment requires more access than a read-only check.

---

**Next Lab:** Continue to [Lab 09 — Git Tags, Versioning, and GitHub Releases](../lab_09/).
