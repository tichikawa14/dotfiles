touch ~/.gitignore_global

.idea/ >> .gitignore_global
.directory/ >> .gitignore_global
.DS_Store >> .gitignore_global
.swp >> .gitignore_global

git config --global core.excludesfile ~/.gitignore_global
