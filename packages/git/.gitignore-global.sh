touch ~/.gitignore_global

echo '.idea' / >> ~/.gitignore_global
echo '.directory/' >> ~/.gitignore_global
echo '.DS_Store' >> ~/.gitignore_global
echo '.swp' >> ~/.gitignore_global

git config --global core.excludesfile ~/.gitignore_global
