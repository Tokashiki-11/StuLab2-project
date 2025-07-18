from flask import Flask, render_template, request, redirect, url_for, session
from questions import questions

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_quiz():
    session['current'] = 0
    session['correct'] = 0
    return redirect(url_for('question'))

@app.route('/question')
def question():
    q_num = session.get('current', 0)
    if q_num >= len(questions):
        return redirect(url_for('score'))
    return render_template('question.html', q=questions[q_num])

@app.route('/answer', methods=['POST'])
def answer():
    selected = request.form['answer'] == 'True'
    q_num = session['current']
    correct_answer = questions[q_num]['answer']

    if selected == correct_answer:
        session['correct'] += 1
        result = True
    else:
        result = False

    explanation = questions[q_num]['explanation']
    session['current'] += 1

    return render_template('result.html', result=result, explanation=explanation)

@app.route('/score')
def score():
    correct = session.get('correct', 0)
    total = len(questions)
    percentage = int((correct / total) * 100)
    return render_template('score.html', correct=correct, total=total, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)