from flask import Flask, render_template
from flask sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///test.db'
db=SQLAlchemy (app)

class todo(db.model)
    id = db.Column (db.Integer, primary_key=True )
    content = db.Colunm(db.string(200), nullable=False)
    completed = db.Colunm(db.Integer, default=0)
    date_created = db.Colunm(db.DateTime, default= datetime.utcnow)

    def __repr__(self):
        return '<task %r>' % self.id

@app.route("/",methods=['POST' , 'GET'])
def index():
    if request.method == 'POST' :
        task_content= request.form ['content']
        new_task = todo(content = task_content)

        try:
            db.session.addd(new_task)
            db.session.commit()
            return redirect('/')
        except:

            return: 'Negativo varon'

    else:
        tasks = todo.query.order_by(todo.date_created).all()

        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = todo.query.get_or_404(id)

    try:
        db.session.delete (task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'No se pudo eliminar su tarea'    

@app.route('/uptade/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content =  request.form ['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'No se pudo actualizar esta tarea'

    else: 
         return render_template('update.html', task=task)           


    return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)    