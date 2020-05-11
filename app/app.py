from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def kibun():
    return render_template('kibun.html', title='今日の気分')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)