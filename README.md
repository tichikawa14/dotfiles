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

日常利用する開発ツールはグローバルmise設定で管理し、プロジェクト固有のバージョンが必要な場合は各プロジェクトで上書きします。

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

`mise bootstrap`では管理しないため、新しいMacのセットアップ時に以下を確認します。

### Xcode

- [ ] Xcodeのライセンスに同意する

### `.zsh_history`移行

- [ ] Macのファイル共有で新しいPCに移す

### システム環境設定

- [ ] システム設定 > ディスプレイ > 解像度を適宜変更する
- [ ] システム設定 > 通知 > 必要なアプリの通知をオンにする
- [ ] システム設定 > デスクトップとDock > デフォルトのWebブラウザをArcにする
- [ ] システム設定 > ディスプレイ > 複数のディスプレイを配置する
- [ ] システム設定 > 壁紙・スクリーンセーバーを適宜変更する
- [ ] システム設定 > ロック画面 > ディスプレイをオフにする時間を適宜変更する
- [ ] システム設定 > ユーザーとグループ > ユーザーアイコンを変更する
- [ ] システム設定 > キーボード > キーボードショートカット > Spotlight > Spotlight検索を表示をオフにする
- [ ] システム設定 > 一般 > ソフトウェアアップデート > 自動アップデートをオフにする
- [ ] `~/Downloads/スクリーンショット`を作成し、`Shift+Command+5` > オプション > 保存先に指定する

### Finder

- [ ] よく使う項目にホームディレクトリなどを追加する

### CleanShot X

- [ ] Capture Areaを`Shift+Command+4`にする
- [ ] Capture Fullscreenを`Shift+Command+5`にする
- [ ] All-In-Oneを`Control+Shift+Command+4`にする
- [ ] Scrolling Captureを`Shift+Command+2`にする
- [ ] Screen Recordingを`Shift+Command+3`にする
- [ ] Text Recognitionを`Control+Shift+Command+T`にする

### Raycast

- [ ] Export Settings & Dataで`.rayconfig`をGit管理外の安全な場所へ書き出す
- [ ] 新しいMacでImport Settings & Dataから`.rayconfig`を読み込む

### DockDoor

- [ ] 除外アプリにLINEとSparkを追加する
- [ ] Window Switcherを現在のモニターとSpaceのウインドウだけ表示する設定にする
- [ ] メニューバーアイコンを非表示にする

### Nani

- [ ] 選択したテキストを翻訳するショートカットを`Option+Command+J`にする

### GitHub

- [ ] SSH秘密鍵・公開鍵を登録する
- [ ] `gh auth login`でログインする

### AWS

- [ ] `aws configure`で認証情報を設定する
