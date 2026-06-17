#            _
#    _______| |__  _ __ ___
#   |_  / __| '_ \| '__/ __|
#  _ / /\__ \ | | | | | (__
# (_)___|___/_| |_|_|  \___|

source $STOW_PACKAGES_PATH/zsh/.zsh/init.zsh
source $STOW_PACKAGES_PATH/zsh/.zsh/alias.zsh
source $STOW_PACKAGES_PATH/zsh/.zsh/history.zsh

# bun completions
[ -s "/Users/ichikawa/.bun/_bun" ] && source "/Users/ichikawa/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
export PATH="/opt/homebrew/opt/libpq/bin:$PATH"

# pnpm
export PNPM_HOME="/Users/ichikawa/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac

# Claude Code
export PATH="$HOME/.local/bin:$PATH"

# Turso
export PATH="$PATH:/Users/ichikawa/.turso"
