# ChargeFinder – Git & GitHub Setup Guide

Follow these instructions to set up the project and collaborate with the team.

## 1. Clone the Project (First Time Only)

Open VS Code terminal inside the folder where you want to keep the project.

```bash
git clone https://github.com/Yusuf-J24/charge-finder.git
cd charge-finder
```

## 2. Configure Your Git Identity (First Time Only)

Set your own name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Git uses this information to identify who made each commit.

## 3. Connect to Your Frontend Branch (First Time Only)

The project lead has already created the required branches on GitHub.

**Our branch structure:**

- `main` – Contains reviewed and approved project code.
- `frontend` – Your branch for frontend development.
- `backend` – Project lead's branch for backend and database development.

Connect to your frontend branch:

```bash
git switch --track origin/frontend
```

This creates a local frontend branch connected to the frontend branch on GitHub.

**Important:**

- You only need to do this once.
- Always work on your assigned `frontend` branch.
- Never make changes directly to `main` or `backend`.

## 4. Understand the `.gitignore` File

The `.gitignore` file tells Git which files and folders should not be uploaded to GitHub.

We already have this file configured for the project.

**What you need to know:**

- You don't need to modify this file during normal frontend development.
- Upload your actual HTML, CSS, JavaScript and image files normally.
- Never upload passwords or private credentials.
- If you think a file should be ignored, check with the project lead first.

## 5. Understand the Project Folders

- `backend/` – Python and Flask backend code.
- `frontend/` – HTML, CSS, JavaScript and frontend assets.
- `database/` – MySQL database files and scripts.
- `documentation/` – Project reports, diagrams and other documentation.

**Your responsibility is to work on the `frontend/` folder.**

## 6. Daily Git Workflow

Follow these steps whenever you start and finish your work.

**A. Before starting work**

Make sure you are on your frontend branch:

```bash
git switch frontend
git status
```

If you have unfinished changes, save and commit them before pulling new changes.

Get the latest frontend changes:

```bash
git pull origin frontend
```

**B. After completing your work**

Check which files you have modified:

```bash
git status
```

Stage your frontend changes:

```bash
git add frontend/
```

Check the staged files again:

```bash
git status
```

Commit your changes:

```bash
git commit -m "Describe your changes"
```

Example:

```bash
git commit -m "Add homepage design"
```

Upload your changes to GitHub:

```bash
git push origin frontend
```

**Remember:**

- Check the files shown by `git status` before committing.
- Commit and push your completed work regularly.
- If Git shows an error or conflict you don't understand, stop and inform the project lead.

## 7. Submit Your Work for Review

Once your frontend work is ready:

1. Run `git push origin frontend` to upload your changes.
2. Open our repository on GitHub.
3. Go to **Pull requests** and click **New pull request**.
4. Select:
   - Base: `main`
   - Compare: `frontend`
5. Create the Pull Request and inform the project lead.

**What happens next?**

The project lead will:

- Review your frontend code.
- Check whether it works with the backend.
- Test the complete application.
- Request corrections if needed.

**If corrections are requested:**

1. Make the requested changes in your code.
2. Check your changes using `git status`.
3. Stage and commit the updated files.
4. Push again using `git push origin frontend`.

Your existing Pull Request will automatically show the updated work.

**Important:** Do not merge the Pull Request yourself. The project lead will handle reviewing, testing and merging approved changes into `main`.

## 8. When the Project Lead Updates the Main Branch

After approved changes are merged into `main`, the project lead will update your `frontend` branch with the latest project changes.

**What do you need to do?**

- No Git commands are required from your side for this update.
- Continue working on your assigned `frontend` branch.
- Before starting your next task, follow Section 6 to get the latest changes.

The project lead will inform you when the branch has been updated.

## 9. Important Team Rules

1. Work only on your assigned `frontend` branch.
2. Get the latest changes before starting work.
3. Check your files before committing.
4. Make requested corrections before pushing the updated work.
5. Create a Pull Request when your work is ready for review.
6. Never merge changes into `main` or `backend`.
7. If Git reports a conflict or an unfamiliar error, stop and inform the project lead.

**Our workflow:**

You develop the frontend → You commit and push → You submit a Pull Request → Project lead reviews and tests → You make requested corrections → Project lead approves and merges.

## 10. Basic Git Terminology

| Term         | Meaning                                       |
| ------------ | --------------------------------------------- |
| Clone        | Download the repository to your computer.     |
| Branch       | A separate workspace for development.         |
| Pull         | Download the latest changes.                  |
| Add          | Select changes to include in a commit.        |
| Commit       | Save changes in Git history.                  |
| Push         | Upload commits to GitHub.                     |
| Pull Request | Request a review before merging changes.      |
| Merge        | Combine changes from one branch into another. |
