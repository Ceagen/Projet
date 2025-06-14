from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
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

@app.route('/')
def index():
    return render_template('index.html')

#task manager options
@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/test')
        except:
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