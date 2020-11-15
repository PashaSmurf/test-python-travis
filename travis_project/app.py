from flask import Flask

from travis_project.env_var import TEST_SECRET_2

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!' + TEST_SECRET_2


if __name__ == '__main__':
    app.run(port=8080)
