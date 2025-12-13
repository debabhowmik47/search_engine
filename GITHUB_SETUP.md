# How to Push to GitHub

Complete guide to push your Multi-LLM Search Agent to GitHub.

## Prerequisites

### 1. Install Git

**Windows:**
- Download from: https://git-scm.com/download/win
- Run installer, use default options
- Restart your computer

**Linux:**
```bash
sudo apt update
sudo apt install git
```

**Mac:**
```bash
brew install git
```

### 2. Create GitHub Account

1. Go to https://github.com
2. Click "Sign Up"
3. Create account (free)
4. Verify email

### 3. Configure Git

First time only! Run these commands in terminal/PowerShell:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your real name and email.

---

## Steps to Push to GitHub

### Step 1: Create Repository on GitHub

1. **Go to GitHub**
   - Open https://github.com
   - Log in

2. **Create New Repository**
   - Click "+" icon (top right)
   - Click "New repository"
   - Or go directly to: https://github.com/new

3. **Fill in Details**
   - **Repository name**: `intellisearch3` (or any name)
   - **Description**: "Multi-LLM Search Agent with DuckDuckGo, Arxiv, and Wikipedia" (optional)
   - **Public or Private**: Choose Public (so others can find it)
   - **Initialize with**: Leave unchecked
   - Click "Create repository"

4. **Copy Repository URL**
   - You'll see something like: `https://github.com/yourname/intellisearch3.git`
   - Copy this URL (you'll use it next)

### Step 2: Initialize Local Repository

In your project folder, open PowerShell/Terminal and run:

```bash
git init
```

This creates a hidden `.git` folder that tracks changes.

### Step 3: Add Files

Add all project files to tracking:

```bash
git add .
```

This stages all files (except those in `.gitignore`).

### Step 4: Create First Commit

```bash
git commit -m "Initial commit: Multi-LLM Search Agent with Groq and Google support"
```

This saves a snapshot of all files.

### Step 5: Add Remote Repository

Connect to GitHub repository:

```bash
git remote add origin https://github.com/yourname/intellisearch3.git
```

Replace `yourname` with your actual GitHub username!

### Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

This uploads all files to GitHub!

---

## Complete Command Reference

### Windows PowerShell
```powershell
# 1. Navigate to project folder
cd C:\Users\ISHIKA\OneDrive\Desktop\intellisearch3

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. Create first commit
git commit -m "Initial commit: Multi-LLM Search Agent"

# 5. Add remote (replace yourname!)
git remote add origin https://github.com/yourname/intellisearch3.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

### Linux/Mac Terminal
```bash
# 1. Navigate to project folder
cd ~/Desktop/intellisearch3

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. Create first commit
git commit -m "Initial commit: Multi-LLM Search Agent"

# 5. Add remote (replace yourname!)
git remote add origin https://github.com/yourname/intellisearch3.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

---

## Authentication

### First Time Push Warning

When you push, Git asks for authentication:

```
Username for 'https://github.com': yourname
Password for 'https://yourname@github.com': 
```

**Two Options:**

#### Option 1: GitHub Token (Recommended - Secure)

1. **Generate Token**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token"
   - Select "Generate new token (classic)"
   - Give it a name: "intellisearch3"
   - Check: `repo` (full control of private repositories)
   - Click "Generate token"
   - Copy the token (long string of letters/numbers)

2. **Use Token as Password**
   ```
   Username: yourname
   Password: [paste the token here]
   ```

3. **Save for Later**
   - Store token in safe place
   - Use for all future pushes

#### Option 2: Password (Simpler but Less Secure)

Just use your GitHub password:
```
Username: yourname
Password: your-github-password
```

**Note**: GitHub removed password authentication for Git in 2021. Use Token method.

#### Option 3: SSH (Advanced)

For repeated pushes without password entry:

```bash
# Generate SSH key (one time)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add public key to GitHub
# Instructions: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

# Use SSH URL instead
git remote add origin git@github.com:yourname/intellisearch3.git
```

---

## Verify Success

After pushing, verify on GitHub:

1. **Go to your repository**
   - https://github.com/yourname/intellisearch3

2. **Check Files are Visible**
   - Should see all your project files
   - README.md should display on homepage
   - Folders (agents, config, utils) visible

3. **Check Commit**
   - Click "X commits" link
   - Should see your commit message

Great! Your project is on GitHub! 🎉

---

## Making Changes & Pushing Again

After initial push, workflow is simpler:

```bash
# 1. Make changes to files...

# 2. Stage changes
git add .

# 3. Commit
git commit -m "Your change message"

# 4. Push
git push origin main
```

---

## Troubleshooting

### Error: "remote origin already exists"

**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/yourname/intellisearch3.git
```

### Error: "Authentication failed"

**Solutions:**
1. Use token instead of password
2. Check spelling of GitHub username
3. Verify token hasn't expired

### Error: "fatal: not a git repository"

**Solution:**
```bash
git init
```

### Files not pushing

**Solution:**
```bash
# Check what will be committed
git status

# Add any missing files
git add .

# Try push again
git push origin main
```

### .env file accidentally pushed

**Emergency:**
1. Regenerate all API keys immediately
2. Run:
   ```bash
   git rm --cached .env
   git commit -m "Remove .env with API keys"
   git push
   ```
3. Add to .gitignore if not there
4. Regenerate all API keys in GitHub Secrets if using Actions

---

## Sharing Your Project

Once on GitHub:

### Share Repository URL
Send this link to others:
```
https://github.com/yourname/intellisearch3
```

### Let Others Clone It
They can run:
```bash
git clone https://github.com/yourname/intellisearch3.git
cd intellisearch3
pip install -r requirements.txt
python main.py
```

### Add a License (Optional)

If you want to specify usage terms:

1. Create `LICENSE` file in root folder
2. Add license text (MIT, Apache, etc.)
3. Commit and push

**MIT License (Simple, Permissive):**
https://opensource.org/licenses/MIT

---

## Next Steps (After Push)

### Add to GitHub Profile

1. Go to https://github.com/yourname
2. Edit profile bio to mention your project
3. Pin repository to profile

### Enable Features

**1. Discussions** (for community questions)
- Settings → Discussions → Enable

**2. Issues** (for bug tracking)
- Settings → Features → Issues → checked

**3. GitHub Pages** (optional website)
- Settings → Pages
- Source: Main branch
- Publishes docs as website

### Collaborate

Invite others to contribute:
- Settings → Collaborators
- Add GitHub usernames

---

## Common Git Commands Reference

```bash
# Clone a repository
git clone https://github.com/user/repo.git

# Check status
git status

# View changes
git diff

# View commit history
git log

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Create a branch
git checkout -b feature-name

# Switch branches
git checkout main

# Merge branch into main
git merge feature-name

# Delete branch
git branch -d feature-name
```

---

## Support & Resources

- **GitHub Docs**: https://docs.github.com
- **Git Tutorial**: https://git-scm.com/book
- **GitHub Help**: https://support.github.com
- **Git Basics**: https://git-scm.com/docs

---

## Summary

You're ready to push! Follow these steps in order:

1. ✓ Create GitHub account & repository
2. ✓ Install Git
3. ✓ Run: `git init` → `git add .` → `git commit -m "..."` → `git remote add ...` → `git push`
4. ✓ Verify files on GitHub
5. ✓ Share URL with others!

**Good luck! Your project is about to go live! 🚀**
