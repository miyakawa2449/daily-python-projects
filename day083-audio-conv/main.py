from pydub import AudioSegment
import os

def convert_audio(input_file, output_format="wav"):
    """音声ファイルを別形式に変換"""
    if not os.path.exists(input_file):
        print(f"❌ ファイルが見つかりません: {input_file}")
        return
    
    filename, ext = os.path.splitext(os.path.basename(input_file))
    output_file = f"{filename}_converted.{output_format}"

    try:
        print(f"🎧 読み込み中: {input_file}")
        sound = AudioSegment.from_file(input_file)

        print(f"💾 変換して保存中: {output_file}")
        sound.export(output_file, format=output_format)

        print(f"✅ 変換完了: {output_file}")
    except Exception as e:
        print(f"🚨 エラー発生: {e}")

# --- 使用例 ---
if __name__ == "__main__":
    print("🎙 音声ファイル変換ツール")
    path = input("🎵 入力ファイルのパス（例: song.mp3）: ").strip()
    fmt = input("📀 出力フォーマット（例: wav, mp3, ogg）: ").strip().lower() or "wav"
    convert_audio(path, fmt)
