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

公開は、**homepage（funitclub.org）の中でこのアプリを動かす**かたちで行う。
置き場所は 2 つあり、公表できる形になったら移る（URL は変わらない）。

| | 置き場所 | URL | 直打ちしたとき |
|---|---|---|---|
| 作っている途中 | `wg/<名前>/` | `/<名前>/` | WG 一覧 `/wg/` へ送り返す |
| 公表したもの | `works/<名前>/` | 同じ | 成果物一覧 `/works/` へ送り返す |

フォルダー名は URL に出ない。**アプリのフォルダー名がそのまま URL** になる
（`protein` → `/protein/`）。homepage 側で URL を書き足す作業は要らない。

**リポジトリは分けたまま**で、ソースが homepage（公開リポジトリ）に入ることはない。
homepage のデプロイが、そのときだけこのリポジトリを読んで `wg/<名前>/` に置く。

```
funITclub/wg-<名前>（非公開）        ここで開発する
     ↓ デプロイのときだけ取り込まれる
App Service の wg/<名前>/            公開はここで動く。URL は /<名前>/
```

### 載せるときにやること（運営）

1. homepage の `wg-apps.yml` に足す（`repo` / `take` / `as`）。`take` には載せるアプリを並べる。
   活動ページは `{app: <名前>_activity, url: <名前>/activity}`、WG が作る Web アプリは `<名前>`
2. このリポジトリの Secrets に、起動用の2つを入れる
   （`HOMEPAGE_DEPLOY_APP_ID`・`HOMEPAGE_DEPLOY_PRIVATE_KEY`。手順は homepage の `deploy.txt`）
3. `/edit/` の「WG紹介」で、その WG のカードに登録する。登録先は 2 つある
   - **活動ページ**（`/<名前>/activity/`）：追加リンクの名前を「活動ページ」、URL を
     `https://funitclub.org/<名前>/activity/` にする
   - **Web アプリ**（`/<名前>/`）：「Webアプリの URL」に `https://funitclub.org/<名前>/` を入れる。
     アプリができるまでは空欄のまま

以後は、**このリポジトリの `main` に push するたびに自動で公開される**
（`.github/workflows/deploy.yml` が homepage のデプロイを起動する）。

### 作るときの決まり

- **`apps.py` を置かない**（テンプレートにも入れていない）。このリポジトリでは `<名前>`、
  本番では `wg.<名前>` と読み込まれる名前が変わるため。無ければ Django が自動で作り、
  呼び名（`label`）はどちらも `<名前>` になるのでマイグレーションが一致する
- **誰でも見せるページには `login_not_required` を付ける**。本番は既定で全ビューが
  ログイン必須（homepage の `LoginRequiredMiddleware`）。付け忘れると、手元では見えるのに
  公開したらログイン画面に飛ばされる。逆に、WG の中だけで使う画面には付けないでおけば、
  そのままログイン必須になる

  ```python
  from django.contrib.auth.decorators import login_not_required
  from django.utils.decorators import method_decorator

  @method_decorator(login_not_required, name='dispatch')   # クラスベースのとき
  class IndexView(generic.TemplateView):
      ...
  ```

- **`config/` と `manage.py` は本番に持ち込まれない**（homepage 側の設定で動く）。
  設定が要るものは、運営に言って homepage の `settings_common.py` に足してもらう
- 秘密情報は `.env` ではなく App Service の設定に入る。運営に渡す
- `requirements.txt` に足したものは、本番の分と合わせて入る。増やしすぎない。
  **Django などの版は homepage と同じにしておく**（テンプレートは合わせてある）。
  同じパッケージを両方が指定していたら本番の版が使われるので、違えておくと
  「手元では新しい版、本番では古い版」になって動きが変わる

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
7. **活動ページを入れる**（立ち上げたらすぐ。Web アプリより先に載せる）。WG の紹介・構想資料・
   チケット管理を見せる場所で、`/<WG>/activity/` に置く（`<WG>` は WG の名前。英小文字と数字。
   例：`countdown`）。
   - [funITclub/claude-plugins](https://github.com/funITclub/claude-plugins) の wg-activity スキル
     （`plugins/wg-activity/skills/wg-activity/SKILL.md`）で、このリポジトリに `<WG>_activity` を作る。
     ブランチを切って PR を出し、マージする
   - マージしてから、homepage の `wg-apps.yml` にこの WG を足す（順番を逆にすると、取り込む
     フォルダーが無くてデプロイが止まる）

     ```yaml
     - repo: funITclub/wg-<WG の名前>
       take:
         - {app: <WG>_activity, url: <WG>/activity}   # /<WG>/activity/ 活動ページ
       as: wg
     ```

   - このリポジトリの Secrets に起動用の2つを入れる（上の「公開」の「載せるときにやること」の 2）
   - `/edit/` の「WG紹介」で、追加リンクの名前を「活動ページ」、URL を
     `https://funitclub.org/<WG>/activity/` にする。「Webアプリの URL」は空欄のまま
   - 活動ページは全画面が公開で、だれでもチケットを作成・編集・削除できる（WG のメンバーに
     ログインのアカウントを配っていないため）。WG に伝えておく

`/<WG>/` は、WG が作る Web アプリのために空けておく。活動ページとは別のアプリで、
Web アプリができたら homepage の `wg/` へ移して公開する（上の「公開」）。`wg-apps.yml` の
`take` に `<WG>` を足し、WG紹介の状態を「活動中」にして、「Webアプリの URL」に
`https://funitclub.org/<WG>/` を入れる（活動ページの追加リンクはそのまま残す）。
公表できる形になったら `works/` へ移し、成果物紹介にも登録する。

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
