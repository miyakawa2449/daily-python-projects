# Pythonプログラミング入門

## はじめに

**Python**は、シンプルで読みやすい文法を持つ*プログラミング言語*です。
初心者から上級者まで幅広く使われています。

## Pythonの特徴

### 1. シンプルな文法

Pythonのコードは他の言語と比べて非常に読みやすいです。

```python
# Hello Worldの例
def hello_world():
    print("Hello, World!")
    
# 関数の呼び出し
hello_world()
```

### 2. 豊富なライブラリ

- **NumPy**: 数値計算
- **Pandas**: データ分析
- **Django/Flask**: Webフレームワーク
- **TensorFlow/PyTorch**: 機械学習

### 3. 多様な用途

1. Web開発
2. データサイエンス
3. 機械学習・AI
4. 自動化スクリプト
5. ゲーム開発

## コード例

### リスト内包表記

```python
# 1から10までの偶数のリストを作成
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### 辞書の操作

```python
# 学生の成績管理
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# 平均点を計算
average = sum(students.values()) / len(students)
print(f"平均点: {average:.1f}")
```

## 便利なリンク

- [Python公式サイト](https://www.python.org/)
- [Python日本語ドキュメント](https://docs.python.org/ja/)
- [PyPI - Pythonパッケージインデックス](https://pypi.org/)

## まとめ

> Pythonは学習しやすく、実用的なプログラミング言語です。
> 
> ぜひ一緒にPythonの世界を探索しましょう！

---

*最終更新日: 2025年8月5日*