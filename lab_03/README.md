# Free Hosting For Web Projects

This lab explores the most practical free hosting platforms for web projects. Whether you are hosting a personal portfolio, a documentation site, a small web app, or a prototype, choosing the right free hosting service can save you money and simplify deployment. By the end of this lab, you will understand the strengths and limitations of GitHub Pages, Vercel, Netlify, Surge.sh, and Render, and know how to deploy projects to each platform using their respective CLIs.

## Why consider free hosting?

Free hosting allows developers, students, and hobbyists to publish web projects without paying for infrastructure. It is ideal for portfolios, open-source documentation, prototypes, and client demos. Beyond cost savings, free hosting platforms usually integrate directly with Git repositories, offer HTTPS out of the box, and handle scaling for small to moderate traffic.

### When free hosting makes sense

1. **Personal projects and portfolios** — You can showcase your work without managing servers or paying monthly fees.
2. **Documentation and tutorials** — Static documentation sites benefit from platforms that handle redirects, search, and custom domains easily.
3. **Prototypes and demos** — Rapid iteration is easier when deployment is automated and free.
4. **Learning web deployment** — Understanding hosting workflows, environment variables, and build processes is easier without financial risk.

### When to upgrade beyond free hosting

1. **High traffic or production applications** — Free tiers usually have bandwidth and build-time limits.
2. **Complex backend requirements** — Free hosting often focuses on frontend or simple serverless functions.
3. **Team collaboration needs** — Advanced previews, role management, and private deployments may require paid plans.

## Step 1: Free hosting Sites

This step introduces the most popular free hosting platforms and explains what makes each one suitable for different types of web projects.

### GitHub Pages

GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files directly from a GitHub repository and publishes them through a GitHub-owned domain. It is one of the simplest ways to host documentation sites, landing pages, and portfolios.

#### Key Benefits

1. **Completely free for public repositories** — No hidden costs, no time-limited free tiers. As long as your repository is public, hosting is free.
2. **Seamless Git integration** — Every push to the configured branch can trigger an automatic rebuild and deployment.
3. **Custom domain support** — You can connect a custom domain with HTTPS if you already own one.
4. **Jekyll support** — GitHub Pages natively supports Jekyll, making it easy to build documentation-style sites without extra build tooling.
5. **No server management** — You do not need to configure servers, install packages, or manage uptime.

#### Limitations

1. **Static sites only** — GitHub Pages does not support server-side rendering or traditional backend code. Everything must be static HTML, CSS, JavaScript, or pre-built assets.
2. **Build time limits** — Documentation and large static sites are limited to a maximum build time, which can be restrictive for very large projects.
3. **Bandwidth and file size limits** — Soft limits exist on repository size and monthly bandwidth, which may affect high-traffic projects.
4. **No server-side logic** — You cannot run backend APIs, databases, or server-side processing directly on GitHub Pages.

#### Deploying to GitHub Pages

1. Create a repository on GitHub or use an existing one.
2. Add your static site files (`index.html`, CSS, JS, images) to the repository.
3. Go to **Settings → Pages** in the repository.
4. Under **Source**, select the branch you want to deploy from, usually `main` or `master`.
5. Save the settings. GitHub will automatically build and deploy the site.
6. After a few minutes, your site will be available at `https://<your-username>.github.io/<repository-name>/`.

If you want a custom deployment workflow using GitHub Actions, you can create a workflow file under `.github/workflows/` that builds your site and deploys it using the `actions/deploy-pages` action.

#### How it stacks up

GitHub Pages is best suited for documentation, portfolios, README-driven sites, and simple static project pages. It is the most cost-effective option if your project is already hosted on GitHub and does not require backend logic.

### Vercel

Vercel is a cloud platform optimized for frontend developers. It is widely used for Next.js applications but also supports static sites, serverless functions, and other popular frameworks such as React, Vue, Svelte, and Astro.

#### Key Features and Benefits

1. **Framework-aware deployments** — Vercel automatically detects the framework you are using and configures the build process accordingly. This removes the need for manual configuration files.
2. **Zero-config deployments** — Connect a Git repository, and every push triggers a preview deployment. Production deployments happen when you merge to the main branch.
3. **Edge Network and CDN** — Vercel serves your site from a global edge network, making it fast for users around the world.
4. **Serverless Functions** — You can deploy backend API routes alongside your frontend without managing a separate server.
5. **Preview deployments** — Every pull request gets its own unique preview URL, which is extremely useful for reviewing changes before merging.

#### How to Deploy to Vercel using CLI

1. Install the Vercel CLI globally using npm:
   ```bash
   npm install -g vercel
   ```
2. Navigate to your project directory in the terminal.
3. Run the following command to log in:
   ```bash
   vercel login
   ```
4. Deploy the project by running:
   ```bash
   vercel
   ```
5. Follow the prompts to configure the project settings. Vercel will detect your project type, build settings, and output directory automatically in most cases.
6. Once complete, Vercel provides a live preview URL. To deploy to production, run:
   ```bash
   vercel --prod
   ```

#### How Does Vercel Compare to Other Hosting Services

Vercel excels with Next.js and modern frontend frameworks because of its deep framework integration. Compared to GitHub Pages, it offers more advanced build and runtime features such as serverless functions and edge caching. Compared to Netlify, it is often faster for Next.js-specific workflows, while Netlify offers stronger support for traditional static sites and form handling.

### Netlify

Netlify is a popular platform for deploying static websites and Jamstack applications. It provides a smooth developer experience through its Git-based workflow, build pipeline, and generous free tier.

#### Key Features and Benefits

1. **Continuous deployment from Git** — Netlify automatically builds and deploys your site whenever you push changes to your connected repository.
2. **Forms without backend code** — Netlify Forms adds form handling and spam filtering directly to static HTML forms without requiring backend logic.
3. **Split testing and A/B testing** — You can run experiments by splitting traffic between different deploys directly from the Netlify dashboard.
4. **Identity and authentication** — Netlify Identity makes it easy to add user authentication to static or Jamstack sites.
5. **Edge handlers and functions** — You can run serverless functions at the edge to modify requests and responses with minimal latency.

#### How to Deploy to Netlify using CLI

1. Install the Netlify CLI globally using npm:
   ```bash
   npm install -g netlify-cli
   ```
2. Log in to your Netlify account:
   ```bash
   netlify login
   ```
3. Initialize the project if you have not done so already:
   ```bash
   netlify init
   ```
4. Follow the prompts to link the project to an existing Netlify site or create a new one.
5. Deploy the project by running:
   ```bash
   netlify deploy
   ```
6. For a production deployment, use:
   ```bash
   netlify deploy --prod
   ```

Netlify also supports drag-and-drop deployment through its web interface, which is useful if you simply want to upload a built folder without connecting a Git repository.

### Surge.sh

Surge.sh is a minimalist static publishing platform designed for developers who want to deploy static files quickly from the command line without configuring complex build pipelines.

#### Key Features and Benefits

1. **Simple CLI workflow** — Surge is built around a single command that publishes the contents of a folder to the web.
2. **Custom domain support** — You can configure custom domains easily through the CLI or dashboard.
3. **Lightweight and fast** — Surge feels lightweight because it has fewer features than Vercel or Netlify, which makes it faster for small projects.
4. **No Git required** — You can deploy from any folder on your local machine, which is ideal for quick experiments or simple files.
5. **Free SSL** — Every Surge project automatically receives HTTPS support.

#### Deploying to Surge.sh using CLI

1. Install Surge globally using npm:
   ```bash
   npm install -g surge
   ```
2. Navigate to the folder containing your built static site.
3. Run the following command:
   ```bash
   surge
   ```
4. When prompted, enter your email and password to create or log into a Surge account.
5. Choose a domain name. You can use Surge's free domain or type your own custom domain.
6. Confirm the deployment. Surge will upload your files and provide a live URL.

You can redeploy updated files by running the `surge` command again in the same directory.

#### Comparing Surge.sh to Vercel and Netlify

Surge.sh is ideal for quick, simple static deployments and small experiments. It does not offer framework auto-detection, serverless functions, or the advanced build pipelines that Vercel and Netlify provide. Use Surge when you want minimal configuration and speed over advanced features.

### Render

Render is a unified cloud platform that supports static sites, web services, background workers, databases, and cron jobs. It is designed to replace smaller Heroku-like workflows while also supporting modern Jamstack deployments.

#### Unique Features and Benefits

1. **Multiple service types** — Render can host static sites, run backend web services, manage PostgreSQL databases, and execute scheduled cron jobs from a single platform.
2. **Automatic HTTPS** — Every service on Render receives free HTTPS without manual certificate management.
3. **Git-based deployments** — Connect your repository and Render will rebuild and deploy automatically on every push.
4. **Environment management** — You can set environment variables securely through the Render dashboard or CLI.
5. **Free tier with scaling options** — Render offers free static sites and free web services with limitations that can be upgraded when your project grows.

#### Deploying on Render

1. Sign up on Render and connect your Git repository.
2. Click **New** and choose **Static Site** if your project is purely frontend, or **Web Service** if it includes backend code.
3. Provide the repository, branch name, and build command appropriate for your project.
4. Set the publish directory or start command depending on the service type.
5. Click **Create Static Site** or **Create Web Service**.
6. Render will build and deploy your project, then provide a live URL.

For advanced users, Render also offers an infrastructure-as-code approach through its `render.yaml` blueprint file, which allows you to define services declaratively.

#### How Render Stacks Up Against Other Hosting Services

Render provides more backend flexibility than GitHub Pages, Vercel, Netlify, or Surge because it supports running persistent servers and databases. It sits between traditional IaaS providers and Jamstack hosts, making it a good choice when you need both frontend hosting and lightweight backend services in one place. For static-only projects, its feature set is comparable to Netlify, but with a simpler dashboard and predictable pricing.

## Summary and Final Thoughts

Choosing the right free hosting platform depends on your project type, expected traffic, and need for backend features. GitHub Pages is unbeatable for simple static documentation and portfolios. Vercel and Netlify are better for modern framework-based applications that need preview deployments and serverless functions. Surge.sh offers the fastest CLI workflow for tiny static projects. Render is the most versatile when you need both frontend and backend hosting together.

`Dive Deeper` — Explore each platform's official documentation to learn about custom domains, environment variables, edge caching, and serverless function limits. Consider deploying the same project to multiple platforms to compare build times, caching behavior, and global performance firsthand.

Mastering free hosting tools gives you the freedom to publish projects quickly, iterate confidently, and scale when necessary without being locked into expensive infrastructure.

---

**Next Lab:** Ready to level up? Continue to [Lab 04 — Mastering Git Workflows and Merge Conflict Resolution](../lab_04/)
