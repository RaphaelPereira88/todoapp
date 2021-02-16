from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

                                            #create an app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:raphael@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

                                            # allows use of Flask database migrate commands to initialize, upgrade and downgrade migrations
migrate = Migrate(app, db)                  # links up Flask app and SQLAlchemy db instance

                                            # models to create and manage to add app functionality?
class Todo(db.Model):                       # to link to SQLAlchemy, class should inherit from db.model
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean, nullable=True)
  list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable= False )

                                            # to give useful debugging statements when objs are printed,
                                            # we can define __repr__ to return a to do with the id and desc

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

                                            # db.create_all() is no longer needed with migrationsd
                                            # sync up models with db using db.create_all
                                            #db.create_all()  # ensures tables are created for all models declared

                                            # create url and url handler on our server, by defining route that listens to todos/create

class Todolist(db.Model):
  __tablename__ = 'todolists'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  todos = db.relationship('Todo', backref='list', lazy =True)


@app.route('/todos/create', methods=['POST'])
def create_todo():
  error = False
  body = {}
  try:                                              #to get that field description
    description = request.get_json()['description'] # Json object  come back to us as a dictionary with key description
                                                    # use description to create new todo object
    todo = Todo(description=description, completed=False ) #create a todo and store it to our database
    db.session.add(todo)
    db.session.commit()
    body['id'] = todo.id
    body['completed'] = todo.completed
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
                                        # could be useful debugging statement, 
    print(sys.exc_info())               # but terminal may also raise error for you
  finally:
    db.session.close()
                                        # we'd now tell the controller what to render to the user, by
                                        # telling the view to re-direct to the index route & re-show the index pg
  if error:
    abort (400)
  else:
    return jsonify(body)                # to return an useful JSON object that includes that description
                                        #name of route handler that listens for change on the index route

@app.route('/todos/<todo_id>/set-completed', methods=['POST']) #to write <todo_id> he knows the set completed property and we aer able to use it as an argument
def set_completed_todo(todo_id):
  try:
    completed = request.get_json()['completed']
    print('completed', completed)
    todo = Todo.query.get(todo_id)
    todo.completed = completed
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('index'))     # that will wound up grabbing a fresh list of all the todo items and refreshing the page automatically


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
  try:
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
    return jsonify({ 'success': True })


@app.route('/lists/<list_id>')
def get_list_todos(list_id):
  return render_template('index.html', 
  data=Todo.query.filter_by(list_id = list_id).order_by('id').all()
  )



@app.route('/')
def index():
  return redirect(url_for('get_list_todos', list_id =1))
