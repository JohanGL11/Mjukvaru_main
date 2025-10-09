from flask import Flask, request, jsonify
from collectionmanager import CollectionManager
from backupmanager import backup_manager

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"

collection_mgr = CollectionManager()
backup_mgr = backup_manager(collection_mgr)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
