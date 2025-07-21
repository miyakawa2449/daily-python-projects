# 🎵 day83-audio-conv

## 📋 アプリケーション名
**音声ファイル変換ツール**

## 🎯 アプリケーション概要
PyDubライブラリを使用して、音声ファイルを異なるフォーマット間で変換するPythonツールです。MP3、WAV、OGG、FLAC、AACなど多様な音声フォーマットに対応し、簡単なコマンドライン操作で高品質な音声変換が可能です。FFmpegを内部で使用することで、幅広い音声コーデックをサポートしています。

## 📁 ファイル構成
```
day83-audio-conv/
├── main.py             # メインスクリプト
├── README.md          # このファイル
├── song.mp3           # サンプル音声ファイル（テスト用）
├── song_converted.wav  # 変換済みファイル（実行後作成）
└── music_converted.ogg # 変換済みファイル（実行後作成）
```

## 🔧 必要なライブラリ
```bash
# PyDubのインストール
pip install pydub

# FFmpegのインストール（Mac）
brew install ffmpeg

# FFmpegのインストール（Ubuntu/Debian）
sudo apt update
sudo apt install ffmpeg

# FFmpegのインストール（Windows）
# https://ffmpeg.org/download.html からダウンロード
```

## 🚀 実行方法
```bash
# プロジェクトディレクトリに移動
cd day83-audio-conv

# スクリプトを実行
python main.py
```

## 💻 使い方

### 1️⃣ **基本的な使い方**
```bash
python main.py

# 実行例
🎙 音声ファイル変換ツール
🎵 入力ファイルのパス（例: song.mp3）: music.mp3
📀 出力フォーマット（例: wav, mp3, ogg）: wav

🎧 読み込み中: music.mp3
💾 変換して保存中: music_converted.wav
✅ 変換完了: music_converted.wav
```

### 2️⃣ **様々な変換例**
```bash
# MP3 → WAV（非圧縮）
入力: song.mp3
出力フォーマット: wav
結果: song_converted.wav

# WAV → MP3（圧縮）
入力: audio.wav  
出力フォーマット: mp3
結果: audio_converted.mp3

# FLAC → OGG
入力: music.flac
出力フォーマット: ogg  
結果: music_converted.ogg

# デフォルト（WAV）変換
入力: sound.m4a
出力フォーマット: [Enter]
結果: sound_converted.wav
```

### 3️⃣ **プログラムから直接呼び出し**
```python
from main import convert_audio

# 関数として使用
convert_audio("input.mp3", "wav")
convert_audio("music.wav", "ogg") 
convert_audio("audio.m4a", "flac")
```

## 🛠️ 機能

### ✅ **対応フォーマット**

#### 📥 **入力対応フォーマット**
- **MP3** (.mp3) - MPEG Audio Layer 3
- **WAV** (.wav) - Waveform Audio File Format
- **FLAC** (.flac) - Free Lossless Audio Codec
- **AAC** (.aac, .m4a) - Advanced Audio Coding
- **OGG** (.ogg) - Ogg Vorbis
- **WMA** (.wma) - Windows Media Audio
- **AIFF** (.aiff) - Audio Interchange File Format

#### 📤 **出力対応フォーマット**
- **MP3** - 圧縮音声（可逆圧縮）
- **WAV** - 非圧縮音声（高品質）
- **OGG** - オープンソース圧縮音声
- **FLAC** - 可逆圧縮音声（高品質）
- **AAC** - 高効率圧縮音声

### ✅ **主要機能**
- **自動ファイル名生成**: `元ファイル名_converted.拡張子`
- **フォーマット自動判定**: 入力ファイルの形式を自動識別
- **エラーハンドリング**: ファイル不存在・変換失敗の適切な処理
- **デフォルト設定**: 出力フォーマット未指定時はWAV形式
- **パス解析**: フルパス入力に対応、ファイル名のみ抽出

## 📊 変換品質とファイルサイズの目安

### 🎵 **音声品質比較**
```
品質ランク（高→低）:
1. FLAC（可逆圧縮、元音質100%保持）
2. WAV（非圧縮、元音質100%保持）  
3. AAC（高効率圧縮、音質90-95%）
4. MP3（標準圧縮、音質85-95%）
5. OGG（オープン圧縮、音質85-90%）
```

### 💽 **ファイルサイズ目安**
```
3分間の楽曲の場合:
- WAV:   ~30MB（非圧縮）
- FLAC:  ~15-20MB（可逆圧縮）
- MP3:   ~3-7MB（320kbps→96kbps）
- AAC:   ~3-6MB（効率的圧縮）
- OGG:   ~4-8MB（品質設定依存）
```

## ⚙️ 技術仕様

### 🔧 **内部処理フロー**
```python
# 1. ファイル存在確認
os.path.exists(input_file)

# 2. 出力ファイル名自動生成  
filename, ext = os.path.splitext(os.path.basename(input_file))
output_file = f"{filename}_converted.{output_format}"

# 3. 音声ファイル読み込み（自動フォーマット判定）
sound = AudioSegment.from_file(input_file)

# 4. 指定フォーマットで出力（FFmpeg使用）
sound.export(output_file, format=output_format)
```

### 🎚️ **音声処理エンジン**
- **ライブラリ**: PyDub（Pythonラッパー）
- **エンジン**: FFmpeg（音声処理コア）
- **サポート**: 90以上の音声・動画フォーマット

## 📖 使用例

### 🎶 **音楽ファイル変換**
```bash
# CDリッピング音源をMP3に圧縮
python main.py
入力: cd_track01.wav
フォーマット: mp3
→ cd_track01_converted.mp3 (30MB → 5MB)
```

### 🎙️ **ポッドキャスト制作**
```bash  
# 録音音声を配信用OGGに変換
python main.py
入力: recording.wav
フォーマット: ogg
→ recording_converted.ogg
```

### 🎵 **アーカイブ用高品質保存**
```bash
# MP3音源を高品質FLACでアーカイブ
python main.py 
入力: music.mp3
フォーマット: flac
→ music_converted.flac
```

## ⚠️ 注意事項

### 🔍 **ファイル関連**
- **同名ファイル**: 既存ファイルは上書きされます
- **パス指定**: 相対パス・絶対パス両方に対応
- **ファイル権限**: 出力先ディレクトリの書き込み権限が必要

### 🎵 **音質関連**
- **アップコンバート不可**: 低品質→高品質変換では音質改善されません
- **圧縮による劣化**: MP3/AAC/OGG変換では音質が若干劣化します
- **サンプルレート**: 変換時に元ファイルの設定を維持

### 💻 **システム関連**
- **FFmpeg必須**: 多くのフォーマット対応にはFFmpegが必要
- **メモリ使用量**: 大容量ファイルは一時的に大量メモリを消費
- **処理時間**: ファイルサイズと変換フォーマットに依存

## 🐛 トラブルシューティング

### ❌ **FFmpegエラー**
```
FFmpeg not found
```
**解決方法**:
```bash
# Mac
brew install ffmpeg

# パス確認
which ffmpeg
```

### ❌ **フォーマットエラー**
```
CouldntDecodeError: Decoding failed
```
**解決方法**:
- ファイルの破損チェック
- 対応フォーマットの確認
- ファイル拡張子の正確性

### ❌ **メモリエラー**
```
MemoryError: 大容量ファイル処理時
```
**解決方法**:
- ファイルサイズを小さくする
- 不要なアプリケーションを終了
- より高性能なマシンで処理

## 📖 学んだことや今後の改善案（学習ログ）

### ✅ **学んだこと**

#### 🎵 **音声処理基礎**
- **AudioSegment**: PyDubの核となるクラス
- **from_file()**: 汎用音声ファイル読み込み機能
- **export()**: フォーマット変換・出力機能
- **FFmpeg連携**: 外部ツールとの連携方法

#### 🔧 **ファイル処理**
- **os.path.splitext()**: ファイル名と拡張子の分離
- **os.path.basename()**: パス部分の除去
- **os.path.exists()**: ファイル存在確認
- **文字列フォーマット**: f-string を使った動的ファイル名生成

#### 🎯 **エラーハンドリング**
- **try-except**: 音声変換処理の安全な実行
- **ファイル存在チェック**: 事前バリデーション
- **ユーザーフレンドリーな出力**: 日本語でのエラーメッセージ

#### 🌐 **クロスプラットフォーム対応**
- **FFmpegインストール**: Mac/Windows/Linux対応
- **パス処理**: OS依存しないファイルパス操作

### 🚀 **今後の改善案**

#### 🔥 **優先度高**
- [ ] **一括変換機能**: 複数ファイルの同時処理
- [ ] **品質設定**: ビットレート、サンプルレート指定
- [ ] **進行状況表示**: 大容量ファイル変換時のプログレスバー
- [ ] **出力ディレクトリ指定**: ファイル整理機能

#### 🌟 **優先度中**
- [ ] **GUI化**: tkinter/PyQt によるグラフィカルインターフェース
- [ ] **メタデータ保持**: タイトル、アーティスト情報の引き継ぎ
- [ ] **音声編集機能**: トリミング、音量調整、フェードイン・アウト
- [ ] **プリセット機能**: 用途別設定の保存（ポッドキャスト用、音楽用等）

#### 💡 **優先度低（発展）**
- [ ] **Webアプリ化**: Flask/FastAPI でブラウザ対応
- [ ] **クラウド連携**: Google Drive、Dropbox等への自動アップロード
- [ ] **音声解析**: 周波数解析、音量レベル測定
- [ ] **バッチ処理スクリプト**: コマンドライン引数での自動化

#### 🎵 **音声処理高度化**
- [ ] **ノイズ除去**: 背景雑音の自動除去
- [ ] **音量正規化**: 複数ファイル間の音量統一
- [ ] **チャンネル操作**: ステレオ↔モノラル変換
- [ ] **速度変更**: 再生速度調整（ピッチ維持）

### 🎯 **技術的課題と解決策**
```
課題: 大容量ファイルのメモリ使用量
解決策: ストリーミング処理 or チャンク分割処理

課題: 変換時間の長さ
解決策: 並列処理 or GPU加速（CUDA対応）

課題: 音質の劣化
解決策: 高品質エンコーダー設定 or 可逆圧縮推奨
```

### 📚 **参考になったリソース**
- [PyDub Documentation](https://pydub.com/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Audio File Formats Guide](https://en.wikipedia.org/wiki/Audio_file_format)
- [Digital Audio Basics](https://www.izotope.com/en/learn/digital-audio-basics.html)

### 🏆 **プロジェクト成果**
- **コード行数**: 約30行（コンパクト設計）
- **実装時間**: 約1-2時間
- **対応フォーマット**: 10以上の音声形式
- **プラットフォーム**: Mac/Windows/Linux対応

---
**🎉 プロジェクト完成日**: 2025年7月21日  
**⚡ 実装時間**: 約1-2時間  
**🛠️ 使用技術**: Python, PyDub, FFmpeg, File I/O