from flask import Flask, request, jsonify
from flask_cors import CORS
import os  # ← ADD THIS LINE!

app = Flask(__name__)
CORS(app)

@app.route('/lock', methods=['POST'])
def lock():
    data = request.get_json()
    value = data['value']
    print(f"\n🎯🎯🎯 RENDER GOT: {value} 🎯🎯🎯")  # Changed message
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 RENDER SERVER READY!")
    print("📡 https://your-app.onrender.com/lock")
    print("="*50 + "\n")
    # FIXED: Render requires 0.0.0.0 + PORT from environment
    port = int(os.environ.get('PORT', 5000))  # ← FIXED LINE 1!
    app.run(host='0.0.0.0', port=port, debug=True)  # ← FIXED LINE 2!