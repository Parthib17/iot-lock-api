from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/lock', methods=['POST'])
def lock():
    data = request.get_json()
    value = data['value']
    print(f"\n🎯🎯🎯 LAPTOP GOT: {value} 🎯🎯🎯")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 LOCALHOST SERVER STARTED!")
    print("📡 http://127.0.0.1:8000/lock")
    print("="*50 + "\n")
    app.run(host='127.0.0.1', port=8000, debug=True)