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

- [ ] 旧Macの `~/.zsh_history` をMacのファイル共有で新Macのホームフォルダにコピーし、既存のファイルを置き換える

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
- [ ] カレンダー連携を設定する

### T3 Code

2026年10月9日の実設定。設定名や配置はバージョンにより変わるため、Settingsの検索も利用する。

- [ ] `mise bootstrap`でT3 CodeとHackGenを導入する（caskの`t3-code`はStable版。この端末ではNightlyを使用）
- [ ] Nightlyを使う場合はSettings → General → Update trackでNightlyへ切り替える
- [ ] Providersで利用するCodex・ClaudeのCLIと認証状態を確認する
- [ ] プロジェクトを追加する。別Macへ接続する場合はConnectionsからペアリングする
- [ ] `~/.t3/userdata/keybindings.json`がdotfilesへのsymlinkになっていることを確認する。既存ファイルと衝突する場合は退避してから`mise bootstrap`を再実行する
- [ ] 以下の手動設定を反映する。適用範囲を選べる設定はAll projects / All environmentsを選び、プロジェクト固有の上書きは必要に応じて確認する

キーバインドは自動管理するが、`client-settings.json`と`settings.json`、履歴・接続・認証情報はGit管理しない。

#### General

| 項目 | 設定値 |
| --- | --- |
| New threads → Model | Claude Opus 5.5（利用可能な環境で選択） |
| New threads → Permissions | Auto（`defaultRuntimeMode: auto`） |
| Project grouping | ON（同じリポジトリをまとめる） |
| Working section (beta) | OFF |
| Thread notifications | 通知＋サウンド（macOS側でも通知を許可する） |
| In-app notifications | ON |
| Time format | System default（保存値：`locale`） |
| Hide whitespace changes | OFF |
| Default diff file state | Expanded（ファイルを展開して開く） |
| Diff layout | Side by side（保存値：`split`） |
| Proactive panels | ON |
| Show skills in slash menu | ON |
| Rich text composer | ON |
| Collapse composer on scroll | ON |
| Send shortcut | ⌘Enter（保存値：`mod-enter`） |
| Follow-up behavior | Queue |
| Unpin confirmation / Archive confirmation | OFF / OFF |
| Delete confirmation | ON |
| Quit shortcut | Hold |

#### Appearance

| 項目 | フォント | サイズ |
| --- | --- | --- |
| Interface font | System default（未指定） | 17px |
| Prompt font | Interface fontを継承（未指定） | 15px |
| Code font | HackGen35 | 12px |
| Terminal font | 未指定 | 12px |

- [ ] Font smoothingをON、Chat widthをComfortable、Word wrapをONにする
- [ ] Panel animationsを0msにする

Interface font sizeは本文の実表示サイズとは異なり、現在の実装では本文は87.5%で表示される（17px設定で約14.9px）。

#### SnapShots

- [ ] SnapShotsとアクセシビリティ情報の添付をONにする
- [ ] ショートカットを左右両方のShiftキーにする
- [ ] サウンド・フラッシュ・アニメーションをONにする
- [ ] 要求された画面収録・アクセシビリティ権限をmacOSのシステム設定で許可する

#### 操作と現在の制約

- `⌘K` → `pr` → Open pull requestsでPR一覧を開く。PR表示中の`⌘⇧C`でURLをコピーしてブラウザへ貼り付ける
- `⌘⌥S`で右パネルを開閉、`⌘⇧S`で最大化、`⌘⇧T`で閉じたタブを開き直す
- 右パネルの幅・開閉状態・選択タブはスレッド別。全スレッドで共通化する設定は未対応
- Proactive panelsをOFFにするとPR・差分の自動表示を抑えられるが、幅は共通化されない。上表は現在のON設定を記録したもの
- In-app notificationsをOFFにすると他スレッドの完了・承認待ちなどの通知を抑えられるが、エラーや接続警告までは無効化されない

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
