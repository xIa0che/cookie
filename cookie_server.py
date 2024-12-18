from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# 确保存储目录存在
COOKIE_DIR = "cookies"
if not os.path.exists(COOKIE_DIR):
    os.makedirs(COOKIE_DIR)

@app.route('/upload_cookie', methods=['POST'])
def upload_cookie():
    try:
        data = request.json
        machine_id = data.get('machine_id')
        cookies = data.get('cookies')
        
        # 保存cookie，文件名包含机器ID和时间戳
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{COOKIE_DIR}/cookie_{machine_id}_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
            
        return jsonify({
            "status": "success",
            "message": f"Cookie saved from machine {machine_id}"
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 