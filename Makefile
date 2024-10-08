PHONY: all
all: initialize brew-bundle brew-bundle-mas stow-packages gitignore-global mac-setup @cmatrix

PHONY: initialize
initialize:
	@./scripts/initialize.sh

.PHONY: brew-bundle
brew-bundle:
	brew bundle install --verbose --no-lock --file=./packages/brewfiles/.Brewfile

.PHONY: brew-bundle-mas
brew-bundle-mas:
	brew bundle install --verbose --no-lock --file=./packages/brewfiles/.Brewfile.mas

.PHONY: brew-bundle-ci
brew-bundle-ci:
	grep -Ev "awscli|cocoapods" ./packages/brewfiles/.Brewfile > ./packages/brewfiles/.Brewfile.ci
	brew bundle --verbose --no-lock --file=./packages/brewfiles/.Brewfile.ci

.PHONY: stow-packages
stow-packages:
	@echo	"------------Start updating dotfiles symbolic link.------------"
	@./scripts/stow_packages.sh
	@echo "--------------------Finished Successfully.--------------------"

.PHONY: gitignore-global
gitignore-global:
	@./packages/git/.gitignore-global.sh

.PHONY: mac-setup
mac-setup:
	@./mac/setup.sh
