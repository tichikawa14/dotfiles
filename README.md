[![Installation and Setup Check](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml)
[![Shellcheck](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml)

# dotfiles for Apple Silicon MacBook

macOS用の個人設定です。[mise](https://mise.jdx.dev/)でパッケージ、GUIアプリ、dotfiles、macOS設定を管理します。

## 初回セットアップ

```sh
xcode-select --install
git clone https://github.com/tichikawa14/dotfiles.git ~/dotfiles
~/dotfiles/scripts/initialize.sh
```

Homebrewとmiseを導入し、`mise bootstrap`で環境を構築します。途中でApp Storeへのログインやsudoパスワードが必要になる場合があります。

## 日常運用

dotfilesは`~/dotfiles`へのsymlinkなので、普段どおりホーム側を編集してコミットします。

```sh
vim ~/.zshrc
git -C ~/dotfiles diff
git -C ~/dotfiles add .
git -C ~/dotfiles commit -m "zsh設定を更新"
git -C ~/dotfiles push
```

パッケージやmacOS設定を変更したときは、planを確認してから再適用します。

```sh
mise -C ~/dotfiles bootstrap plan
mise -C ~/dotfiles bootstrap
mise -C ~/dotfiles bootstrap status
```

Node.jsやRubyなどの開発ツールは、このリポジトリではなく各プロジェクトでバージョンを指定します。

## パッケージの変更

CLIツールとApp Storeアプリはmiseで追加します。

```sh
mise -C ~/dotfiles bootstrap packages use brew:jq
mise -C ~/dotfiles bootstrap packages use mas:497799835
```

Homebrew caskは`scripts/install-casks.sh`を編集して適用します。

```sh
vim ~/dotfiles/scripts/install-casks.sh
mise -C ~/dotfiles run casks
```

削除時は宣言を消すだけではアンインストールされません。`brew uninstall`、`brew uninstall --cask`、`mas uninstall`で対象を個別に削除します。

## その他手動で行う設定

### Xcode

- Xcodeのライセンスに同意する

### `.zsh_history`移行

- Macのファイル共有で新しいPCに移す

### システム環境設定

- システム環境設定 > ディスプレイ > 解像度を適宜変更
- システム環境設定 > 通知 > 適宜onにする
- システム環境設定 > サウンド > 通知音変更
- システム環境設定 > コントロールセンター > バッテリー > 割合（%）を表示onにする
- システム環境設定 > デスクトップとDock > デフォルトのWebブラウザ > Arcに設定
- システム環境設定 > 複数のディスプレイを配置
- システム環境設定 > 壁紙・スクリーンセーバー > 適宜変更
- システム環境設定 > ロック画面 > ディスプレイオフを適宜設定
- システム環境設定 > ユーザーとグループ > ユーザーアイコン編集
- システム環境設定 > キーボード > ショートカット > Spotlight検索を表示するショートカットをoffにする
- システム環境設定 > キーボード > ファンクションキー > 標準のファンクションキーとして使用をonにする
- システム環境設定 > キーボード > 修飾キー > Caps LockキーをCommandキーにする
- システム環境設定 > ソフトウェアアップデート > 自動アップデートをoffにする

### Finder

- よく使う項目にホームディレクトリなどを追加

### GitHub

- SSH秘密鍵・公開鍵を登録する
- `gh auth login`でログインする

### AWS

- `aws configure`で認証情報を設定する

### RunCat Neo

- ログイン時に自動でRunCat Neoを起動するように設定する
