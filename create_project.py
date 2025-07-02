#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def create_project(project_name):
    """指定したフォルダに空のmain.pyとREADME.mdを作成する"""
    
    project_dir = Path(project_name)
    
    if project_dir.exists():
        print(f"エラー: フォルダ '{project_name}' は既に存在します。")
        return False
    
    try:
        project_dir.mkdir()
        print(f"フォルダ '{project_name}' を作成しました。")
        
        main_py = project_dir / "main.py"
        main_py.write_text("")
        print(f"{main_py} を作成しました。")
        
        readme_content = f"""# {project_name}
## アプリケーション名
アプリケーション概要

## ファイル構成

## 実行方法

## 使い方

## 📖 学んだことや今後の改善案（学習ログ）
"""
        
        readme_md = project_dir / "README.md"
        readme_md.write_text(readme_content)
        print(f"{readme_md} を作成しました。")
        
        return True
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("使用方法: python create_project.py <プロジェクト名>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    if create_project(project_name):
        print(f"\nプロジェクト '{project_name}' の作成が完了しました！")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()