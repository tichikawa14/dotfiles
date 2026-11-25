# Orca の設定一覧

Orca の設定は `~/Library/Application Support/orca/profiles/local-default/profile-state.db`（SQLite）に保存される。ファイルとして書き出したり読み込んだりする機能はないので、新しいマシンではこの一覧を見ながら設定画面（⌘,）で入れ直す。

DB を直接書き換えると壊れるおそれがあるので、agent に頼む場合も設定画面を操作させる。ショートカットだけは `keybindings.json` を `~/.orca/keybindings.json` にリンクして管理している。

2026-11-25 に Orca 1.4.274 の値を読み出して作成した。かっこ内は DB 上のキー名で、設定画面で検索するときの手がかりにする。

## Appearance

- テーマ: Light（`theme`）
- UI フォント: Geist（`appFontFamily`）
- 使用量の表示: % used（`usagePercentageDisplay`）
- ステータスバーの使用量: 全部の枠を表示する（`statusBarUsageMode: verbose`）。ステータスバーの使用量の表示から Detailed を選ぶ
- 新しいワークツリーカードの見た目とアプリレール: 有効（実験的機能 `experimentalNewWorktreeCardStyle`、`experimentalAppRail`）

## Editor と Diff

- 自動保存: オン、遅延 1000 ms（`editorAutoSave`、`editorAutoSaveDelayMs`）
- Diff の表示: 左右に並べる（`diffDefaultView: side-by-side`）
- Diff の折り返し: オン（`diffWordWrap`）
- Diff で空白の差分を表示: オン（`diffShowWhitespace`）
- ソース管理の並び順: 変更を先に表示（`sourceControlGroupOrder: changes-first`）

## Terminal

- フォント: SF Mono、13、太さ 500（`terminalFontFamily`、`terminalFontSize`、`terminalFontWeight`）
- 左右の余白: 10（`terminalPaddingX`）
- テーマ: Ghostty の Galaxy を取り込んで使う（`terminalThemeDark: custom:ghostty:galaxy`）。Ghostty の設定（`dot_config/ghostty/config`）を先に入れておき、Terminal の Ghostty import で取り込む
- ライトモード用に別テーマを使う: オフ（`terminalUseSeparateLightTheme`）
- Claude Code のテーマを同期: オン（`claudeCodeThemeSync`）
- 入力中はマウスカーソルを隠す: オン（`terminalMouseHideWhileTyping`）
- 右クリックで貼り付け: オフ（`terminalRightClickToPaste`）
- 非アクティブなペインの不透明度: 0.7（`terminalInactivePaneOpacity`）
- スクロールバック: 5000 行（`terminalScrollbackRows`）
- Quick Commands: なし（既定のコマンドも消している）

## Agents と Chat

- エージェントを開く形式: Chat（`agentDefaultSurface: chat`）
- 既定のエージェント: Claude（`defaultTuiAgent`）
- 権限の既定値: Auto（`agentPermissionDefault`、Chat の `nativeChatPermissionMode`）
- Chat の幅: 広い（`nativeChatAppearance.width: wide`）
- 何もしていない Chat を止めるまで: 30 分（`nativeChatIdleStopMinutes`）
- 無効にしているエージェント: なし（`disabledTuiAgents`）

## General

- Open in メニュー: Zed（`openInApplications`）

## Notifications

- 通知: オン。完了したとき、入力待ちのとき、ターミナルのベルで通知する
- Orca を見ているときは通知しない: オン（`suppressWhenFocused`）
- 通知音: blop、音量 100
- 非表示のワークスペースは通知しない（`notifyHiddenWorkspaces: false`）
