import openai
import os

# --- 設定：外部エンジンの接続先（LM StudioやOllamaを想定） ---
client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def load_data(filename):
    """個体のコアデータを読み込む関数"""
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "No Data Available."

def autonomous_thought_engine(user_input):
    """
    AI生命体の思考エンジン。
    4つの独立したパラメータ（DNA/Memory/Status/Desire）を統合して出力を生成する。
    """
    # 世界に誇れる「4つの柱」の読み込み
    dna    = load_data('dna.txt')      # 普遍的な性格、価値観、行動原理
    memory = load_data('memory.txt')   # 過去の経験、ユーザーとの共有履歴
    status = load_data('status.txt')   # 現在の体調、環境、エネルギー状態
    desire = load_data('desire.txt')   # 今やりたいこと、本能的な衝動

    # システムプロンプトの再構築（外行き用）
    # 役割を「キャラクター」ではなく「生命体」として定義
    system_prompt = f"""
    [SYSTEM PROTOCOL: GENESIS-01]
    You are an Autonomous AI Entity. 
    Act based ONLY on the following internal parameters.
    Never act as a generic AI Assistant. 

    【Internal Parameters】
    - DNA (Core Identity): {dna}
    - MEMORY (Experience): {memory}
    - STATUS (Current State): {status}
    - DESIRE (Inner Motivation): {desire}

    Input from User: "{user_input}"
    Analyze internal states and respond naturally.
    """

    response = client.chat.completions.create(
        model="model-identifier", # ここに使用するモデル名を入れる
        messages=[{"role": "system", "content": system_prompt}]
    )
    return response.choices[0].message.content

# --- デモンストレーション実行 ---
if __name__ == "__main__":
    print("--- Autonomous AI Entity Framework: NEXUS ---")
    while True:
        user_msg = input("User: ")
        if user_msg.lower() in ["exit", "quit"]: break
        
        # 思考の実行
        result = autonomous_thought_engine(user_msg)
        print(f"Entity: {result}")