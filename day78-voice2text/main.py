import speech_recognition as sr

def recognize_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ マイクをオンにしています...話してください")
        recognizer.adjust_for_ambient_noise(source)  # ノイズキャンセル
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ja-JP")
        print(f"✅ 認識結果: {text}")
    except sr.UnknownValueError:
        print("❌ 音声を認識できませんでした")
    except sr.RequestError as e:
        print(f"🚨 API通信エラー: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
