from flask import Blueprint,render_template,url_for,request,jsonify
from website import db 
from website.models import Taskdb

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        
        
        type_request=request.headers.get('Operation')

        if type_request=='Submit':
            data=request.json 
            
            task=data['task']

            

            code,task,id=add_to_db(task)
        
            return jsonify({'Task':task,'id':id}),code
        
        if type_request=='Clear':
            clear_db()

            return '200'

            
        

        if type_request=='remove_task':
            data=request.json
            id=data
            remove_this_task(id)

            return jsonify(str(id))
        

        if type_request=='Reloaded':
            all_task=get_all_task()

            return jsonify({"All_task":all_task})


        
            


        

        

        

        
        
        


        
        
        

        
    return render_template('todolist.html')


def remove_this_task(id):
    task_to_delete=db.session.query(Taskdb).get(id)
    db.session.delete(task_to_delete)
    db.session.commit()
def clear_db():
    db.session.query(Taskdb).delete()
    db.session.commit()

def add_to_db(task):
    
    if check_first(task):
        return 200,None,None
    
    new_task=Taskdb(task=task) 
    try:
        db.session.add(new_task)
        db.session.commit()

        id=len(db.session.query(Taskdb).all())

        return 200,task,id 
    
    except Exception as e:
        return 400,None,None




def check_first(task):
    if_not_present=db.session.query(Taskdb).filter_by(task=task).first()

    
    

    if if_not_present is not None:
        return True
    else:
        return False

def get_all_task():
    tasks_and_id=db.session.query(Taskdb).all()
    all_task=[]

    for i in tasks_and_id:
        all_task.append((i.id,i.task))

    return all_task
