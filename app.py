from flask import Flask, request, jsonify
from prediction import predictor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_url():
    return jsonify({"status":"Success"})

@app.route('/detect', methods=['POST'])
def detect_url():
    try:
        data = request.json
        if data and 'url' in data:
            url = data['url']
            result = predictor(url)
            if result == 0:
                return jsonify({"result": "No", "message": "The URL is not detected as malicious."})
            else:
                return jsonify({"result": "Yes", "message": "The URL is detected as malicious."})
        else:
            return jsonify({"error": "Invalid request data."}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
