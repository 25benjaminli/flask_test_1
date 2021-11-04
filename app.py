#flask vid: https://www.youtube.com/watch?v=Z1RJmh_OqeA
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stupid.db'

db = SQLAlchemy(app)

class Test(db.Model):
  id = db.Column(db.Integer, primary_key = True) #how you access each one
  content = db.Column(db.String(200), nullable = False)
  date_created = db.Column(db.DateTime, default = datetime.utcnow) #automated

  def __repr__(self):
    return '<Task %r>' % self.id
# num_rows_deleted = db.session.query(Test).delete()
# db.session.commit()

@app.route('/', methods = ['POST', 'GET'])
def index(): #automatically finds templates folder
    if request.method == "POST": #submit form
      task_content = request.form['content']
      new_task = Test(content = task_content)

      try: 
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
      except:
        return 'Issue adding task'
    else:
      tasks = Test.query.order_by(Test.date_created).all() # ordering by date_created
      return render_template('index.html', tasks = tasks)

  # print("hi, again")
  # i = 5
  # return render_template("index.html", i = i)
@app.route('/delete/<int:id>')
def delete(id):
  task_delete = Test.query.get_or_404(id)

  try:
    db.session.delete(task_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was a problem deleting the task'

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
  task = Test.query.get_or_404(id) #getting the task

  if request.method == 'POST':
    task.content = request.form['content']
    try:
      db.session.commit() #content is being set
      return redirect('/')
    except:
      return 'Issue updating'
  else:
    return render_template('update.html', task = task)


if __name__ == "__main__":
  print("ran")
  app.run(debug=True, port = '0.0.0.0')

