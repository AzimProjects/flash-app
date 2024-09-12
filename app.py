from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        collection.insert_one(data)
        return jsonify({"message": "Data inserted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
