from flask import Flask
from blueprints.account import account

app = Flask(__name__)

app.register_blueprint(account)


if __name__ == '__main__':
    app.run()
