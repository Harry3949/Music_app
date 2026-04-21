# Music_app - 音楽共有プラットフォーム

Music_appは、ユーザーが自分の好きな音楽を共有し、コメントを通じてコミュニケーションを図ることができる、Djangoベースのウェブアプリケーションです。

## 主な機能

- **ユーザー認証**: サインアップ、ログイン、パスワードリセット機能。
- **音楽投稿**: 画像と音声ファイルを含めた投稿。
- **カテゴリ管理**: 投稿をカテゴリごとに分類（実装中）。
- **コメントシステム**: 投稿に対するコメントの追加、編集、削除。
- **検索機能**: タイトルや内容からお気に入りの音楽を検索。
- **メディア管理**: 画像や音声データのセキュアな管理。

## 技術スタック

- **Backend**: Python 3.x / Django 3.2
- **Frontend**: HTML5 / CSS3 / JavaScript (Bootstrap 4/5)
- **Database**: SQLite3 (開発用) / PostgreSQL (推奨)
- **Environment Management**: python-dotenv

## セットアップ手順

1. **リポジトリをクローン**:
   ```bash
   git clone <repository-url>
   cd Music_app
   ```

2. **仮想環境の作成と起動**:
   ```bash
   python -m venv venv
   .\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **依存パッケージのインストール**:
   ```bash
   pip install -r requirements.txt
   ```

4. **環境変数の設定**:
   `.env` ファイルを作成し、以下の項目を設定してください。
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **データベースのマイグレーション**:
   ```bash
   python manage.py migrate
   ```

6. **サーバーの起動**:
   ```bash
   python manage.py runserver
   ```

## プロジェクトのこだわり

- **デザインの刷新**: ガラスモーフィズムを採用したモダンなダークテーマへの移行。
- **実用的な検索機能**: Qオブジェクトを使用したタイトル・本文の横断検索を実装。
- **セキュリティの強化**: `python-dotenv` による機密情報の外部管理。
- **テスト駆動**: 重要なビューとモデルに対する自動テストの導入。
- **品質管理**: 全ビューへのドキュメント追加とコードのクリーンアップ。
