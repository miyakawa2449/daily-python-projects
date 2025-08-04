// 画像ギャラリー JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // DOM要素取得
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const fileList = document.getElementById('file-list');
    const uploadBtn = document.getElementById('upload-btn');
    
    // ドラッグ&ドロップ機能
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });
    
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
    
    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
    });
    
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        handleFileSelection(files);
    });
    
    // ファイル選択ハンドラ
    fileInput.addEventListener('change', (e) => {
        handleFileSelection(e.target.files);
    });
    
    // ファイル選択処理
    function handleFileSelection(files) {
        if (files.length === 0) return;
        
        // ファイルリストクリア
        fileList.innerHTML = '';
        
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
        let validFiles = 0;
        
        // DataTransferオブジェクトを作成してfile inputに設定
        const dataTransfer = new DataTransfer();
        
        Array.from(files).forEach((file, index) => {
            if (allowedTypes.includes(file.type)) {
                displayFileItem(file);
                dataTransfer.items.add(file);
                validFiles++;
            } else {
                showAlert(`${file.name} は対応していないファイル形式です`, 'warning');
            }
        });
        
        // file inputにファイルを設定
        fileInput.files = dataTransfer.files;
        
        if (validFiles > 0) {
            uploadBtn.style.display = 'block';
            uploadBtn.textContent = `${validFiles}個のファイルをアップロード`;
        } else {
            uploadBtn.style.display = 'none';
        }
    }
    
    // ファイルアイテム表示
    function displayFileItem(file) {
        const fileItem = document.createElement('div');
        fileItem.className = 'file-item mb-2';
        
        const fileName = document.createElement('span');
        fileName.className = 'file-name';
        fileName.textContent = file.name;
        
        const fileSize = document.createElement('span');
        fileSize.className = 'file-size';
        fileSize.textContent = formatFileSize(file.size);
        
        fileItem.appendChild(fileName);
        fileItem.appendChild(fileSize);
        fileList.appendChild(fileItem);
    }
    
    // ファイルサイズフォーマット
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
    
    // アラート表示
    function showAlert(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.children[1]);
        
        // 5秒後に自動削除
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }
    
    // 画像モーダル処理
    const imageModal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');
    const modalTitle = document.getElementById('imageModalTitle');
    const modalFilename = document.getElementById('modalFilename');
    const modalSize = document.getElementById('modalSize');
    const modalUploaded = document.getElementById('modalUploaded');
    
    // サムネイルクリック時のモーダル表示
    document.querySelectorAll('.gallery-thumbnail').forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const src = this.dataset.src;
            const filename = this.dataset.filename;
            const size = this.dataset.size;
            const uploaded = this.dataset.uploaded;
            
            modalImage.src = src;
            modalTitle.textContent = filename;
            modalFilename.textContent = filename;
            modalSize.textContent = size;
            modalUploaded.textContent = uploaded;
        });
    });
    
    // キーボードナビゲーション
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const modal = bootstrap.Modal.getInstance(imageModal);
            if (modal) {
                modal.hide();
            }
        }
    });
    
    // アップロード進行状況
    const uploadForm = document.querySelector('form[action*="upload"]');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function() {
            uploadBtn.disabled = true;
            uploadBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>アップロード中...';
        });
    }
    
    // 画像遅延読み込み (Intersection Observer)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('.gallery-thumbnail').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // タッチデバイス対応
    if ('ontouchstart' in window) {
        document.querySelectorAll('.gallery-item').forEach(item => {
            item.addEventListener('touchstart', function() {
                this.classList.add('touch-active');
            });
            
            item.addEventListener('touchend', function() {
                setTimeout(() => {
                    this.classList.remove('touch-active');
                }, 150);
            });
        });
    }
});

// ページ読み込み完了時の処理
window.addEventListener('load', function() {
    // 画像の読み込み完了をアニメーションで表示
    document.querySelectorAll('.gallery-thumbnail').forEach((img, index) => {
        img.style.animationDelay = `${index * 0.1}s`;
    });
});