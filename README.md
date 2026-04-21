# Music_app - 音楽共有プラットフォーム

あなたのサウンドを世界へ。Music_appは、アーティストが自信を持って楽曲を共有し、リスナーと繋がることができる、Djangoベースの音楽共有プラットフォームです。

## ✨ 特徴 (Features)

- **モダンなUI/UX**: ガラスモーフィズムを採用したスタイリッシュなダークテーマ。
- **インテリジェント検索**: タイトルや投稿内容から、お気に入りの曲を即座に発見可能。
- **インタラクティブな反応**: AJAX(Fetch API)を使用した、ページリロードなしのリアルタイム「いいね」機能。
- **安心のバリデーション**: 音楽・画像の同時投稿を必須化し、コンテンツの質を維持。
- **ユーザー認証**: セキュアなサインアップ、ログイン、マイページ機能を完備。

## 🛠 技術スタック (Tech Stack)

- **バックエンド**: Python 3.x / Django 3.2
- **フロントエンド**: HTML5 / CSS3（バニラCSSによるカスタムデザイン） / JavaScript
- **データベース**: SQLite3（開発環境）
- **環境管理**: python-dotenv

## 💎 プロジェクトのこだわり (Key Points)

- **実務レベルの品質管理**: ユニットテストを導入し、主要機能の動作を保証しています。
- **セキュリティの徹底**: `python-dotenv` による機密情報の外部管理を徹底。
- **快適な操作性**: 非同期通信を活用し、ユーザーの操作を妨げないシームレスな体験を追求しました。
- **美しいデザイン**: 各種フォームやボタンに至るまで、共通のデザイントークンに基づいた一貫性のあるUIを構築しました。

# Music_app 起動・運用マニュアル

このドキュメントは、本アプリケーションをローカル環境で起動し、正常に動作させるための手順をまとめたものです。

## 1. 動作環境
- **OS**: Windows / macOS / Linux
- **Python**: 3.8 以上
- **Framework**: Django 3.2 以上

## 2. セットアップ手順

### ① 仮想環境の構築
プロジェクトのルートディレクトリ（Music_app）で以下のコマンドを実行します。

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

### ② 依存ライブラリのインストール
```bash
pip install -r musicproject/requirements.txt
```

### ③ 環境変数の設定
`musicproject/` ディレクトリ内に `.env` ファイルがあることを確認してください。
ない場合は作成し、以下の内容を記述します。
```env
SECRET_KEY=django-insecure-xxxxx  # 任意の文字列
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### ④ データベースの準備
```bash
cd musicproject
python manage.py makemigrations
python manage.py migrate
```

### ⑤ 管理者ユーザーの作成（任意）
```bash
python manage.py createsuperuser
```

## 3. アプリケーションの起動
```bash
python manage.py runserver
```
起動後、ブラウザで [http://127.0.0.1:8000/](http://127.0.0.1:8000/) にアクセスしてください。

## 4. 動作確認ポイント
- **トップページ**: 音楽投稿のカードが並び、検索バーで曲の絞り込みができるか。
- **ログイン/サインアップ**: ユーザー登録とログインが正常に行えるか。
- **投稿機能**: 音楽ファイルと画像を1つずつ選択して投稿できるか。
- **いいね機能**: ハートマークを押した際に、リロードなしでカウントが増減するか。
- **マイページ**: 自分が投稿した曲だけが表示されているか。
