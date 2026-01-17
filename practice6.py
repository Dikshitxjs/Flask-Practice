from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = flask (__name__)
app.config ['SQLALCHEMY_DSATABSE_URL'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

class Profile(db.model):
    id = db.column(db.integer, primary_key = True)
    f_name = db.column (db.string(20), unique = False , nullable = False)
    l_name = db.column(db.string(20), unique = False , nullable= Fasle)
    age = db.column (db.Integer , nullable = False)
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

