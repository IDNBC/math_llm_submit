# LMstudioで起動した llama-3-8b-instruct-32k-v0.1 のサーバでモデルに計算機を使わせるコード

import os
import requests

# -------------------------------
# 1. LM StudioのOpenAI互換API設定
# -------------------------------
API_URL = "http://127.0.0.1:1234/v1/completions"  # LM StudioでOpenAI互換APIを有効にした場合
os.environ["OPENAI_API_KEY"] = "dummy"

# -------------------------------
# 2. 安全な四則演算関数
# -------------------------------
def safe_calculate(expression: str) -> str:
    try:
        # __builtins__をNoneにしてevalを安全化
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Error: {e}"

# -------------------------------
# 3. LM Studio API経由でテキスト生成
# -------------------------------
def llama_generate(prompt: str) -> str:
    payload = {
        "model": "llama-3-8b-instruct-32k-v0.1",
        "prompt": prompt,
        "max_tokens": 256
    }
    headers = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # LM Studio の OpenAI互換APIだと choices[0].text に結果が返る
        return data["choices"][0]["text"].strip()
    else:
        return f"Error {response.status_code}: {response.text}"

# -------------------------------
# 4. 対話ループ
# -------------------------------
print("LM Studio Llama Agent 起動。'exit' で終了")
while True:
    query = input("質問: ")
    if query.lower() == "exit":
        break

    # 数式なら計算する
    if any(op in query for op in ["+", "-", "*", "/"]):
        result = safe_calculate(query)
        print("計算結果:", result)
    else:
        # それ以外はLlamaに質問
        result = llama_generate(query)
        print("回答:", result)
