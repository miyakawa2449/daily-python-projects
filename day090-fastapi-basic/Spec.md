# 📊 FastAPI Simple Note API - 仕様書

## 📋 プロジェクト概要

### 🎯 **アプリケーション名**
**Simple Note API - FastAPIによるREST API基本実装**

### 📝 **プロジェクト説明**
FastAPIフレームワークを使用して構築されたシンプルなメモ管理REST APIです。CRUD操作（作成・読取・更新・削除）の完全な実装と、自動API文書生成機能を提供します。モダンなWeb API開発の基礎学習に最適なプロジェクトです。

### 🗂️ **ファイル構成**
```
day90-fastapi-basic/
├── main.py                 # メインアプリケーション
├── Spec.md                # この仕様書ファイル
└── README.md              # プロジェクト説明（予定）
```

## 🛠️ **技術仕様**

### 📚 **使用技術**
- **FastAPI 0.104+**: モダンなPython Webフレームワーク
- **Pydantic**: データバリデーションとシリアライゼーション
- **Uvicorn**: ASGI（非同期）Webサーバー
- **Python 3.7+**: 型ヒント完全対応

### 🔧 **依存ライブラリ**
```bash
pip install fastapi uvicorn
```

### 🚀 **起動方法**
```bash
uvicorn main:app --reload
```

### 🌐 **アクセスURL**
- **アプリケーション**: `http://127.0.0.1:8000`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
- **OpenAPI仕様**: `http://127.0.0.1:8000/openapi.json`

## 📊 **データモデル**

### 🗄️ **Note モデル**
```python
class Note(BaseModel):
    id: int        # ノートの一意識別子
    title: str     # ノートのタイトル
    content: str   # ノートの内容
```

### 📦 **データストレージ**
```python
notes: List[Note] = []  # メモリ上のリスト（簡易DB）
```

**注意**: 現在の実装ではメモリ上にデータを保存するため、サーバー再起動時にデータは消失します。

## 🌐 **API エンドポイント仕様**

### 📖 **1. 全ノート取得**
```http
GET /notes
```

**レスポンス**:
```json
[
  {
    "id": 1,
    "title": "サンプルノート",
    "content": "これはテストノートです"
  }
]
```

**HTTPステータス**:
- `200 OK`: 成功（空配列も含む）

---

### 🔍 **2. 特定ノート取得**
```http
GET /notes/{note_id}
```

**パラメータ**:
- `note_id` (int): 取得するノートのID

**レスポンス例**:
```json
{
  "id": 1,
  "title": "サンプルノート",
  "content": "これはテストノートです"
}
```

**HTTPステータス**:
- `200 OK`: ノートが見つかった場合
- `404 Not Found`: 指定されたIDのノートが存在しない場合

**エラーレスポンス**:
```json
{
  "detail": "Note not found"
}
```

---

### ✏️ **3. ノート作成**
```http
POST /notes
```

**リクエストボディ**:
```json
{
  "id": 1,
  "title": "新しいノート",
  "content": "ノートの内容をここに記述"
}
```

**レスポンス**:
```json
{
  "id": 1,
  "title": "新しいノート",
  "content": "ノートの内容をここに記述"
}
```

**HTTPステータス**:
- `200 OK`: ノート作成成功
- `400 Bad Request`: 同じIDのノートが既に存在する場合
- `422 Unprocessable Entity`: リクエストデータの形式が無効

**エラーレスポンス（ID重複）**:
```json
{
  "detail": "Note ID already exists"
}
```

---

### 🔄 **4. ノート更新**
```http
PUT /notes/{note_id}
```

**パラメータ**:
- `note_id` (int): 更新するノートのID

**リクエストボディ**:
```json
{
  "id": 1,
  "title": "更新されたタイトル",
  "content": "更新された内容"
}
```

**レスポンス**:
```json
{
  "id": 1,
  "title": "更新されたタイトル",
  "content": "更新された内容"
}
```

**HTTPステータス**:
- `200 OK`: 更新成功
- `404 Not Found`: 指定されたIDのノートが存在しない場合

---

### 🗑️ **5. ノート削除**
```http
DELETE /notes/{note_id}
```

**パラメータ**:
- `note_id` (int): 削除するノートのID

**レスポンス**:
```json
{
  "message": "Note deleted successfully"
}
```

**HTTPステータス**:
- `200 OK`: 削除成功
- `404 Not Found`: 指定されたIDのノートが存在しない場合

## 🧪 **動作テスト方法**

### 🌐 **Swagger UIでのテスト**
1. `http://127.0.0.1:8000/docs` にアクセス
2. 各エンドポイントで「Try it out」をクリック
3. パラメータを入力して「Execute」を実行
4. レスポンスを確認

### 💻 **cURLでのテスト**

#### **ノート作成**
```bash
curl -X POST "http://127.0.0.1:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "テストノート",
    "content": "これはcURLでのテストです"
  }'
```

#### **全ノート取得**
```bash
curl "http://127.0.0.1:8000/notes"
```

#### **特定ノート取得**
```bash
curl "http://127.0.0.1:8000/notes/1"
```

#### **ノート更新**
```bash
curl -X PUT "http://127.0.0.1:8000/notes/1" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "更新されたノート",
    "content": "内容も更新されました"
  }'
```

#### **ノート削除**
```bash
curl -X DELETE "http://127.0.0.1:8000/notes/1"
```

## 🎯 **FastAPIの主要機能と学習ポイント**

### ✨ **自動生成される機能**
- **API文書**: Swagger UI + ReDoc
- **データ検証**: Pydantic による自動バリデーション
- **型チェック**: Python型ヒントの活用
- **エラーハンドリング**: 適切なHTTPステータスコード
- **JSON変換**: 自動シリアライゼーション・デシリアライゼーション

### 🔧 **開発効率の向上**
- **ホットリロード**: `--reload` オプションでコード変更時の自動再起動
- **インタラクティブテスト**: ブラウザから直接API実行
- **型補完**: IDEでの自動補完とエラー検出
- **明確なエラーメッセージ**: デバッグが容易

### 📊 **Flask との比較**

| 機能 | Flask | FastAPI |
|------|-------|---------|
| **API文書** | 手動作成 | 🚀 自動生成 |
| **データ検証** | 手動実装 | 🚀 自動バリデーション |
| **型チェック** | なし | 🚀 完全対応 |
| **テストUI** | なし | 🚀 Swagger UI内蔵 |
| **開発速度** | 普通 | 🚀 高速 |
| **実行性能** | 普通 | 🚀 高性能（Node.js並み） |

## 🔍 **エラーハンドリング**

### 📊 **HTTPステータスコード一覧**
- `200 OK`: 正常処理
- `400 Bad Request`: 不正なリクエスト（ID重複等）
- `404 Not Found`: リソースが見つからない
- `422 Unprocessable Entity`: データ形式エラー（Pydantic検証失敗）

### 🚨 **エラーレスポンス形式**
```json
{
  "detail": "エラーメッセージ"
}
```

### 🔧 **バリデーションエラー例**
```json
{
  "detail": [
    {
      "loc": ["body", "id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

## 🚀 **フルスタック拡張提案**

## 🗄️ **MySQL データベース統合**

### 📋 **MySQL統合のメリット**
- **データ永続化**: サーバー再起動後もデータが保持される
- **本格運用**: 実際のWebアプリケーションレベルのデータ管理
- **スケーラビリティ**: 大量データの効率的な処理
- **データ整合性**: トランザクション処理による安全な操作

### 🔧 **必要なライブラリ**
```bash
# MySQL統合用パッケージ
pip install sqlalchemy pymysql python-multipart

# 開発用（オプション）
pip install alembic  # DBマイグレーション
```

### 🏗️ **MySQL統合版のアーキテクチャ**
```python
# database.py - DB設定
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://username:password@localhost/notedb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# models.py - DBモデル
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class NoteDB(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# schemas.py - Pydanticモデル
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True  # SQLAlchemyモデルとの互換性

# main.py - メインアプリケーション（MySQL版）
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

app = FastAPI(title="Note API with MySQL")

# 依存性注入用のDB取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/notes", response_model=List[Note])
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = db.query(NoteDB).offset(skip).limit(limit).all()
    return notes

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = NoteDB(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    for field, value in note.dict(exclude_unset=True).items():
        setattr(db_note, field, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(NoteDB).filter(NoteDB.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted successfully"}
```

### 🗄️ **MySQL データベース設定**
```sql
-- データベース作成
CREATE DATABASE notedb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ユーザー作成と権限付与
CREATE USER 'noteuser'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON notedb.* TO 'noteuser'@'localhost';
FLUSH PRIVILEGES;

-- テーブル作成（SQLAlchemyが自動実行）
-- CREATE TABLE notes (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(200) NOT NULL,
--     content TEXT NOT NULL,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--     updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );
```

## 🌐 **Vue.js フロントエンド統合**

### 🎨 **Vue.js統合のメリット**
- **リアクティブUI**: データ変更の即座の反映
- **SPA体験**: ページリロード不要の滑らかな操作
- **コンポーネント化**: 再利用可能なUI部品
- **現代的UX**: モバイルフレンドリーなレスポンシブデザイン

### 📦 **必要なパッケージ**
```bash
# Vue.js プロジェクト作成
npm create vue@latest note-app-frontend
cd note-app-frontend

# 追加パッケージ
npm install axios              # HTTP通信
npm install @headlessui/vue   # UIコンポーネント
npm install @heroicons/vue    # アイコン
npm install tailwindcss       # CSSフレームワーク
```

### 🏗️ **フロントエンド構成**
```
note-app-frontend/
├── src/
│   ├── components/
│   │   ├── NoteList.vue      # ノート一覧コンポーネント
│   │   ├── NoteForm.vue      # ノート作成・編集フォーム
│   │   ├── NoteCard.vue      # 個別ノート表示
│   │   └── ConfirmDialog.vue # 削除確認ダイアログ
│   ├── services/
│   │   └── api.js            # API通信レイヤー
│   ├── App.vue               # メインアプリケーション
│   └── main.js               # エントリーポイント
└── package.json
```

### 🔧 **API通信サービス**
```javascript
// src/services/api.js
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const noteApi = {
  // 全ノート取得
  async getAllNotes() {
    const response = await api.get('/notes')
    return response.data
  },

  // 特定ノート取得
  async getNote(id) {
    const response = await api.get(`/notes/${id}`)
    return response.data
  },

  // ノート作成
  async createNote(note) {
    const response = await api.post('/notes', note)
    return response.data
  },

  // ノート更新
  async updateNote(id, note) {
    const response = await api.put(`/notes/${id}`, note)
    return response.data
  },

  // ノート削除
  async deleteNote(id) {
    const response = await api.delete(`/notes/${id}`)
    return response.data
  },
}
```

### 🎨 **メインアプリケーション**
```vue
<!-- src/App.vue -->
<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <header class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">📝 Note App</h1>
        <p class="text-gray-600">FastAPI + Vue.js による本格ノートアプリ</p>
      </header>

      <!-- ノート作成フォーム -->
      <div class="mb-8">
        <NoteForm 
          :note="editingNote" 
          :is-editing="isEditing"
          @save="handleSave"
          @cancel="handleCancel"
        />
      </div>

      <!-- ノート一覧 -->
      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <NoteCard
          v-for="note in notes"
          :key="note.id"
          :note="note"
          @edit="handleEdit"
          @delete="handleDelete"
        />
      </div>

      <!-- ローディング状態 -->
      <div v-if="loading" class="text-center py-8">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
        <p class="mt-2 text-gray-600">読み込み中...</p>
      </div>

      <!-- エラー表示 -->
      <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { noteApi } from './services/api'
import NoteForm from './components/NoteForm.vue'
import NoteCard from './components/NoteCard.vue'

export default {
  name: 'App',
  components: {
    NoteForm,
    NoteCard,
  },
  setup() {
    const notes = ref([])
    const editingNote = ref(null)
    const isEditing = ref(false)
    const loading = ref(false)
    const error = ref('')

    // ノート一覧取得
    const fetchNotes = async () => {
      try {
        loading.value = true
        error.value = ''
        notes.value = await noteApi.getAllNotes()
      } catch (err) {
        error.value = 'ノートの取得に失敗しました'
        console.error(err)
      } finally {
        loading.value = false
      }
    }

    // ノート保存（作成・更新）
    const handleSave = async (noteData) => {
      try {
        if (isEditing.value && editingNote.value) {
          await noteApi.updateNote(editingNote.value.id, noteData)
        } else {
          await noteApi.createNote(noteData)
        }
        await fetchNotes()
        handleCancel()
      } catch (err) {
        error.value = 'ノートの保存に失敗しました'
        console.error(err)
      }
    }

    // 編集モード開始
    const handleEdit = (note) => {
      editingNote.value = { ...note }
      isEditing.value = true
    }

    // 編集キャンセル
    const handleCancel = () => {
      editingNote.value = null
      isEditing.value = false
    }

    // ノート削除
    const handleDelete = async (note) => {
      if (confirm(`「${note.title}」を削除しますか？`)) {
        try {
          await noteApi.deleteNote(note.id)
          await fetchNotes()
        } catch (err) {
          error.value = 'ノートの削除に失敗しました'
          console.error(err)
        }
      }
    }

    // 初期データ読み込み
    onMounted(() => {
      fetchNotes()
    })

    return {
      notes,
      editingNote,
      isEditing,
      loading,
      error,
      handleSave,
      handleEdit,
      handleCancel,
      handleDelete,
    }
  },
}
</script>
```

### 🎨 **ノートカードコンポーネント**
```vue
<!-- src/components/NoteCard.vue -->
<template>
  <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
    <div class="flex justify-between items-start mb-4">
      <h3 class="text-lg font-semibold text-gray-900 truncate">
        {{ note.title }}
      </h3>
      <div class="flex space-x-2 ml-4">
        <button
          @click="$emit('edit', note)"
          class="text-blue-600 hover:text-blue-800 transition-colors"
          title="編集"
        >
          ✏️
        </button>
        <button
          @click="$emit('delete', note)"
          class="text-red-600 hover:text-red-800 transition-colors"
          title="削除"
        >
          🗑️
        </button>
      </div>
    </div>
    
    <p class="text-gray-700 text-sm mb-4 line-clamp-3">
      {{ note.content }}
    </p>
    
    <div class="text-xs text-gray-500">
      <p>作成: {{ formatDate(note.created_at) }}</p>
      <p v-if="note.updated_at !== note.created_at">
        更新: {{ formatDate(note.updated_at) }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NoteCard',
  props: {
    note: {
      type: Object,
      required: true,
    },
  },
  emits: ['edit', 'delete'],
  methods: {
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('ja-JP', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      })
    },
  },
}
</script>
```

### 🎨 **ノートフォームコンポーネント**
```vue
<!-- src/components/NoteForm.vue -->
<template>
  <div class="bg-white rounded-lg shadow-md p-6">
    <h2 class="text-xl font-semibold mb-4">
      {{ isEditing ? 'ノート編集' : '新規ノート作成' }}
    </h2>
    
    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label for="title" class="block text-sm font-medium text-gray-700 mb-2">
          タイトル
        </label>
        <input
          id="title"
          v-model="formData.title"
          type="text"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="ノートのタイトルを入力..."
        />
      </div>
      
      <div class="mb-4">
        <label for="content" class="block text-sm font-medium text-gray-700 mb-2">
          内容
        </label>
        <textarea
          id="content"
          v-model="formData.content"
          required
          rows="4"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="ノートの内容を入力..."
        ></textarea>
      </div>
      
      <div class="flex space-x-3">
        <button
          type="submit"
          class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors"
        >
          {{ isEditing ? '📝 更新' : '➕ 作成' }}
        </button>
        
        <button
          v-if="isEditing"
          type="button"
          @click="$emit('cancel')"
          class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-400 transition-colors"
        >
          キャンセル
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref, watch } from 'vue'

export default {
  name: 'NoteForm',
  props: {
    note: {
      type: Object,
      default: null,
    },
    isEditing: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['save', 'cancel'],
  setup(props, { emit }) {
    const formData = ref({
      title: '',
      content: '',
    })

    // 編集時のデータ反映
    watch(
      () => props.note,
      (newNote) => {
        if (newNote) {
          formData.value = {
            title: newNote.title,
            content: newNote.content,
          }
        } else {
          formData.value = {
            title: '',
            content: '',
          }
        }
      },
      { immediate: true }
    )

    const handleSubmit = () => {
      emit('save', formData.value)
      if (!props.isEditing) {
        formData.value = { title: '', content: '' }
      }
    }

    return {
      formData,
      handleSubmit,
    }
  },
}
</script>
```

## 🌐 **CORS設定（FastAPI側）**
```python
# main.py にCORS設定を追加
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Note API with MySQL")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Vue.js開発サーバー
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🚀 **フルスタック開発手順**

### 📋 **開発ステップ**
1. **バックエンド開発**
   ```bash
   # MySQL統合版FastAPI
   pip install fastapi uvicorn sqlalchemy pymysql
   uvicorn main:app --reload
   ```

2. **データベース準備**
   ```sql
   CREATE DATABASE notedb;
   -- テーブル作成はSQLAlchemyが自動実行
   ```

3. **フロントエンド開発**
   ```bash
   npm create vue@latest note-app-frontend
   cd note-app-frontend
   npm install axios
   npm run dev
   ```

4. **統合テスト**
   - FastAPI: `http://localhost:8000`
   - Vue.js: `http://localhost:3000`

### 🎯 **期待される成果**
- **永続化されたデータ**: MySQL による安全なデータ保存
- **現代的UI**: Vue.js による美しいユーザーインターフェース
- **リアルタイム更新**: SPA による滑らかな操作体験
- **本格的アプリ**: 企業レベルのWebアプリケーション

## 💡 **学習成果**

### ✅ **習得できる技術**
- **REST API設計**: HTTP メソッドの適切な使用
- **JSON通信**: リクエスト・レスポンスの標準的な形式
- **データモデリング**: Pydantic を使用した型安全なデータ構造
- **エラーハンドリング**: 適切なHTTPステータスコードの返却
- **API文書化**: Swagger/OpenAPI による自動文書生成

### 🎯 **プロジェクトの価値**
- **学習用途**: モダンWeb API開発の基礎理解
- **プロトタイプ**: 新機能の迅速な検証
- **本格開発**: 企業レベルのAPI開発基盤

### 📚 **参考リソース**
- **FastAPI公式ドキュメント**: https://fastapi.tiangolo.com/
- **Pydantic公式**: https://pydantic-docs.helpmanual.io/
- **OpenAPI仕様**: https://swagger.io/specification/
- **Vue.js公式**: https://vuejs.org/
- **SQLAlchemy**: https://www.sqlalchemy.org/

## 🎊 **まとめ**

このSimple Note APIは、FastAPIの基本機能を網羅した実践的な学習プロジェクトです。わずか50行程度のコードで、完全なCRUD操作、自動API文書生成、データ検証を実現しており、モダンなWeb API開発の効率性を体感できます。

MySQL統合により本格的なデータ永続化を、Vue.js統合により現代的なフロントエンドを実現でき、企業レベルのフルスタックWebアプリケーション開発の基礎を学習できます。

FastAPIの「Fast」は開発速度と実行速度の両方を意味し、このプロジェクトを通じて現代的なPython Web開発の威力を実感することができます。🚀✨