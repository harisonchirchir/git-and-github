# Introduction to Git and GitHub

This is my learning journey with Git and GitHub. I will use GitHub to host my code and Git to track changes to my code.

## What is Git?

Git is a system that tracks changes made to source code. This allows us to keep track of changes to our code and to be able to revert changes if needed.

### Step 1: Understanding Git: A Powerful Tool for Tracking Changes

#### Key Advantages of Git in Development

1. **Branching and Merging** - Git allows us to create branches to work on different features or bug fixes without affecting the main codebase.

2. **Collaboration** - Git allows us to collaborate with other developers on the same codebase.

3. **Snapshots** - Git allows us to take snapshots of our code at any point in time. This creates a clear history of changes made to our code.

4. **Speed and Efficiency** - Git is fast and efficient. It allows us to work on our code without having to worry about conflicts or merge issues.

5. **Data Integrity** - Git ensures data integrity by tracking changes to our code. This allows us to revert changes if needed.

### Step 2: Getting Started with Git

Before you can start using Git, you need to install it on your computer. Installing Git is easy and essential for your development workflow. Follow the steps below to get started with Git:

1. From the official website
2. Install Git from the command line.

#### Installing Git from the Official Website

Visit the official website: https://git-scm.com/ and download the latest version of Git that is compatible with your operating system.

#### Installing Git from the Command Line

To install Git from the command line, open your terminal or command prompt and run the following command:

~~~bash
# MacOS
brew install git

# Ubuntu/Debian-based Linux distributions
sudo apt-get update
sudo apt-get install git

# Fedora/RHEL-based Linux distributions
sudo dnf install git

# Windows
Install Git from the official website: https://git-scm.com/download/win.
~~~

#### What to Do After Installing Git

1. Follow the installation instructions. Keep the default settings unless you have a specific reason to change them.

2. Once the installation is complete, open your terminal or command prompt and run the following command to verify that Git is installed correctly and check the version number displayed on the terminal:

~~~bash
git --version
~~~

Setting up your configuration file is an important step in using Git. It allows you to configure your Git settings, such as your name and email address. Follow the steps below to set up your configuration file:

~~~bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
~~~

This will set your name and email address in the global configuration file. Make sure to replace "Your Name" and "youremail@example.com" with your actual name and email address. This information will be used to identify you when you commit changes to your code.

Verify that your configuration file is set up correctly by running the following command:

~~~bash
git config --list
~~~

The output should show your name and email address. After setting up your configuration file, you can start using Git to track changes to your code.

### Step 3: Creating and Initializing a Git Repository

Once you have Git installed and configured, you can start creating projects in your Git repository. This is where all your project's files will be stored.

1. Open your command line or terminal

For Windows users, open Command Prompt or PowerShell. macOS or Linux users can use the Terminal.

2. Navigate to your project directory

To navigate to your project location, use the command `cd` (change directory). If you are using VS Code, you can open the IDE terminal and navigate to your project directory.

3. Initialize a Git repository

Once you are in your project directory, type `git init`. This would initialize a Git repository in your project directory. This command creates a new subdirectory `.git` that contains all your necessary repository files. A skeleton of a Git repository with no commits.

4. Verify Repository Creation

After initialization, verify that the `.git` directory was created by running the following command:

~~~bash
ls -a # macOS/Linux
dir # Windows
~~~

By completing the above steps, you have successfully created a Git repository for your project. Remember, this process only initializes the repository. You will need to add files to the repository to start tracking changes and building your commits history in subsequent steps.

### Step 4: Working with Remote Repositories: An Introduction to GitHub

GitHub is a web-based platform that allows you to host your Git repositories and collaborate with other developers. When you use Git for version control on your local machine, GitHub serves as the online counterpart where you can upload (push) your code to and pull (download) code from. This allows for safe and secure storage of your code and provides a platform for collaboration.

#### Key Features of GitHub

1. **Forking and Cloning** - GitHub allows you to fork a repository to create a copy of it, and then clone it to your local machine.

2. **Collaboration** - GitHub allows multiple developers to collaborate on the same codebase, making it easy to work on projects with others.

3. **Pull Requests** - Propose changes to a repository and request that the repository owner review and merge your changes into the main codebase.

4. **Issue Tracking** - GitHub allows you to track and manage issues related to your code, making it easy to keep track of bugs, feature requests, and other tasks.

Understanding the key features of GitHub is essential for working with Git and GitHub effectively. By using GitHub alongside Git, you can collaborate with other developers, track changes to your code, and manage issues related to your projects.

### Step 5: Setting up a GitHub Account and Repository

Before you can start using GitHub, you need to create an account and a repository. Here's how to do it:

1. Go to GitHub: https://github.com/ and click on the "Sign up" button.

2. Fill in the required information, including your name, email address, and a username.

3. Verify your account by clicking on the "Verify your email address" link sent to your email.

4. Once you have verified, customize your experience by selecting whether the account is for personal use or organization and if you want updates and offers from GitHub.

After setting up your account, you are ready to create a repository. Follow the steps below to create a repository:

1. Click the plus sign `(+)` in the top right corner of the GitHub page and select "New repository".

2. Give your repository a `unique name` that helps you identify the project.

3. Write a `short description` of your project.

4. Choose a `visibility` option for your repository, such as public or private.

5. Initialize your repository with a `README.md` file, which is a standard file used to provide information about your project.

6. Consider adding a `.gitignore` file to your repository, which specifies files and directories that Git should ignore when tracking changes.

7. Click the "Create repository" button to create your repository.

With these steps completed, you have a space on GitHub where your project can live and grow, ready for version control with Git and collaboration with others.

### Step 6: Add, Commit, and Push Changes to Your Repository

Once you have made changes in your local repository, you need to add, commit, and push those changes to your remote repository on GitHub. This is a crucial step in version control that ensures all your updates are recorded and can be retrieved at any time.

#### Tracking Changes with Git

To start tracking changes in new or modified files, use the `git add` command. If you have added a file, e.g., `README.md`, you would run the following command:

~~~bash
git add README.md
~~~

For adding all files in a directory, you can use the command:

~~~bash
git add .
~~~

#### Committing Changes

After adding files, commit your changes with a clear message that describes the changes you made using the `git commit` command. This helps to understand the changes you made and provides a record of what was changed. Here's an example of a commit message:

~~~bash
git commit -m "Add README.md file with sample content"
~~~

#### Pushing Changes to GitHub

Finally, to upload your local repository changes to GitHub, execute the `git push` command. Assuming you're working on the master or main branch, you would run the following command:

~~~bash
git push origin master
git push origin main
~~~

By following these steps, you have successfully set up a GitHub repository and started tracking changes to your code.

### Step 7: Branching Out: Working with Branches in Git

Branching is a powerful feature of Git that allows you to work on different features or bug fixes without affecting the main codebase. This approach enables a parallel development workflow, making it easier to manage changes and collaborate with other developers.

#### Creating a New Branch

To create a new branch, use the `git branch` command followed by the name of the branch you want to create.

#### Switching to a Branch

To switch to a branch, use the `git checkout` command followed by the name of the branch you want to switch to.

~~~bash
git checkout -b <branch-name> # to create a new branch
git checkout <branch-name>    # to switch to an existing branch
~~~

When you switch to a branch, any changes you make will be applied to that branch only.

#### Deleting a Branch

After merging a feature or fixing bugs, you may want to delete the branch you created. To delete a branch:

~~~bash
git branch -d <branch-name>
~~~

Use `-d` for safe deletion, which prevents you from deleting branches with unmerged changes. If you're sure you want to delete a branch, use `-D` instead.

Remember that when working with branches, it is important to notify other developers of the changes you're making. This would help to avoid conflicts and ensure that everyone is working on the same codebase.

### Step 8: Collaborative Development with Pull Request on GitHub

A pull request is the central collaboration development process for developers. They allow you to notify members about the changes you have made and pushed to a branch in a repository on GitHub. Through pull requests, you can discuss how the project should be done and how to merge the changes made by you and other developers.

Here are the steps to create and merge a pull request:

1. Fork the repository - Start by forking the repository you want to contribute to.

2. Clone the forked repository - Clone the forked repository to your local machine.

3. Implement the changes - Make the necessary changes to the codebase.

4. Push the changes - Push your changes to your new branch and its commits to the forked repository.

5. Open a pull request - Open a pull request to the original repository to propose your changes.

6. Review and Discuss - Review the changes and discuss with the project maintainers.

7. Finalize and Merge - Once the changes are approved, merge the pull request to the main branch.

This process not only streamlines contributions but also ensures that every change is reviewed and discussed before being merged into the main codebase. Collaborators can provide feedback and suggestions to improve the codebase, ensuring that it remains robust and maintainable.

Remember, effective collaboration via pull requests is essential for maintaining a healthy and robust codebase. By following these steps, you can contribute to open-source projects and make a positive impact on the community.

## Conclusion

Mastering Git and GitHub is an essential skill for developers. It allows you to collaborate effectively with other developers, track changes to your code, and manage issues related to your projects.

`Dive Deeper` - There are many resources available to learn more about Git and GitHub. Consider exploring topics such as merging conflicts, using `git stash`, or leveraging GitHub Actions for automating your workflow.

Proficiency in Git and GitHub will open up a world of opportunities for you as a developer.

---

**Next Lab:** Ready to level up? Continue to [Lab 02 - The Ultimate Guide to Writing a Good Commit Message](../lab_02/README.md)
