import os
import requests
from bs4 import BeautifulSoup
import mimetypes


# 保存先ディレクトリ
SAVE_DIR = "downloaded_images"

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def fetch_image_urls(query, max_images=5):
    search_url = f"https://www.bing.com/images/search?q={query}&form=HDRSC3"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    images = []
    for img_tag in soup.find_all("img"):
        img_url = img_tag.get("src")
        if img_url and img_url.startswith("http"):
            images.append(img_url)
        if len(images) >= max_images:
            break
    return images

import mimetypes

def download_images(image_urls, save_dir):
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "")
            ext = mimetypes.guess_extension(content_type.split(";")[0].strip()) or ".jpg"

            filename = os.path.join(save_dir, f"img_{i}{ext}")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ {filename} を保存しました")
        except Exception as e:
            print(f"❌ {url} のダウンロードに失敗: {e}")

def main():
    query = input("検索キーワードを入力してください（例: 富士山）: ").strip()
    create_dir(SAVE_DIR)
    print("🔍 画像URLを収集中...")
    image_urls = fetch_image_urls(query)
    print(f"📥 {len(image_urls)} 件の画像URLを取得しました。")
    download_images(image_urls, SAVE_DIR)

if __name__ == "__main__":
    main()
