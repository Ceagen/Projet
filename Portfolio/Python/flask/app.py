from flask import Flask, render_template, request, url_for, redirect, session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash
from functools import wraps
from lib import *

app = Flask(__name__)
app.secret_key = '0792040667693d1dd4354c0181e6877d6c83e17e26788393c4530ca7720f5c05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ceagen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # optional, silences warning
db = SQLAlchemy(app)  # initializes the database

class todo(db.Model):  # creating the columns for the database and specifying the data type
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return '<Task %r>' % self.id
    
def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Veuillez vous connecter.', 'warning')
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    return wrapper
    
#permet a celui qui est connecter d'avoir access sur chacune des templates
@app.context_processor
def inject_user():
    return {
        'user': {
            'is_logged_in':'user_id' in session,
            'username': session.get('username')
        }
    }

@app.route('/Authentification', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('password')
        user = getLogin(username)

        if user and check_password_hash(user['Pwd'], pwd):
            session['user_id'] = user['ID']
            session['username'] = user['Login']
            flash('Connecté avec succès !', 'success')
        else:
            flash('Identifiants invalides.', 'danger')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

#task manager options
@app.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/test')
        except Exception as e:
            print(f"{e}")
            return 'Task could not be added'
    else:
        tasks = todo.query.order_by(todo.date_created).all()
        return render_template('test.html', tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/test')
    except:
        return 'Your task could not be deleted'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/test')
        except:
            return "Task update couldn't be done"
    else:
        return render_template('update.html',task=task)

if __name__ == "__main__":
    app.run(debug=True)