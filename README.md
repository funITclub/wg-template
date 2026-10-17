# WG テンプレート

fun IT club の WG が作るアプリのひな形（Django）。WG のリポジトリはこのテンプレートから作る。

開発環境（VS Code ＋ Docker Desktop の Dev Container）は homepage と共通で、手順は
[開発環境と手順](https://github.com/funITclub/homepage/blob/main/docs/development.md) にある。
このリポジトリを開いてコンテナができたら、`F5` でサイトが起動する。

> WG のリポジトリを作ったら、この README の先頭を「WG の名前・作っているもの・メンバー」に
> 書き換える。下の「開発の流れ」以降は残しておく。

## 開発の流れ

WG のリポジトリは複数人で触るので、**`main` に直接 push しない**。VS Code は `main` のままの
コミットを止めて新しいブランチを作らせ、`main` への push も送る前に止める（`.githooks/pre-push`）。
自分用の「ブランチ」で作業し、プルリクエスト（PR）を出して、テストが通って WG の誰かが
確認してから `main` にまとめる（マージ）。

開発環境の準備がまだなら、先に
[開発環境と手順](https://github.com/funITclub/homepage/blob/main/docs/development.md) を済ませる。

### VS Code でやること

1. **最新にする**
   - 左下にブランチ名が出ている。`main` になっていることを確かめる。
   - 左の「**ソース管理**」（枝分かれのアイコン）→ 上の「**…**」→「**プル**」。
2. **ブランチを作る**
   - 左下のブランチ名（`main`）を押す →「**+ 新しいブランチの作成...**」。
   - 名前を英小文字とハイフンで入れて Enter（例：`add-login-page`、`fix-date-format`）。
   - 左下が新しいブランチ名に変わる。
3. **作る**：コードを書き、`F5` で動きを確かめる。
4. **テストを流す**：ターミナルで `python manage.py test`。最後に `OK` と出れば通っている。
5. **コミットする**（変更を記録する）
   - 「ソース管理」を開くと、変えたファイルが並んでいる。
   - 上の入力欄に、何をなぜ変えたかを日本語で書く（例：`ログイン画面を追加する`）。
   - 「**コミット**」を押す。「ステージされている変更がなく…直接コミットしますか?」と
     出たら「**はい**」。
   - 区切りのいいところで何回コミットしてもよい。
6. **GitHub に送る**：「**Branch の発行**」を押す（2 回目からは「**変更の同期**」）。
   初回は GitHub へのサインインを求められるので、「許可」→ ブラウザで「Authorize」。

### GitHub でやること

7. **PR を出す**
   - ブラウザでリポジトリのページを開くと、上に黄色い帯で
     「**Compare & pull request**」が出ているので押す。
   - タイトルと、「何を変えたか」「どう確かめたか」を書いて「**Create pull request**」。
8. **テストを待つ**：PR の下のほうで「**Test**」が動く。緑のチェックになれば通過。
   赤い × なら「Details」でエラーを見て、VS Code で直して 5〜6 をもう一度（同じ PR に反映される）。
9. **見てもらう**：WG の誰かに PR の URL を送って、確認をお願いする。
10. **マージする**：「Approve」をもらったら「**Squash and merge**」→「**Confirm squash and merge**」。
    そのあと出る「**Delete branch**」も押してよい。

### 次の作業に移る

11. VS Code の左下のブランチ名を押して `main` を選ぶ → 1 の「プル」をする。
    2 からまた始める。

### PR を確認する人（レビュー）

- PR の「**Files changed**」タブで変更を見る。気になる行は行番号の横の「+」でコメントできる。
- 問題なければ右上の「**Review changes**」→「**Approve**」→「**Submit review**」。
- 直してほしいときは「**Request changes**」にして、何をどう直すかを書く。

## 構成

```
config/                設定（共通 settings_common / 本番 settings / 開発 settings_dev）
core/                  最初のアプリ。トップページとテストだけ入っている
.devcontainer/         開発環境（VS Code の Dev Container）の定義
.vscode/               VS Code の共通設定（F5 の起動構成・タスク）
.github/workflows/     PR と main への push でテストを流す
```

アプリを足すときは `python manage.py startapp <名前>` で作り、
`config/settings_common.py` の `INSTALLED_APPS` に足す。

**アプリの名前は `core` のままにせず、WG ごとに一意なものにする**（例: `protein`）。
公開のときに homepage へそのまま移すので、ほかの WG とぶつからない名前が要る。
あわせて次も同じ名前で揃えておくと、移すときに書き換えが出ない。

- `core/urls.py` の `app_name`
- テンプレートの置き場所（`<名前>/templates/<名前>/…`）
- モデルを持つなら `class Meta` の `db_table`（`funitclub_<名前>_…`）

設定は homepage と同じく3ファイルに分けてあり、**既定は本番**（`config.settings`）。
Dev Container の中と CI では `DJANGO_SETTINGS_MODULE=config.settings_dev` にしてあるので、
`--settings` を付けなくてよい。

パスワードや API キーはコードに書かない。`.env` に置く
（[開発環境と手順](https://github.com/funITclub/homepage/blob/main/docs/development.md) の「秘密情報の扱い」）。

## 公開

**このリポジトリは公開されない。** 公開するのは動いている Web ページだけで、ソースは
成果物に含めない（リポジトリは完成後も非公開のまま）。

公開は、**homepage のリポジトリにアプリを移して**行う。homepage には置き場所が2つある。

| | 置き場所 | 送り返す先 |
|---|---|---|
| 作っている途中 | `wg/<名前>/` | WG 一覧 `/wg/` |
| 公表したもの | `works/<名前>/` | 成果物一覧 `/works/` |

フォルダー名は URL に出ない。URL は homepage の `config/urls.py` で決める
（`wg.protein` → `/protein/`）。公表できる形になったら `wg/` から `works/` へ移し、
URL は変えない。

### 移すときにやること（運営）

1. アプリのフォルダー（`<名前>/`）だけを homepage の `wg/` へコピーする。
   **`config/` は持ち込まない**（homepage 側の設定を使う）。設定が要るなら
   `config/settings_common.py` に定数として足す
2. `apps.py` の `name` を `wg.<名前>` にし、`label = '<名前>'` を明示する
   （あとで `works/` へ移してもマイグレーションと DB の呼び名が変わらない）
3. homepage の `INSTALLED_APPS` と `config/urls.py` に足す
4. homepage の `GATE_BACK` に `'/<URL>/': 'home:wg_list'` を足す（公表時は `home:work_list`）
5. `/edit/` の「WG紹介」で、その WG の「Webアプリの URL」を入れる

### URL を直打ちしても開かない

公開したアプリは、**ホームページの一覧から辿ったときだけ開く**（homepage の
`config/gate.py`）。一覧のリンクに期限つきの通行証が付いていて、通行証も印も無い
アクセスは一覧へ送り返される。入口を funitclub に集めるためで、WG のアプリだけを
単体で使われないようにする狙い。

作るときは、次の2つに気をつける。

- アプリの中のリンクは**相対**で書く（`{% url %}` を使う）。一覧を経由しない
  入口を自分で作らない
- 外部サービスからの戻り先（メールのリンクなど）が要るときは、そこだけ通行証を
  免除する必要がある。**別の鍵（署名付きリンクなど）を自分で持たせたうえで**、
  運営に相談する

## WG のリポジトリを作る（運営向け）

1. **公開サイトに「準備中」で載せる**（WG が立ち上がったらすぐ）。homepage の編集画面
   （`/edit/`）の「WG紹介」→「WGを追加」。状態は「準備中」、「GitHub のチーム」は空欄のまま。
   アプリがまだでも載せる（ほかのメンバーが活動を知って参加できるように）。
2. このリポジトリの「**Use this template**」→「**Create a new repository**」。
   - Owner：`funITclub`
   - 名前：`wg-<WG の名前>`（英小文字とハイフン。例：`wg-countdown`）
   - **Private**（チームの人だけが見られる。org のメンバーの基本権限は「No permission」にしてある）
3. **main を守る仕組み**は、テンプレートに入っているので作業は要らない。
   - VS Code の設定（`main` のままコミットしようとすると新しいブランチを作らせる）と、
     `.githooks/pre-push`（`main` への push を手元で止める。作業部屋を作るときに自動で有効になる）
   - GitHub の Rulesets（`main` への push を GitHub 側で断る）は、無料プランでは**非公開の
     リポジトリに掛けられない**。有料の Team プラン（または教育機関向けの無料アップグレード）に
     したら、Settings → Rules → Rulesets で次を足す：対象は default branch、Restrict deletions・
     Block force pushes・Require a pull request（承認 1。メンバーが1人の WG は 0）・
     Require status checks（`test`）
4. **WG のチームを作って権限を付ける**。権限は人ごとではなく、チームに付ける。
   - チームを作る（org の「Teams」→「New team」）。名前はリポジトリと同じ `wg-<WG の名前>`、
     公開範囲は Visible。作った人（運営）は maintainer として自動で入る。そのままでよい
   - リポジトリの「Settings → Collaborators and teams」→「Add teams」で、そのチームに **Write** を付ける
   - **メンバーは入れない。** 本人が公開サイトの「WG に参加」から入る（下）
5. **サイトとつなぐ**。1 で載せた WG の「GitHub のチーム」に `wg-<WG の名前>` を入れて保存する。
   WG 一覧のカードに「WG に参加」が出る。
6. README の先頭を WG 用に書き換える（最初の PR にするとルールの確認にもなる）。

アプリができたら、homepage の `wg/` へ移して公開する（上の「公開」）。WG紹介の状態を
「活動中」にして、Webアプリの URL を入れる。公表できる形になったら `works/` へ移し、
成果物紹介にも登録する。

**メンバーの参加は自動。** WG 一覧の「WG に参加」から、本人が大学のアドレスを入れる →
Classroom のクラブのクラスにいれば確認のメールが届く → リンクから GitHub でログインすると、
このチームに入る（まだ org にいない人には org への招待が届く）。運営の作業はない。
仕組みは homepage の README の「WG への参加」。

WG を抜けた人は、チームの「Members」から外す。卒業・退部したら org から外し
（org の「People」→「Remove from organization」。すべてのチームからも外れる）、
Classroom のクラブのクラスからも外す（外さないと「WG に参加」を通れてしまう）。
WG が終わったら、リポジトリをアーカイブしてチームを消す。

テンプレートを直しても、作成済みの WG リポジトリには反映されない。開発環境の標準
（`.devcontainer/`・`.vscode/`・`.gitattributes`）を変えたときは、homepage にも同じ変更を
入れ、必要なら各 WG に知らせる。
