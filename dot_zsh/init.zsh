#  _       _ _
# (_)_ __ (_) |_
# | | '_ \| | __|
# |_|_| |_|_|\__|

if type brew &>/dev/null; then
  FPATH="/opt/homebrew/share/zsh-completions:$FPATH"
  source "/opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh"

  autoload -Uz compinit
  zcompdump="${ZDOTDIR:-$HOME}/.zcompdump"
  stale_zcompdump=(${~zcompdump}(N.mh+24))
  if [[ ! -e "$zcompdump" || ${#stale_zcompdump} -gt 0 ]]; then
    compinit -d "$zcompdump"
  else
    compinit -C -d "$zcompdump"
  fi
  unset zcompdump stale_zcompdump
fi

# PATHを変更する初期化処理の後でmiseを有効化する
eval "$(mise activate zsh)"
eval "$(starship init zsh)"
eval "$(direnv hook zsh)"
