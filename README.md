[![Installation and Setup Check](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml)
[![Shellcheck](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml)

# dotfiles(for AppleSilicon MacBook)

This dotfiles for macOS are managed with [Homebrew Bundle](https://github.com/Homebrew/homebrew-bundle), [GNU stow](https://www.gnu.org/software/stow/) and [asdf](https://asdf-vm.com/).

- Shell: Z shell
- Terminal: [Warp](https://www.warp.dev) with [Starship](https://starship.rs/)
- Editor: [RubyMine](https://www.jetbrains.com/ruby/)

## セットアップ

```
$ xcode-select --install
$ git clone https://github.com/tichikawa14/dotfiles.git
$ cd ~/dotfiles
$ make all
```

## その他手動で行う設定(TODO)

### Homebrew

最初はパスを通す必要あり([scripts/initialize.sh](https://github.com/tichikawa14/dotfiles/blob/main/scripts/initialize.sh#L27-L29)では対応できず...)
```
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```

### Xcode

- Xcodeのライセンス同意

### .zsh_history移行

- Macのファイル共有で新しいPCに移す

### システム環境設定

- システム環境設定 > ディスプレイ > 解像度を適宜変更
- システム環境設定 > 通知 > 適宜 on にする
- システム環境設定 > サウンド > 通知音変更
- システム環境設定 > コントロールセンター > バッテリー > 割合(%)を表示 on にする
- システム環境設定 > デスクトップとDock > デフォルトのWebブラウザ > Vivaldi に設定
- システム環境設定 > ディスプレイ > 解像度 スペースを拡大 に設定
- システム環境設定 > ディスプレイ > 複数のディスプレイを配置 変更
- システム環境設定 > 壁紙・スクリーンセーバー > 適宜変更
- システム環境設定 > ロック画面 > ディスプレイオフ適宜設定
- システム環境設定 > ユーザーとグループ > ユーザーアイコン編集
- システム環境設定 > キーボード > ショートカット > Spotlight > Spotlight 検索を表示のショートカットを off にする
- システム環境設定 > キーボード > ショートカット > ファンクションキー > 標準のファンクションキーとして使用を on にする
- システム環境設定 > キーボード > ショートカット > 修飾キー > Caps Lockキーを Commandキー にする
- システム環境設定 > ソフトウェアアップデート > 自動アップデート off にする

### Dock整理

![](https://gyazo.com/af64ba2a3e40858be4a2479baa7eb639)

### Finder

- よく使う項目にホームディレクトリなどを追加

### GitHub

- SSH秘密鍵・公開鍵の登録
　(参考)https://chaika.hatenablog.com/entry/2021/05/06/083000
- `gh auth login`コマンドでログインする

### RubyMine

- Edit > Manage IDE Settings > IDE Setting Sync > Sync Plugins Silently
- Preferences > Version Control > Githubアカウント 追加

### Alfred

- General > Alfred Hotkey を cmd + space にする
- General > Where are you を Japan に設定
- Features > Web Bookmarks > Google Chrome Bookmarks を on にする
- Features > Calculator > Ignore thousands grouping separator にチェックを入れる
- Appearance > Alfred Modern Dark
- Appearance > Options > Hide menu bar icon を on にする
- Appearance > Options > Show Alfred on > mouse screen にする
- Advanced > Force Keyboard を ABC にする
- クリップボード履歴 ~/Library/Application Support/Alfred/Databases/clipboard.alfdbにあるので、Macのファイル共有で新しいPCに移して再起動

### VSCode

- GitHubアカウントでログインして設定を同期させる

### AWS

- aws configure コマンドで認証情報の設定を行う

### HyperSwitch

- Run HyperSwitch in the background を チェックする

### RunCat

- 一般 > ログイン時に自動でRunCatを起動 を チェックする
- システム情報 > CPU負荷 メニューバーに表示 を チェックする
