// static/js/editor.js
let currentFile = null;
let currentImage = null;
let editHistory = []; // 編集履歴
let isProcessing = false; // 処理中フラグ

// DOM要素の取得
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const uploadSection = document.getElementById('uploadSection');
const editorSection = document.getElementById('editorSection');
const previewImage = document.getElementById('previewImage');
const imageInfo = document.getElementById('imageInfo');

// ファイル入力の初期化
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
});

function setupEventListeners() {
    // ファイル入力
    fileInput.addEventListener('change', handleFileSelect);
    
    // ドラッグ&ドロップ
    dropZone.addEventListener('dragover', handleDragOver);
    dropZone.addEventListener('dragleave', handleDragLeave);
    dropZone.addEventListener('drop', handleDrop);
    
    // クリックでファイル選択
    dropZone.addEventListener('click', () => fileInput.click());
}

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        uploadFile(file);
    }
}

function handleDragOver(event) {
    event.preventDefault();
    dropZone.classList.add('dragover');
}

function handleDragLeave(event) {
    event.preventDefault();
    dropZone.classList.remove('dragover');
}

function handleDrop(event) {
    event.preventDefault();
    dropZone.classList.remove('dragover');
    
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        uploadFile(files[0]);
    }
}

async function uploadFile(file) {
    // ファイルサイズチェック
    if (file.size > 10 * 1024 * 1024) {
        alert('ファイルサイズは10MB以下にしてください。');
        return;
    }
    
    // ファイル形式チェック
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp'];
    if (!allowedTypes.includes(file.type)) {
        alert('対応していないファイル形式です。JPG、PNG、GIF、WEBPファイルを選択してください。');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        // アップロード表示
        showLoading();
        
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            currentFile = result;
            displayImage(result.url, result.original_name);
            showEditor();
        } else {
            alert(result.error || 'アップロードに失敗しました。');
        }
    } catch (error) {
        console.error('アップロードエラー:', error);
        alert('アップロードに失敗しました。');
    } finally {
        hideLoading();
    }
}

function displayImage(imageUrl, originalName) {
    previewImage.src = imageUrl;
    previewImage.onload = function() {
        updateImageInfo(originalName, previewImage.naturalWidth, previewImage.naturalHeight);
    };
    
    // 編集履歴をクリア
    editHistory = [];
}

function updateImageInfo(originalName, width, height) {
    const editCount = editHistory.length;
    const statusText = editCount > 0 ? `（${editCount}回編集済み）` : '';
    
    imageInfo.innerHTML = `
        <strong>📁 ファイル名:</strong> ${originalName} ${statusText}<br>
        <strong>📐 サイズ:</strong> ${width} × ${height}px<br>
        <strong>💾 現在のファイル:</strong> ${getCurrentFilename()}<br>
        <strong>🔄 編集回数:</strong> ${editCount}回
    `;
}

function showEditor() {
    uploadSection.style.display = 'none';
    editorSection.style.display = 'block';
}

function showLoading() {
    dropZone.innerHTML = `
        <div class="drop-zone-content">
            <div class="upload-icon">⏳</div>
            <h3>アップロード中...</h3>
        </div>
    `;
}

function hideLoading() {
    dropZone.innerHTML = `
        <div class="drop-zone-content">
            <div class="upload-icon">📁</div>
            <h3>画像をドラッグ&ドロップ</h3>
            <p>または</p>
            <label for="fileInput" class="upload-btn">
                ファイルを選択
                <input type="file" id="fileInput" accept="image/*" hidden>
            </label>
            <div class="file-info">
                <small>対応形式: JPG, PNG, GIF, WEBP（最大10MB）</small>
            </div>
        </div>
    `;
    setupEventListeners();
}

// 編集機能（とりあえずダミー）
async function rotateImage(degrees) {
    if (!currentFile || isProcessing) {
        return;
    }
    
    isProcessing = true;
    showProcessing('回転中...');
    
    try {
        const operation = degrees > 0 ? 'rotate_right' : 'rotate_left';
        
        const response = await fetch('/edit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                filename: getCurrentFilename(),
                operation: operation
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            // 編集履歴に追加
            editHistory.push({
                operation: operation,
                filename: result.edited_filename,
                url: result.edited_url
            });
            
            // プレビューを更新
            updatePreview(result.edited_url, result.edited_filename);
            updateImageInfo(currentFile.original_name, result.width, result.height);
            
            console.log(`画像を${degrees}度回転しました`);
        } else {
            alert(result.error || '回転に失敗しました');
        }
        
    } catch (error) {
        console.error('回転エラー:', error);
        alert('回転処理でエラーが発生しました');
    } finally {
        isProcessing = false;
        hideProcessing();
    }
}

async function resetImage() {
    if (!currentFile || isProcessing) {
        return;
    }
    
    if (!confirm('すべての編集をリセットしますか？')) {
        return;
    }
    
    isProcessing = true;
    showProcessing('リセット中...');
    
    try {
        const response = await fetch('/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                original_filename: currentFile.filename
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            // 編集履歴をクリア
            editHistory = [];
            
            // 元画像に戻す
            updatePreview(result.reset_url, result.filename);
            
            // 元画像の情報で更新
            const img = new Image();
            img.onload = function() {
                updateImageInfo(currentFile.original_name, img.width, img.height);
            };
            img.src = result.reset_url;
            
            console.log('画像をリセットしました');
        } else {
            alert(result.error || 'リセットに失敗しました');
        }
        
    } catch (error) {
        console.error('リセットエラー:', error);
        alert('リセット処理でエラーが発生しました');
    } finally {
        isProcessing = false;
        hideProcessing();
    }
}

function downloadImage() {
    if (!currentFile) {
        alert('ダウンロードする画像がありません');
        return;
    }
    
    // 編集済みファイルがある場合は最新の編集版をダウンロード
    let downloadUrl, downloadName;
    
    if (editHistory.length > 0) {
        const latestEdit = editHistory[editHistory.length - 1];
        downloadUrl = latestEdit.url;
        downloadName = `edited_${currentFile.original_name}`;
    } else {
        downloadUrl = currentFile.url;
        downloadName = currentFile.original_name;
    }
    
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = downloadName;
    link.click();
    
    console.log(`${downloadName} をダウンロードしました`);
}

// ヘルパー関数

function getCurrentFilename() {
    // 最新の編集ファイル名を取得
    if (editHistory.length > 0) {
        return editHistory[editHistory.length - 1].filename;
    }
    return currentFile.filename;
}

function updatePreview(imageUrl, filename) {
    previewImage.src = imageUrl;
    
    // スムーズなアニメーション
    previewImage.style.opacity = '0.5';
    setTimeout(() => {
        previewImage.style.opacity = '1';
    }, 150);
}

function showProcessing(message) {
    // 処理中の表示
    const processingDiv = document.createElement('div');
    processingDiv.id = 'processingOverlay';
    processingDiv.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.7);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        color: white;
        font-size: 1.2rem;
    `;
    processingDiv.innerHTML = `
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 20px;">⚙️</div>
            <div>${message}</div>
        </div>
    `;
    
    document.body.appendChild(processingDiv);
}

function hideProcessing() {
    const overlay = document.getElementById('processingOverlay');
    if (overlay) {
        overlay.remove();
    }
}