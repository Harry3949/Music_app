# Music_app 起動・運用マニュアル

このドキュメントは、本アプリケーションをローカル環境で起動し、正常に動作させるための手順をまとめたものです。

---

## 1. 動作環境
- **OS**: Windows / macOS / Linux
- **Python**: 3.12 以上
- **Framework**: Django 6.0 以上

---

## 2. セットアップ手順

### ① リポジトリをクローンする
```bash
git clone https://github.com/（あなたのGitHubユーザー名）/Music_app.git
cd Music_app
```

### ② 仮想環境の構築
クローンしたフォルダ（`Music_app/`）で以下を実行します。

**Windowsの場合:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linuxの場合:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### ③ 依存ライブラリのインストール
```bash
cd musicproject
pip install -r requirements.txt
```
> ※ここで `musicproject/` フォルダに移動します。以降の操作はすべてこのフォルダ内で行います。

### ④ 環境変数の設定
`musicproject/` フォルダ内（`manage.py` と同じ場所）に `.env` ファイルを新規作成し、以下の内容を記述してください。

```env
SECRET_KEY=django-insecure-任意の長い文字列
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# メール送信設定（お問い合わせ機能用）
EMAIL_HOST_USER=あなたのGmailアドレス
EMAIL_HOST_PASSWORD=Googleで発行した16桁のアプリパスワード
```
> ※メール送信を機能させるには、Googleアカウントの2段階認証を有効にし「アプリパスワード」を発行する必要があります。

### ⑤ データベースの準備
```bash
python manage.py makemigrations
python manage.py migrate
```

### ⑥ 管理者ユーザーの作成（任意）
管理画面（`/admin`）を使いたい場合に実行してください。
```bash
python manage.py createsuperuser
```

---

## 3. アプリケーションの起動

```bash
python manage.py runserver
```

起動後、ブラウザで [http://127.0.0.1:8000/](http://127.0.0.1:8000/) にアクセスしてください。

---

## 4. 動作確認ポイント
- **トップページ**: 音楽投稿のカードが並び、検索バーで曲の絞り込みができるか。
- **ログイン/サインアップ**: ユーザー登録とログインが正常に行えるか。
- **投稿機能**: 音楽ファイルと画像を1つずつ選択して投稿できるか。
- **いいね機能**: ハートマークを押した際に、リロードなしでカウントが増減するか。
- **マイページ**: 自分が投稿した曲だけが表示されているか。

---

## 5. フォルダ構成（参考）

```
Music_app/              ← ここで仮想環境を作成・起動する
├── musicproject/       ← ここで pip install、manage.py を実行する
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env            ← 自分で作成する（GitHubには含まれません）
│   ├── accounts/
│   ├── musicapp/
│   ├── musicproject/
│   └── static/
├── .gitignore
├── README.md
└── startup_guide.md    ← このファイル
```
