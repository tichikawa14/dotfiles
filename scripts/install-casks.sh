#!/bin/bash

set -e

if [ "$(uname)" != "Darwin" ]; then
  echo "Not macOS!"
  exit 0
fi

# miseはHomebrewが導入した既存caskを引き継げないため、Homebrewへ委譲する。
casks=(
  arc
  brave-browser
  claude
  cleanshot
  codex-app
  cursor
  dockdoor
  expo-orbit
  font-hackgen
  ghostty
  google-chrome
  karabiner-elements
  libreoffice
  linear
  nani
  ngrok
  notion
  orbstack
  raycast
  slack
  spotify
  zed
  zoom
)

if [ "${DOTFILES_CHECK_ONLY:-0}" = 1 ]; then
  brew info --cask "${casks[@]}" >/dev/null
  exit 0
fi

for cask in "${casks[@]}"; do
  if brew list --cask "$cask" >/dev/null 2>&1; then
    continue
  fi

  brew install --cask "$cask"
done
