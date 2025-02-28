from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/activate-ai', methods=['GET'])
def activate_ai():
    try:
        subprocess.run(['python', 'LobbyOfTheLost.py'], check=True)
        return jsonify(success=True)
    except subprocess.CalledProcessError as e:
        return jsonify(success=False, error=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
