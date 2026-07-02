#             _   _
#  _ __   __ _| |_| |__
# | '_ \ / _` | __| '_ \
# | |_) | (_| | |_| | | |
# | .__/ \__,_|\__|_| |_|
# |_|

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

# pnpm
export PNPM_HOME="$HOME/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac

# Claude Code
export PATH="$HOME/.local/bin:$PATH"

# Turso
export PATH="$PATH:$HOME/.turso"
