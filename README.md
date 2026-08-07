[![Installation and Setup Check](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml)
[![Shellcheck](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml)

# dotfiles for Apple Silicon MacBook

macOS用dotfilesです。[mise](https://mise.jdx.dev/)でシステムパッケージ、GUIアプリ、dotfiles、macOS設定を管理します。開発ツールのバージョンは各プロジェクトのmise設定で管理します。

- Shell: Z shell
- Terminal: [Ghostty](https://ghostty.org/) with [Starship](https://starship.rs/)
- Editor: [Cursor](https://cursor.com/)

## 初回セットアップ

```sh
xcode-select --install
git clone https://github.com/tichikawa14/dotfiles.git ~/dotfiles
~/dotfiles/scripts/initialize.sh
```

`scripts/initialize.sh`は次の処理を行います。

- Homebrewとmiseの導入
- `mise.toml`の信頼済み設定への登録
- `mise bootstrap`による環境構築

`mise bootstrap`では、パッケージ、dotfiles、macOS設定、ログインシェルを順番に適用します。App Storeへのログインやsudoパスワードが必要になる場合があります。

すでにHomebrew、mise、リポジトリがある場合は、次のコマンドで再適用できます。

```sh
mise -C ~/dotfiles bootstrap
```

## 日常運用

dotfilesは`~/dotfiles`内のファイルへのsymlinkです。ホーム側を編集すると、リポジトリのファイルが直接更新されます。

```sh
vim ~/.zshrc
git -C ~/dotfiles diff
git -C ~/dotfiles add .
git -C ~/dotfiles commit -m "zsh設定を更新"
```

`mise.toml`で管理するアプリ、dotfile、macOS設定を変更した場合は、適用前にplanを確認します。

```sh
mise -C ~/dotfiles bootstrap plan
mise -C ~/dotfiles bootstrap
```

影響範囲を限定して確認・適用する場合は、対象別のコマンドを使います。

```sh
# パッケージ
mise -C ~/dotfiles bootstrap packages apply --dry-run
mise -C ~/dotfiles bootstrap packages apply

# dotfiles
mise -C ~/dotfiles bootstrap dotfiles apply --dry-run
mise -C ~/dotfiles bootstrap dotfiles apply

# macOS設定
mise -C ~/dotfiles bootstrap macos defaults apply --dry-run
mise -C ~/dotfiles bootstrap macos defaults apply
```

開発ツールは各プロジェクトの`mise.toml`やバージョンファイルに宣言し、プロジェクト内で`mise install`を実行します。グローバル設定はNode.jsとRubyのバージョンファイル認識だけを有効にし、共通バージョンは指定しません。

現在の状態は次のコマンドで確認できます。

```sh
mise -C ~/dotfiles bootstrap status
mise doctor
```

## アプリとCLIツールの管理

パッケージを追加するときは、種別に応じたmanagerを指定します。コマンドは`mise.toml`の更新とインストールをまとめて行います。

```sh
# Homebrew formula
mise -C ~/dotfiles bootstrap packages use brew:jq

# Mac App Store
mise -C ~/dotfiles bootstrap packages use mas:497799835
```

GUIアプリは、Homebrewが導入した既存caskをmiseが引き継げないため、`scripts/install-casks.sh`の`casks`へ追加します。`mise bootstrap`の最後にHomebrew経由で不足分だけを導入します。

```sh
vim ~/dotfiles/scripts/install-casks.sh
mise -C ~/dotfiles run casks
```

今後のMacにインストールしないパッケージは、`mise.toml`から該当行を削除します。現在のMacからも削除する場合は、対象を確認して個別にアンインストールします。

```sh
brew uninstall jq
brew uninstall --cask ghostty
mas uninstall 497799835
```

Homebrew formulaに限り、宣言されていないパッケージをまとめて確認・削除できます。手動で導入したformulaも対象になるため、必ずdry-runを先に実行します。

```sh
mise -C ~/dotfiles bootstrap packages prune --manager brew --dry-run
mise -C ~/dotfiles bootstrap packages prune --manager brew
```

パッケージとGUIアプリを更新する場合は、次のコマンドを使います。

```sh
mise -C ~/dotfiles bootstrap packages upgrade --dry-run
mise -C ~/dotfiles bootstrap packages upgrade
brew upgrade --cask
```

## Homebrewへ委譲する設定

Homebrew所有の既存caskはmiseが引き継げないため、bootstrapタスクからHomebrewへ委譲します。

- Homebrew cask
- `ngrok` caskのpostflight処理

これらの処理は`mise bootstrap`の最後に`scripts/install-casks.sh`を通して実行されます。

## 意図的に自動管理しないmacOS設定

旧`mac/setup.sh`にあった次の設定は管理対象外です。

- Dockから全アプリを削除する設定
- スクリーンショットの保存先
- DNSサーバー
- ファイアウォール
- ホスト固有のタップクリック設定（`defaults -currentHost`）

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
