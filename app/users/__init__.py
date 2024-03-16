from flask import Flask
from users import users_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(debug=True)