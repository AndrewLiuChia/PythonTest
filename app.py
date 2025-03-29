from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 存儲輸入的數字
numbers = []

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        number = request.form.get('number')
        if number and number.isdigit():
            numbers.append(int(number))
    return render_template('index.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
