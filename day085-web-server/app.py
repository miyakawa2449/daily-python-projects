import os
import platform
import psutil
import datetime
import sys
import json
from pathlib import Path

def generate_system_info():
    """Pythonでしか取得できないシステム情報を収集"""
    try:
        return {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "os_name": platform.system(),
            "os_version": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor() or "不明",
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "cpu_count": psutil.cpu_count(),
            "cpu_percent": round(psutil.cpu_percent(interval=1), 1),
            "memory_total": round(psutil.virtual_memory().total / (1024**3), 2),
            "memory_percent": round(psutil.virtual_memory().percent, 1),
            "memory_available": round(psutil.virtual_memory().available / (1024**3), 2),
            "disk_usage": round(psutil.disk_usage('/').percent, 1),
            "current_dir": os.getcwd(),
            "python_path": sys.executable,
            "network_interfaces": get_network_info(),
            "top_processes": get_top_processes()
        }
    except Exception as e:
        return {"error": f"システム情報取得エラー: {e}"}

def get_network_info():
    """ネットワーク情報を取得"""
    network_info = []
    try:
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == 2:  # IPv4
                    network_info.append({
                        "interface": interface,
                        "ip": addr.address
                    })
    except Exception:
        pass
    return network_info[:3]  # 上位3個まで

def get_top_processes():
    """CPU使用率上位プロセスを取得"""
    processes = []
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                if proc.info['cpu_percent'] and proc.info['cpu_percent'] > 0:
                    processes.append({
                        "name": proc.info['name'],
                        "cpu_percent": round(proc.info['cpu_percent'], 1)
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # CPU使用率順でソート、上位5個
        return sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    except Exception:
        return []

def update_html_with_data():
    """既存のindex.htmlにシステム情報を埋め込む"""
    html_file = Path("public/index.html")
    
    # 既存のHTMLファイルを読み込み
    if not html_file.exists():
        print("❌ public/index.html が見つかりません")
        return False
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # システム情報を取得
        system_info = generate_system_info()
        
        # HTMLに埋め込むデータを準備
        data_sections = generate_html_sections(system_info)
        
        # プレースホルダーを置換
        # {{SYSTEM_DATA}} のような形式で埋め込み
        html_content = html_content.replace('{{SYSTEM_DATA}}', data_sections)
        html_content = html_content.replace('{{TIMESTAMP}}', system_info.get('timestamp', ''))
        html_content = html_content.replace('{{PYTHON_VERSION}}', system_info.get('python_version', ''))
        
        # 更新されたHTMLを保存
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ {html_file} を更新しました")
        print(f"🕐 更新時刻: {system_info.get('timestamp')}")
        return True
        
    except Exception as e:
        print(f"❌ HTML更新エラー: {e}")
        return False

def generate_html_sections(system_info):
    """システム情報をHTML形式で生成"""
    if "error" in system_info:
        return f'<div class="error">⚠️ {system_info["error"]}</div>'
    
    # ネットワーク情報のHTML
    network_html = ""
    for net in system_info.get("network_interfaces", []):
        network_html += f'<li><strong>{net["interface"]}:</strong> {net["ip"]}</li>'
    
    # プロセス情報のHTML
    process_html = ""
    for proc in system_info.get("top_processes", []):
        process_html += f'<li><strong>{proc["name"]}:</strong> {proc["cpu_percent"]}%</li>'
    
    return f"""
    <div class="system-info">
        <h2>🖥️ システム情報 <span class="timestamp">({system_info['timestamp']})</span></h2>
        
        <div class="info-grid">
            <div class="info-card">
                <h3>📊 基本情報</h3>
                <ul>
                    <li><strong>OS:</strong> {system_info['os_name']} {system_info['os_version']}</li>
                    <li><strong>アーキテクチャ:</strong> {system_info['machine']}</li>
                    <li><strong>プロセッサ:</strong> {system_info['processor']}</li>
                    <li><strong>Python:</strong> {system_info['python_version']}</li>
                </ul>
            </div>
            
            <div class="info-card">
                <h3>⚡ パフォーマンス</h3>
                <ul>
                    <li><strong>CPUコア:</strong> {system_info['cpu_count']}コア</li>
                    <li><strong>CPU使用率:</strong> 
                        <span class="metric">{system_info['cpu_percent']}%</span>
                        <div class="progress-bar">
                            <div class="progress" style="width: {system_info['cpu_percent']}%"></div>
                        </div>
                    </li>
                    <li><strong>メモリ使用率:</strong> 
                        <span class="metric">{system_info['memory_percent']}%</span>
                        <div class="progress-bar">
                            <div class="progress" style="width: {system_info['memory_percent']}%"></div>
                        </div>
                    </li>
                    <li><strong>メモリ:</strong> {system_info['memory_available']}GB / {system_info['memory_total']}GB 利用可能</li>
                    <li><strong>ディスク使用率:</strong> {system_info['disk_usage']}%</li>
                </ul>
            </div>
            
            <div class="info-card">
                <h3>🌐 ネットワーク</h3>
                <ul>
                    {network_html}
                </ul>
            </div>
            
            <div class="info-card">
                <h3>📈 プロセス（CPU上位）</h3>
                <ul>
                    {process_html}
                </ul>
            </div>
        </div>
    </div>
    """

def main():
    """メイン実行関数"""
    print("🐍 Python System Info Generator")
    print("=" * 40)
    
    # HTMLを更新
    success = update_html_with_data()
    
    if success:
        print("\n🚀 次のコマンドでサーバーを起動してください:")
        print("   python simple_server.py")
        print("\n🌐 ブラウザで確認:")
        print("   http://localhost:8000/")
    else:
        print("\n❌ HTML更新に失敗しました")

if __name__ == "__main__":
    main()