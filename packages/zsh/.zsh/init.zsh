#  _       _ _
# (_)_ __ (_) |_
# | | '_ \| | __|
# | | | | | | |_
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

# zellij がいつも自動的に開かれるように設定
eval "$(zellij setup --generate-auto-start zsh)"

# Ctrl + d でペインが閉じられしまうため、シェルを終了しないように設定
setopt IGNORE_EOF
# Ctrl + d の補完プロンプトを無効にするカスタムウィジェットを作成
function custom-delete-char-or-list() {
  if [[ -z $BUFFER ]]; then
    # バッファが空の場合は何もしない
    true
  else
    # バッファが空でない場合はデフォルトの後方文字削除を実行
    zle delete-char
  fi
}

# カスタムウィジェットを zle に登録
zle -N custom-delete-char-or-list

# Ctrl + d をカスタムウィジェットにバインド
bindkey '^D' custom-delete-char-or-list

# Option + → を次の単語に進むように設定
bindkey '^[^[[C' forward-word

# Option + ← を前の単語に戻るように設定
bindkey '^[^[[D' backward-word
