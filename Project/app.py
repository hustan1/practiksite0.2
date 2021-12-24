from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import defaultload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


@app.route('/',) # для отслеживания URL адреса
@app.route('/home',) # для отслеживания URL адреса
def index():
    return render_template("index.html")

# class Material(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(16), nullable=False)
#     intro = db.Column(db.String(16), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #когда выбирает объект на основе этого класса, то будет выдаваться сам объект и его идентификатор
        return 'Article $r' % self.id

@app.route('/about') 
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>') 
def user(name, id):
    return "User page: " + name + "-" + str(id)


@app.route('/create-article') 
def create_article():
    return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)
