from flask import Flask, render_template
from flask import request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

tasks =[]
app = Flask(__name__)

#Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    tasks = Task.query.all() #fetch all tasks from the database
    return render_template('index.html', tasks = tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task_text= request.form['task']
        new_task = Task(content=task_text)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_task.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/completed/<int:id>',methods=['POST'])
def completed(id):
    task= Task.query.get(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)

