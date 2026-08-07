#  _              _     _           _
# | | _____ _   _| |__ (_)_ __   __| |
# | |/ / _ \ | | | '_ \| | '_ \ / _` |
# |   <  __/ |_| | |_) | | | | | (_| |
# |_|\_\___|\__, |_.__/|_|_| |_|\__,_|
#           |___/

unset FZF_DEFAULT_OPTS
export FZF_DEFAULT_OPTS="--color=bg+:#555555"
export FZF_CTRL_R_OPTS="--layout=reverse --with-nth=2.."
FZF_CTRL_T_COMMAND= FZF_ALT_C_COMMAND= source "/opt/homebrew/opt/fzf/shell/key-bindings.zsh"

# Gitブランチ切り替え
function fzf-git-branch () {
  local selected_branch
  selected_branch="$(git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads | fzf --prompt="branch > " --layout=reverse)"
  if [ -n "$selected_branch" ]; then
    zle -I
    git switch -- "$selected_branch"
    zle reset-prompt
  fi
}
zle -N fzf-git-branch
bindkey '^]' fzf-git-branch

# ディレクトリ履歴
if [[ -n $(echo ${^fpath}/chpwd_recent_dirs(N)) && -n $(echo ${^fpath}/cdr(N)) ]]; then
  autoload -Uz chpwd_recent_dirs cdr add-zsh-hook
  add-zsh-hook chpwd chpwd_recent_dirs
  zstyle ':completion:*' recent-dirs-insert both
  zstyle ':chpwd:*' recent-dirs-default true
  zstyle ':chpwd:*' recent-dirs-max 1000
  zstyle ':chpwd:*' recent-dirs-file "$HOME/.cache/chpwd-recent-dirs"
fi

function fzf-cdr () {
  cdr -r
  local selected_dir="$(printf '%s\n' "${reply[@]}" | fzf --prompt="cdr >" --layout=reverse --query "$LBUFFER")"
  if [ -n "$selected_dir" ]; then
    BUFFER="cd -- ${(q)selected_dir}"
    CURSOR=$#BUFFER
    zle reset-prompt
  fi
}
zle -N fzf-cdr
bindkey '^G' fzf-cdr

# go-task
function select-task () {
  task_name=$(task -a --json | jq -r '.tasks[].name' | fzf --layout=reverse)
  if [ -n "$task_name" ]; then
    BUFFER="task $task_name"
    CURSOR=$#BUFFER
    zle reset-prompt
  fi
}
zle -N select-task
bindkey '^T' select-task

# Option + → を次の単語に進むように設定
bindkey '^[^[[C' forward-word

# Option + ← を前の単語に戻るように設定
bindkey '^[^[[D' backward-word

# Ctrl + u をbashの挙動と合わせる
bindkey '^U' backward-kill-line
