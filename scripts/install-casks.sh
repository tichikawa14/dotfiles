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
  chatgpt
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
  stablyai/orca/orca
  raycast
  slack
  snapzy
  spotify
  t3-code
  zed
  zoom
)

# Orca は公式の Homebrew cask がなく開発元の tap にあるため、tap しないと info も install も解決できない。
taps=(
  stablyai/orca
)

for tap in "${taps[@]}"; do
  if ! brew tap | grep -qx "$tap"; then
    brew tap "$tap"
  fi
done

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
