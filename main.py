from flask import Flask, render_template

app = Flask(__name__, static_url_path='/web/static', static_folder='/web/static', template_folder='web/templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 80, debug=True)
