from flask import Flask, render_template, request, redirect, url_for
from models import db, Number
import os

app = Flask(__name__)

# 設置數據庫
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'numbers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化數據庫
db.init_app(app)

# 確保在第一次運行時創建數據庫表
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        number = request.form.get('number')
        if number and number.isdigit():
            # 創建新的數字記錄
            new_number = Number(value=int(number))
            db.session.add(new_number)
            db.session.commit()
    
    # 獲取所有數字，按創建時間降序排序
    numbers = Number.query.order_by(Number.created_at.desc()).all()
    return render_template('index.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
