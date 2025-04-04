from flask import Flask, jsonify, request, send_from_directory
import os
import glob

app = Flask(__name__, static_folder='H:/HTML', static_url_path='')

# ✅ HTML 파일이 저장된 기본 폴더
HTML_FOLDER = r'H:\HTML'

@app.route('/')
def home():
    return send_from_directory(HTML_FOLDER, 'index.html')

# ✅ 검색 기능 (검색 후 파일 리스트 반환)
@app.route('/search', methods=['GET'])
def search_html_files():
    search_term = request.args.get('query', '')
    if not search_term:
        return jsonify({"error": "검색어를 입력하세요."}), 400

    html_files = glob.glob(os.path.join(HTML_FOLDER, '**', '*.html'), recursive=True)
    results = []

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_term in content:
                relative_path = os.path.relpath(file, HTML_FOLDER).replace("\\", "/")
                
                # ✅ 경로에서 /static/ 제거하여 원래의 경로로 반환
                results.append({
                    "filename": os.path.basename(file),
                    "filepath": f"/{relative_path}"  # /static/이 아니라 바로 원래 경로를 사용
                })

    return jsonify({"results": results})

# ✅ Flask에서 HTML 파일 제공
@app.route('/<path:filename>')
def serve_html(filename):
    return send_from_directory(HTML_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
