#!/bin/bash
# SpeakGerman — Push to GitHub
# Run this once from Terminal to initialise and push all files to github.com/mrees/german

set -e

GITHUB_TOKEN="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"
GITHUB_USER="mrees"
REPO="german"

echo "🚀 Pushing SpeakGerman to github.com/$GITHUB_USER/$REPO …"

# Navigate to the project folder
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Initialise git if not already done
if [ ! -d ".git" ]; then
  git init
  git branch -M main
fi

# Set remote (overwrite if exists)
git remote remove origin 2>/dev/null || true
git remote add origin "https://$GITHUB_TOKEN@github.com/$GITHUB_USER/$REPO.git"

# Stage all files
git add -A

# Commit
git commit -m "Add SpeakGerman app — 30 lessons, index, shared engine" 2>/dev/null || \
  git commit --allow-empty -m "Update SpeakGerman app"

# Push (creates repo if using GitHub CLI; otherwise repo must exist)
echo ""
echo "📡 Pushing to GitHub…"
git push -u origin main --force

echo ""
echo "✅ Done! Your app is at: https://github.com/$GITHUB_USER/$REPO"
echo "🌐 Enable GitHub Pages in repo Settings → Pages → Deploy from branch: main"
echo "   Then your app will be live at: https://$GITHUB_USER.github.io/$REPO/"
