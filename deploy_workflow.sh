#!/bin/bash

set -e

# 1. Copy CSV into app directory
cp ../secure_data.csv ./data/secure_data.csv

# 2. Add to git, commit, push
git add -f data/secure_data.csv
git commit -m "TEMP: Add sensitive CSV for deployment"
git push origin main

# 3. Deploy via Python script
python deploy_to_posit.py

# 4. Remove CSV from repo and filesystem, commit and push
git rm --cached data/secure_data.csv
rm ./data/secure_data.csv
git commit -m "Remove sensitive CSV after deployment"
git push origin main

# 5. (Optional) Re-add to .gitignore for future safety
if ! grep -Fxq "data/secure_data.csv" .gitignore
then
  echo "data/secure_data.csv" >> .gitignore
  git add .gitignore
  git commit -m "Re-add sensitive CSV to .gitignore"
  git push origin main
fi

echo "Deployment complete and sensitive data removed from GitHub."
