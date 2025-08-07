import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# 環境変数読み込み
load_dotenv()

# OpenAIクライアント初期化（新しいAPI）
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.set_page_config(page_title="ChatGPT風チャットUI", layout="wide")
st.title("🧠 ChatGPT風チャットアプリ")

# セッションステートに会話履歴を保存
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "あなたは親切なAIアシスタントです。"}
    ]

# 画面表示：過去のメッセージを表示
for msg in st.session_state.messages[1:]:  # systemメッセージは非表示
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください"):
    # ユーザーメッセージ表示
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # OpenAIへの問い合わせ（新しいAPI）
    with st.spinner("ChatGPTの応答を生成中..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # または "gpt-4"
                messages=st.session_state.messages,
                max_tokens=1000,
                temperature=0.7
            )
            
            # レスポンス取得（新しいAPI形式）
            assistant_message = response.choices[0].message.content
            
            # 会話履歴に追加
            st.session_state.messages.append({
                "role": "assistant", 
                "content": assistant_message
            })
            
            # アシスタントの応答表示
            st.chat_message("assistant").markdown(assistant_message)
            
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
            st.error("APIキーが正しく設定されているか確認してください。")
