[![Installation and Setup Check](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/setup.yaml)
[![Shellcheck](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/tichikawa14/dotfiles/actions/workflows/shellcheck.yaml)

# dotfiles(for AppleSilicon MacBook)

This dotfiles for macOS are managed with [Homebrew Bundle](https://github.com/Homebrew/homebrew-bundle), [GNU stow](https://www.gnu.org/software/stow/) and [asdf](https://asdf-vm.com/).

- Shell: Z shell
- Terminal: [Alacritty](https://alacritty.org/) with [Starship](https://starship.rs/)
- Editor: [RubyMine](https://www.jetbrains.com/ruby/)

## セットアップ

```
$ xcode-select --install
$ git clone https://github.com/tichikawa14/dotfiles.git
$ cd ~/dotfiles
$ make all
```

## その他手動で行う設定(TODO)

### システム環境設定

- デスクトップ画像・ユーザーアイコン編集
- システム環境設定 > キーボード > ショートカット > Spotlight > Spotlight 検索を表示のショートカットを off にする
- システム環境設定 > キーホード > ショートカット > Mission Control > デスクトップ n へ切り替えを on にする
- システム環境設定 > キーホード > ショートカット > キーボード > 次のウィンドウを捜査対象にするの割当を option + tab にする
- システム環境設定 > セキュリティとプライバシー > 一般 > スリープとスクリーンセーバーの解除にパスワードを要求を、開始後すぐにする
- システム環境設定 > セキュリティとプライバシー > 一般 > Apple Watch を使ってアプリケーションとこの Mac のロックを解除を on にする
- システム環境設定 > ソフトウェアアップデート > Mac を自動的に最新の状態に保つを on にする
- システム環境設定 > Bluetooth でマウスとキーボードとイヤホンを登録する
- システム環境設定 > バッテリー > バッテリー > ディスプレイをオフにするを 15 分に設定
- システム環境設定 > バッテリー > 電源アダプタ > ディスプレイをオフにするを 15 分に設定
- システム環境設定 > ディスプレイ > メインディスプレイを適宜変更

### Finder

- よく使う項目にホームディレクトリを追加

### Alfred

- General > Alfred Hotkey を cmd + space に変更
- General > Where are you を Japan に設定
- Features > Web Bookmarks > Google Chrome Bookmarks を on にする
- Appearance > Alfred Modern Dark
- Appearance > Options > Hide menu bar icon を on にする
- Advanced > Force Keyboard を Alphanumeric(Google)に変更

### GitHub

- `gh auth login`コマンドでログインする

### VSCode

- GitHub アカウントで認可
- go のツールのインストールを求められたら、Install All でインストールする

### AWS

- aws configure コマンドで認証情報の設定を行う
