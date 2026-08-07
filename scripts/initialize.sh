#!/bin/bash

set -e

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
repo_dir=$(cd -- "$script_dir/.." && pwd)

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

# Install Homebrew
if [ ! -f /opt/homebrew/bin/brew ]; then
  log 'Setup Homebrew'
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
  log "Homebrew already installed."
fi

eval "$(/opt/homebrew/bin/brew shellenv)"

if ! command -v mise >/dev/null 2>&1; then
  log 'Setup mise'
  brew install mise
else
  log "mise already installed."
fi

mise trust "$repo_dir/mise.toml"
mise -C "$repo_dir" bootstrap
