from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import sys
import os
load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

app = Flask(__name__)

# Model
# ---------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# mpdel
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo ID: {self.id} name: {self.description} >'

db.create_all()



# Controllers
# ----------------------------------------------------------------

# INDEX
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

# POST
@app.route('/todos/create', methods=['POST'])
def create_todo():
    # Pattern Error Handling
    error = False

    # body is used to avoid
    # the error of access at db objects
    # after close the session.
    body = {}
    try:
        # desc = request.form.get('description') # synchronous
        desc = request.get_json()['description'] # asynchronous
        todo = Todo(description=desc)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        # return redirect(url_for('index')) # synchronous
        # return jsonify({
        #     'description': body
        # }) # asynchronous
        return jsonify(body) # asynchronous















# Access
if __name__ == '__main__':
    app.run()
