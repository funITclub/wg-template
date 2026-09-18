# WG テンプレート

fun IT club の WG が作るアプリのひな形（Django）。WG のリポジトリはこのテンプレートから作る。

開発環境（VS Code ＋ Dev Container / GitHub Codespaces）は homepage と共通で、手順は
[開発環境と手順](https://github.com/funITclub/homepage/blob/main/docs/development.md) にある。
このリポジトリを開いてコンテナができたら、`F5` でサイトが起動する。

> WG のリポジトリを作ったら、この README の先頭を「WG の名前・作っているもの・メンバー」に
> 書き換える。下の「開発の流れ」以降は残しておく。

## 開発の流れ

WG のリポジトリは複数人で触るので、**`main` に直接 push しない**。ブランチを切って
プルリクエスト（PR）を出し、テストが通って WG の誰かが確認してからマージする。

1. **最新にする**：VS Code の左下のブランチ名が `main` になっていることを確かめ、
   「ソース管理」の「…」→「プル」。
2. **ブランチを切る**：左下のブランチ名 →「新しいブランチの作成」。名前は
   `やること-短く`（例：`add-login-page`、`fix-date-format`）。
3. **作ってコミットする**：こまめにコミットしてよい。メッセージは日本語で、何をなぜ変えたか。
4. **push する**：「ブランチの発行」を押す。
5. **PR を出す**：GitHub のリポジトリを開くと「Compare & pull request」が出るので押す。
   何を変えたか・どう確かめたかを書く。
6. **テストを待つ**：PR の下で「Test」が緑になるのを待つ。赤なら直して同じブランチに push する。
7. **確認してもらう**：WG の誰かに見てもらい、「Approve」をもらう。
8. **マージする**：「Squash and merge」。終わったらブランチは消してよい。
9. **手元を main に戻す**：左下で `main` に切り替えて、プルする。

テストは手元でも流せる（push する前に流しておくと早い）。

```bash
python manage.py test
```

## 構成

```
config/                設定（共通 settings_common / 本番 settings / 開発 settings_dev）
core/                  最初のアプリ。トップページとテストだけ入っている
.devcontainer/         開発環境（Dev Container / Codespaces）の定義
.vscode/               VS Code の共通設定（F5 の起動構成・タスク）
.github/workflows/     PR と main への push でテストを流す
```

アプリを足すときは `python manage.py startapp <名前>` で作り、
`config/settings_common.py` の `INSTALLED_APPS` に足す。

設定は homepage と同じく3ファイルに分けてあり、**既定は本番**（`config.settings`）。
Dev Container の中と CI では `DJANGO_SETTINGS_MODULE=config.settings_dev` にしてあるので、
`--settings` を付けなくてよい。

パスワードや API キーはコードに書かない。手元では `.env`、Codespaces ではシークレットに置く
（[開発環境と手順](https://github.com/funITclub/homepage/blob/main/docs/development.md) の「秘密情報の扱い」）。

## 公開

公開（デプロイ）の仕組みは準備中。公開できたら、homepage の編集画面（`/edit/`）の
「WG紹介」に URL を登録すると、公開サイトの WG 一覧からリンクされる。

## WG のリポジトリを作る（運営向け）

1. このリポジトリの「**Use this template**」→「**Create a new repository**」。
   - Owner：`funITclub`
   - 名前：`wg-<WG の名前>`（英小文字とハイフン。例：`wg-countdown`）
   - Public
2. **main を守るルール**を作る。リポジトリの「Settings → Rules → Rulesets →
   New ruleset → New branch ruleset」。
   - 名前：`main`、Enforcement status：Active
   - Target branches：「Add target → Include default branch」
   - 「Restrict deletions」と「Block force pushes」をオン
   - 「Require a pull request before merging」をオン、Required approvals は `1`
     （自分の PR は自分で承認できないので、メンバーが1人の WG では `0` にする）
   - 「Require status checks to pass」をオンにし、`test` を追加
     （一度も CI が走っていないと候補に出ないので、先に PR を1つ出すか、Actions から流す）
3. **メンバーに書き込み権限を付ける**。「Settings → Collaborators and teams」で、
   WG のメンバー（または WG の team）に **Write** を付ける。
4. README の先頭を WG 用に書き換える（最初の PR にするとルールの確認にもなる）。

WG のメンバーが卒業・退部したら、3 の権限を外す。

テンプレートを直しても、作成済みの WG リポジトリには反映されない。開発環境の標準
（`.devcontainer/`・`.vscode/`・`.gitattributes`）を変えたときは、homepage にも同じ変更を
入れ、必要なら各 WG に知らせる。
