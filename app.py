from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
# import os
# load_dotenv()
# SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# class Professor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), nullable=False)
#     area = db.Column(db.String())
#
#     def __repr__(self):
#         return f'<Professor ID: {self.id} name: {self.name} >'
#
# db.create_all()


@app.route('/')
def index():
    # prof = Professor.query.all()
    prof = [
        { "name":'Albert' },
        { "name":'Camus' },
        { "name":'George' },
        { "name":'Diego' },
    ]
    return render_template('index.html', data=prof)

if __name__ == '__main__':
    app.run()
