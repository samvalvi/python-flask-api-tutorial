from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "My first task", "done": False} ]

@app.route('/todos', methods=['GET','POST'])
def add_new_todo():
    """json_text = jsonify(todos)
    return json_text"""

    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)