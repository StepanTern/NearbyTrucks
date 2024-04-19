from flask import Flask, render_template

app = Flask(__name__)

tabs = {
    'index': 'Главная',
    'favourite': 'Избранное',
    'profile': 'Профиль',
    'admin': 'Админка',
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', tabs=tabs)


if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=True)
