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

最初はパスを通す必要あり([scripts/initialize.sh](https://github.com/tichikawa14/dotfiles/commit/ed5e63dca1dccce81bb36dc9ec833d39ac21df95#diff-7cc6d1956fc288604f7ac8a34821a403547cc008d2af517ca7c1688ed70e5abcR26-R29)では対応できず...)
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
<img width="1376" alt="スクリーンショット 2022-11-05 23 40 15" src="https://user-images.githubusercontent.com/42080487/200125346-7b4b230f-ea79-4914-abed-921b05d39a6c.png">


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
- workflow から各アプリ用のhotkeyを追加
![スクリーンショット 2022-11-06 15 47 40](https://user-images.githubusercontent.com/42080487/200158100-154c8f1a-e74c-4e14-af20-ec3041463585.png)

### VSCode

- GitHubアカウントでログインして設定を同期させる

### AWS

- aws configure コマンドで認証情報の設定を行う

### HyperSwitch

- Run HyperSwitch in the background を チェックする

### RunCat

- 一般 > ログイン時に自動でRunCatを起動 を チェックする
- システム情報 > CPU負荷 メニューバーに表示 を チェックする
