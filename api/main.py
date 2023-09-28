# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return "Hello, World!"

# main driver function
if __name__ == '__main__':

    app.run()


