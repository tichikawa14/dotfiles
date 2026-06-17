#  _       _ _
# (_)_ __ (_) |_
# | | '_ \| | __|
# |_|_| |_|_|\__|

eval "$(starship init zsh)"
eval "$(mise activate zsh)"

if type brew &>/dev/null; then
  FPATH=$(brew --prefix)/share/zsh-completions:$FPATH
  source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

  autoload -Uz compinit
  compinit
fi

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/ichikawa/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/ichikawa/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/ichikawa/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/ichikawa/google-cloud-sdk/completion.zsh.inc'; fi

# Option + → を次の単語に進むように設定
bindkey '^[^[[C' forward-word

# Option + ← を前の単語に戻るように設定
bindkey '^[^[[D' backward-word

# Ctrl + u を bashの挙動と合わせる
bindkey '^U' backward-kill-line
