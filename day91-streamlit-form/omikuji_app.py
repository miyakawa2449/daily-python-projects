import streamlit as st
import random

# HTMLテンプレート風のスタイル適用
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# タイトルと説明
st.markdown("""
<div class="header">
    <h1>🎯 おみくじ占いアプリ</h1>
    <p>名前を入力して、おみくじを引いてみましょう！</p>
</div>
""", unsafe_allow_html=True)

# フォーム
with st.form("omikuji_form"):
    name = st.text_input("あなたの名前を入力してください")
    submitted = st.form_submit_button("おみくじを引く！")

# 結果処理
if submitted:
    if name.strip() == "":
        st.warning("名前を入力してください。")
    else:
        results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
        result = random.choice(results)
        messages = {
            "大吉": "今日は最高の1日になります！",
            "中吉": "良いことが起こる予感です！",
            "小吉": "ちょっとした幸運があるかも！",
            "吉": "何事も前向きに取り組みましょう！",
            "末吉": "無理せずマイペースで行きましょう。",
            "凶": "焦らず慎重に行動しましょう。",
            "大凶": "災い転じて福となす。前向きに！"
        }

        # 結果の表示
        st.markdown(f"""
        <div class="result-box">
            <h2>{name} さんの運勢は...</h2>
            <div class="result">{result}</div>
            <p>{messages[result]}</p>
        </div>
        """, unsafe_allow_html=True)
