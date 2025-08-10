# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime 
# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)

# class Todo(db.Model):
#     sno=db.Column(db.Integer,primary_key=True)
#     title= db.Column(db.String(200),nullable=False)
#     desc=db.Column(db.String(500),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)
#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"


# # @app.route('/',methods=['GET', 'POST'])
# # def hello_world():
# #     if request.method=='POST':
# #         title=request.form['title']
# #         desc=request.form['desc']
# #         todo=Todo(title=title,desc=desc)
# #     db.session.add(todo)
# #     db.session.commit()
# #     allTodo=Todo.query.all()
# #     # print(allTodo)
# #     return render_template('index.html',allTodo=allTodo)


# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         title = request.form['title']
#         desc = request.form['desc']
#         todo = Todo(title=title, desc=desc)
#         db.session.add(todo)
#         db.session.commit()

#     allTodo = Todo.query.all()
#     return render_template('index.html', allTodo=allTodo)


# @app.route('/show')
# def products():
#     allTodo=Todo.query.all()
#     print(allTodo)
#     return 'welcome to menu'

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

# # if __name__ == "__main__":
# #     with app.app_context():
# #         db.create_all()  # create tables if they don't exist
# #     app.run(debug=True, port=8000)







#------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect
# from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


# Home route - add and display todos
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


# Show route
@app.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'Todos printed in console'

@app.route('/update/<int:sno>' , methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)
    

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)