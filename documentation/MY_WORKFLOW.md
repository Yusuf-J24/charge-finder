# ChargeFinder – My Daily Git & GitHub Workflow

## My Responsibilities

- Backend development
- Database management
- Reviewing Pratham's frontend work
- Frontend, backend and database integration testing
- Managing all merging operations

## 1. Before Starting Backend Work

Open the ChargeFinder project in VS Code.

Check your Git status:

```bash
git status
```

If you have unfinished changes, commit or safely save them before switching branches.

Switch to your backend branch:

```bash
git switch backend
```

Get the latest backend changes from GitHub:

```bash
git pull origin backend
```

Now you are ready to work.

**Important:** You don't need to merge `main` into `backend` every day. Do this only when `main` has received new approved changes.

## 2. After Completing Backend Work

Check your modified files:

```bash
git status
```

Stage your backend and database changes:

```bash
git add backend/ database/
```

Check the staged files:

```bash
git status
```

Commit your changes:

```bash
git commit -m "Describe your changes"
```

Example:

```bash
git commit -m "Add database connection"
```

Push your changes to GitHub:

```bash
git push origin backend
```

Your backend changes are now uploaded to GitHub.

## 3. When Pratham Submits Frontend Work

Pratham will:

1. Complete his frontend development.
2. Push his changes to the `frontend` branch.
3. Create a Pull Request from `frontend` to `main`.

My responsibilities:

1. Review his frontend code.
2. Check whether it is compatible with the backend.
3. Test the frontend with the Python backend and MySQL database.
4. Check whether important features work correctly.
5. Request corrections from Pratham if needed.

**Important:** A successful code review does not automatically mean the application works correctly.

Do not merge the Pull Request into `main` before integration testing.

## 4. Integration Testing and Approval

Before merging frontend changes into `main`:

1. Bring the frontend and backend changes together in a separate testing environment or temporary integration branch.
2. Connect the frontend with the Python backend and MySQL database.
3. Test important features, such as station listings, search and station submissions.
4. Ask Pratham to correct any frontend issues.
5. Test again after corrections.

Once everything works correctly, approve and merge the tested changes into `main`.

**Keep `main` stable. Only tested and approved code should enter it.**

## 5. After Merging Approved Changes into Main

Whenever successfully tested changes are merged into `main` on GitHub, update your local branches.

**Step A: Update your local main branch**

```bash
git switch main
git status
git pull origin main
```

Make sure you have no unfinished changes before switching branches or merging.

**Step B: Update your backend branch**

```bash
git switch backend
git pull origin backend
git merge main
git push origin backend
```

This brings the latest approved changes from `main` into your backend branch.

**Step C: Update Pratham's frontend branch**

```bash
git switch frontend
git pull origin frontend
git merge main
git push origin frontend
```

This brings the latest approved changes from `main` into Pratham's frontend branch.

**Important:**
- You are merging `main` into the development branches, not the other way around.
- You are responsible for these updates.
- You don't need to repeat these steps every day. Do this only when new approved changes have been merged into `main`.

## 6. Integration Testing Commands – To Be Decided Later

When Pratham submits his first Pull Request, we will work out the exact commands for integrating his frontend with your backend.

We will:

1. Check the actual repository and branch status.
2. Create or use a separate testing environment or temporary integration branch.
3. Bring the required frontend and backend changes together.
4. Test the complete application with MySQL.
5. Fix any problems before merging approved changes into `main`.

**Important:**

- Do not guess or run integration commands without checking the actual project status.
- Do not use `main` as a testing branch.
- We will go through the commands together, step by step, using the actual repository.

This will help prevent accidental merges and keep `main` stable.

## 7. Important Rules to Avoid Mistakes

1. Work on your assigned `backend` branch.
2. Pratham works on the `frontend` branch.
3. Check `git status` before switching branches or merging.
4. Commit and push completed backend changes regularly.
5. Review and test frontend changes before approving them.
6. Never merge untested code into `main`.
7. I handle all final merging and branch synchronization.
8. If Git reports a conflict or an unfamiliar error, stop and resolve it carefully before continuing.

## Quick Reference

| Branch | Responsibility |
|---|---|
| `main` | Stable, tested and approved project code |
| `backend` | My development branch |
| `frontend` | Pratham's development branch |

**Our workflow:**

Develop → Commit → Push → Review → Integrate → Test → Approve → Merge into `main` → Update development branches.

**Final reminder:** Keep this workflow as your reference. When Pratham submits his first Pull Request, we will handle the exact integration-testing commands together based on the actual repository state. Do not guess the commands or rush the merging process.