import markdown2

# テスト用のMarkdownテキスト
test_text = """# キーマカレーの買い物リスト

## 必要な材料（4人分）

### メイン食材
- [ ] 合い挽き肉：400g
- [ ] 玉ねぎ：2個（みじん切り用）
- [ ] にんじん：1本
- [ ] トマト缶：1缶（400g）
- [ ] にんにく：2片
- [ ] しょうが：1片（親指大）

### スパイス・調味料
- [ ] カレー粉：大さじ3
- [ ] ガラムマサラ：小さじ1
- [ ] クミンシード：小さじ1/2
- [ ] **ヨーグルト**：大さじ2（隠し味）
- [ ] コンソメキューブ：1個
- [ ] 醤油：小さじ1

### 仕上げ用
- [ ] バター：10g
- [ ] 生クリーム：50ml（お好みで）
- [ ] パクチー：1束（トッピング用）

## 買い物メモ
> **スーパー**: 肉と野菜はイオンで新鮮なものを
> **スパイス**: カルディで本格的なガラムマサラを購入

### 予算
- 概算：**2,500円**程度
- セール情報：火曜日は肉類10%OFF

## レシピのポイント
1. 玉ねぎは**飴色になるまで**じっくり炒める
2. スパイスは焦がさないよう**弱火で香りを出す**
3. 最後にヨーグルトを加えてコクを出す

---
*参考レシピ: [本格キーマカレーの作り方](https://example.com)*
"""

# インデントを削除
import re
cleaned_text = re.sub(r'^  ', '', test_text, flags=re.MULTILINE)

print("=== Cleaned Markdown ===")
print(cleaned_text)

print("\n=== Generated HTML ===")
html = markdown2.markdown(cleaned_text, extras=[
    'fenced-code-blocks', 
    'tables', 
    'break-on-newline',
    'header-ids',
    'strike',
    'task_list',
    'code-friendly'
])
print(html)