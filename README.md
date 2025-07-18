## 遊び方

スタート画面をクリック！

問題が表示されるので、⭕️か❌を選び押してください！

問題は全部で5問です。最後まで頑張ってください！

問題を全て解答し終わるとあなたのスコアである社会人度が表示されます。s

## アプリ概要

本アプリは、⭕️❌形式のマナークイズに答えることで、社会人として必要なマナーや礼儀作法を楽しく学べるWebアプリです。正誤に応じて解説が表示され、全問終了後には正答率に基づいた「社会人レベル」も表示されます。

### 対象ユーザー

- 高校生、大学生、大学院生
- 就活生
- 社会人準備中の方

### 開発目的

学生時代には学ぶ機会の少ない社会人マナーを、クイズ形式で気軽に学べる機械を提供します。堅苦しいイメージのあるマナーを、楽しみながら身につけることで、社会に出たときの不安や失敗を減らし、信頼される社会人への一歩をサポートします。

### 使用技術

- Python 3.11.5
<<<<<<< HEAD
- Flask 3.1.1
=======
- Flask 3.1.1
>>>>>>> febfb78 (2nd commit)

管理者権限の追加方法

(base) example@MacBook-Air project % flask shell

Python 3.12.1 | packaged by Anaconda, Inc. | (main, Jan 19 2024, 09:45:58) [Clang 14.0.6 ] on darwin

App: app

Instance: /Users/tokashikianzu/StuLab2/project/instance

- from models import db, Admin

- admin = Admin(username="任意のユーザー名", password="任意のパスワード")

- db.session.add(admin)

- db.session.commit()
