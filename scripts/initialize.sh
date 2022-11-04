#!/bin/bash

set -e

# Utils
log() {
  message=$1
  echo 📌 "$message"
}

if [ "$(uname)" != "Darwin" ]; then
  echo "Not macOS!"
  exit 1
fi

if [ "$(uname -m)" != "arm64" ]; then
  echo "Not arm64!"
  exit 1
fi

chsh -s /bin/zsh

# Install Homebrew
if [ ! -f /opt/homebrew/bin/brew ]; then
  log 'Setup Homebrew'
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)";
  wait
  echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile
  eval $(/opt/homebrew/bin/brew shellenv)
else
  log "Homebrew already installed."
fi
