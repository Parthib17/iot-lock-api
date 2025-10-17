from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Store the latest lock value
latest_value = None


@app.route('/lock', methods=['POST'])
def lock():
    global latest_value
    data = request.get_json()
    latest_value = data['value']  # Store the value
    print(f"\n🎯 RECEIVED FROM APP: {latest_value} 🎯")
    return jsonify({"status": "ok"})


@app.route('/lock', methods=['GET'])
def get_lock():
    """Raspberry Pi calls this to get the latest value"""
    print(f"\n🔍 RASPBERRY PI REQUESTED: {latest_value}")
    return jsonify({"value": latest_value})


@app.route('/lock/clear', methods=['POST'])
def clear_lock():
    """Optional: Clear the value after Pi processes it"""
    global latest_value
    latest_value = None
    return jsonify({"status": "cleared"})


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("🚀 RENDER SERVER READY!")
    print("📡 POST: https://iot-lock-api.onrender.com/lock")
    print("📡 GET:  https://iot-lock-api.onrender.com/lock")
    print("=" * 50 + "\n")

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)