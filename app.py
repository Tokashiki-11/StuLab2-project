# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, Question, Admin

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# DB設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_quiz():
    session['current'] = 0
    session['correct'] = 0
    session['q_ids'] = [q.id for q in Question.query.all()]
    return redirect(url_for('question'))

@app.route('/question')
def question():
    q_num = session.get('current', 0)
    q_ids = session.get('q_ids', [])
    if q_num >= len(q_ids):
        return redirect(url_for('score'))

    q = Question.query.get(q_ids[q_num])
    return render_template('question.html', q=q)

@app.route('/answer', methods=['POST'])
def answer():
    selected = request.form['answer'] == 'True'
    q_num = session['current']
    q_ids = session['q_ids']
    q = Question.query.get(q_ids[q_num])

    if selected == q.answer:
        session['correct'] += 1
        result = True
    else:
        result = False

    session['current'] += 1
    return render_template('result.html', result=result, explanation=q.explanation)

@app.route('/score')
def score():
    correct = session.get('correct', 0)
    total = len(session.get('q_ids', []))
    percentage = int((correct / total) * 100) if total > 0 else 0
    return render_template('score.html', correct=correct, total=total, percentage=percentage)

# 管理者ログイン
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            session['admin'] = True
            return redirect(url_for('manage'))
        else:
            flash("ログイン失敗")
    return render_template('admin_login.html')

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

# 管理画面
@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        q = request.form['question']
        a = request.form['answer'] == 'True'
        exp = request.form['explanation']
        db.session.add(Question(question=q, answer=a, explanation=exp))
        db.session.commit()
        flash("問題を追加しました")

    questions = Question.query.all()
    return render_template('manage.html', questions=questions)

@app.route('/delete/<int:qid>')
def delete(qid):
    if not session.get('admin'):
        return redirect(url_for('admin_login'))

    q = Question.query.get_or_404(qid)
    db.session.delete(q)
    db.session.commit()
    flash("削除しました")
    return redirect(url_for('manage'))

if __name__ == '__main__':
    app.run()