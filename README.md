[![Installation and Setup Check](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml)
[![Shellcheck](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml)

# dotfiles for Apple Silicon MacBook

macOS 用 dotfiles です。設定ファイルは [chezmoi](https://www.chezmoi.io/) で管理し、アプリケーションと CLI ツールは [Homebrew Bundle](https://github.com/Homebrew/homebrew-bundle) で管理します。

- Shell: Z shell
- Terminal: [Warp](https://www.warp.dev) with [Starship](https://starship.rs/)
- Editor: [RubyMine](https://www.jetbrains.com/ruby/)

## 初回セットアップ

```sh
xcode-select --install
git clone https://github.com/tichikawa14/dotfiles.git ~/dotfiles
cd ~/dotfiles
./scripts/initialize.sh
brew bundle install --verbose --file=dot_Brewfile
brew bundle install --verbose --file=dot_Brewfile.mas
chezmoi init --source ~/dotfiles
chezmoi apply
./mac/setup.sh
```

初回セットアップでは以下を実行します。

- Homebrew の初期導入
- `dot_Brewfile` と `dot_Brewfile.mas` による `brew bundle install`
- `chezmoi apply`
- `mac/setup.sh`

chezmoi を個別に初期化する場合は、clone 済みのこのリポジトリを source directory として使います。

```sh
chezmoi init --source ~/dotfiles
chezmoi source-path
chezmoi apply
```

このリポジトリには `.chezmoi.toml.tmpl` があるため、`chezmoi init --source ~/dotfiles` で `sourceDir` を含む chezmoi 設定が生成されます。`chezmoi source-path` が `~/dotfiles` を指していることを確認してください。

## 日常運用

初回セットアップ後は、普段の作業ディレクトリから `~/dotfiles` へ移動する必要はありません。chezmoi は source directory を覚えているため、以下のコマンドはどこからでも実行できます。

設定変更は、基本的に chezmoi 経由で行います。

```sh
chezmoi edit --apply ~/.zshrc
chezmoi edit --apply ~/.gitconfig
chezmoi edit --apply ~/.config/starship.toml
```

ホーム側を直接編集した場合だけ、source state へ取り込みます。

```sh
chezmoi re-add ~/.zshrc
chezmoi re-add ~/.gitconfig
chezmoi re-add ~/.config/starship.toml
```

`chezmoi apply` は source state から `$HOME` への反映です。ホーム側の変更を取り込むコマンドではありません。

差分確認は次のコマンドを使います。

```sh
chezmoi status
chezmoi diff
```

変更後は source directory に移動して commit します。

```sh
chezmoi cd
git status --short
git diff
git add .
git commit -m "zsh 設定を更新"
git push
```

## Homebrew 管理

Brewfile は chezmoi 管理対象として `$HOME/.Brewfile` と `$HOME/.Brewfile.mas` に反映されます。source state ではそれぞれ `dot_Brewfile` と `dot_Brewfile.mas` です。

インストールは明示的に実行します。

```sh
brew bundle install --verbose --file="$(chezmoi source-path ~/.Brewfile)"
brew bundle install --verbose --file="$(chezmoi source-path ~/.Brewfile.mas)"
```

現時点では `chezmoi apply` 時の `brew bundle` 自動実行は入れていません。`brew bundle install` はアプリのインストールや更新を伴うため、dotfile 反映とは分けて明示実行する方針です。

Homebrew で追加した項目を Brewfile に反映する場合は、内容を確認してから source state を更新します。

```sh
brew bundle dump --file="$(chezmoi source-path ~/.Brewfile)" --force
chezmoi cd
git diff -- dot_Brewfile
```

Mac App Store アプリは `dot_Brewfile.mas` に追記してください。

## その他手動で行う設定

### Homebrew

最初はパスを通す必要があります。

```sh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### Xcode

- Xcode のライセンスに同意する

### .zsh_history 移行

- Mac のファイル共有で新しい PC に移す

### システム環境設定

- システム環境設定 > ディスプレイ > 解像度を適宜変更
- システム環境設定 > 通知 > 適宜 on にする
- システム環境設定 > サウンド > 通知音変更
- システム環境設定 > コントロールセンター > バッテリー > 割合(%)を表示 on にする
- システム環境設定 > デスクトップと Dock > デフォルトの Web ブラウザ > Vivaldi に設定
- システム環境設定 > ディスプレイ > 解像度 スペースを拡大 に設定
- システム環境設定 > ディスプレイ > 複数のディスプレイを配置 変更
- システム環境設定 > 壁紙・スクリーンセーバー > 適宜変更
- システム環境設定 > ロック画面 > ディスプレイオフ適宜設定
- システム環境設定 > ユーザーとグループ > ユーザーアイコン編集
- システム環境設定 > キーボード > ショートカット > Spotlight > Spotlight 検索を表示のショートカットを off にする
- システム環境設定 > キーボード > ショートカット > ファンクションキー > 標準のファンクションキーとして使用を on にする
- システム環境設定 > キーボード > ショートカット > 修飾キー > Caps Lock キーを Command キーにする
- システム環境設定 > ソフトウェアアップデート > 自動アップデート off にする

### Finder

- よく使う項目にホームディレクトリなどを追加

### GitHub

- SSH 秘密鍵・公開鍵を登録する
- `gh auth login` でログインする

### RubyMine

- Edit > Manage IDE Settings > IDE Setting Sync > Sync Plugins Silently
- Preferences > Version Control > Github アカウント追加

### Alfred

- General > Alfred Hotkey を cmd + space にする
- General > Where are you を Japan に設定
- Features > Web Bookmarks > Google Chrome Bookmarks を on にする
- Features > Calculator > Ignore thousands grouping separator にチェックを入れる
- Appearance > Alfred Modern Dark
- Appearance > Options > Hide menu bar icon を on にする
- Appearance > Options > Show Alfred on > mouse screen にする
- Advanced > Force Keyboard を ABC にする
- クリップボード履歴を `~/Library/Application Support/Alfred/Databases/clipboard.alfdb` から移して再起動
- workflow から各アプリ用の hotkey を追加

### VSCode

- GitHub アカウントでログインして設定を同期させる

### AWS

- `aws configure` で認証情報を設定する

### HyperSwitch

- Run HyperSwitch in the background をチェックする

### RunCat

- 一般 > ログイン時に自動で RunCat を起動をチェックする
- システム情報 > CPU 負荷 メニューバーに表示をチェックする
