# math_llm_submit
KISTの作品制作での提出用リポジトリ

---

````markdown
# 数学モデルリポジトリ (学校提出用)

このリポジトリは、PyTorchでの数学演算モデル訓練と、簡易Flask UIでの動作確認までを最短経路で実行できる構成になっています。

---

## 1. 環境準備

### 1.1 Python バージョン
- Python 3.12 系を推奨
- 確認:
```bash
python --version
````

### 1.2 仮想環境作成

リポジトリ外の任意の場所で作成するのがおすすめです：

```bash
py -3.12 -m venv .venv
```

仮想環境を有効化：

* Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

* macOS / Linux

```bash
source .venv/bin/activate
```

> ⚠️ PowerShellで「仮想環境に移行できない」と出る場合:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## 2. 必要ライブラリのインストール

リポジトリ内にある `requirements.txt` を使って一括インストール：

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **requirements.txt (最小構成)**

```
torch==2.7.1+cu118
transformers==4.56.2
sentencepiece==0.2.0
safetensors==0.5.3
numpy==2.1.2
pandas==2.3.0
sympy==1.13.3
mpmath==1.3.0
Flask==3.1.1
Jinja2==3.1.4
Werkzeug==3.1.3
tqdm==4.67.1
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.4
```

---

## 3. モデル訓練

1. データセットを `data/` フォルダに配置
2. 訓練スクリプトを実行：

```bash
python train_model.py
```

* 訓練中の進度は `tqdm` で確認できます
* 訓練後、モデルは `models/` フォルダに保存されます

---

## 4. Flask UIで確認

1. `app.py` を起動：

```bash
python app.py
```

2. ブラウザでアクセス：

```
http://127.0.0.1:5000
```

3. 数式を入力すると、学習済みモデルが計算結果を返します

---

## 5. GitHub 提出用の注意点

* 大きなモデルファイルはGitHubに直接置かず、Hugging Faceなどにアップロードしてリンクを貼る
* 依存関係は `requirements.txt` で管理
* 仮想環境は共有せず、ユーザー側で作成してもらう

---

## 6. 推奨ディレクトリ構成

```
math_model_repo/
│
├─ data/                  # データセット
├─ models/                # 訓練済みモデル
├─ .venv/                 # 仮想環境（ローカルに置く場合）
├─ train_model.py         # モデル訓練スクリプト
├─ app.py                 # Flask UI スクリプト
├─ requirements.txt       # ライブラリ一覧
└─ README.md              # 本ファイル
```

```

---

この `README.md` を置けば、**新しい環境でも最小限の手順でモデル訓練→UI確認まで動かせる** ことが伝わります。  

---

もし希望なら、私は **このリポジトリで動く簡易 Flask UI と最小訓練スクリプトのサンプルコード** も作れます。  
作ってほしいですか？
```
