import os

def batch_rename(directory, prefix):
    # ディレクトリ内のファイル一覧取得
    files = os.listdir(directory)
    print(f"リネーム対象ファイル: {files}")

    for i, filename in enumerate(files, 1):
        # フルパスを作成
        old_path = os.path.join(directory, filename)

        # ディレクトリや隠しファイルをスキップ
        if os.path.isdir(old_path) or filename.startswith('.'):
            continue

        # 拡張子分離
        name, ext = os.path.splitext(filename)

        # 新しいファイル名を作成
        new_filename = f"{prefix}_{i}{ext}"
        new_path = os.path.join(directory, new_filename)

        print(f"{filename} → {new_filename}")

        # 実際にリネーム
        os.rename(old_path, new_path)

if __name__ == "__main__":
    target_dir = input("対象フォルダのパスを入力: ").strip()
    prefix = input("新しいファイル名の接頭辞を入力: ").strip()
    batch_rename(target_dir, prefix)
    print("リネームが完了しました！")
