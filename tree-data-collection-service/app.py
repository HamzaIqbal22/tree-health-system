# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store received data in memory (for simplicity)
tree_data = []

# POST /collect: This allows us to send tree data (like soil moisture) to our service.
@app.route('/collect', methods=['POST'])
def collect_data():
    # Get the data from the request
    data = request.get_json()

    # Add it to our tree_data list
    tree_data.append(data)

    return jsonify({'message': 'Data received successfully!', 'data': data}), 201

# GET /data: This returns all collected data (so we can see what was sent).
@app.route('/data', methods=['GET'])
def get_data():
    # Return the collected data
    return jsonify({'tree_data': tree_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)