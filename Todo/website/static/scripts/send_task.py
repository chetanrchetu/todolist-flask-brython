from browser import document,alert,ajax,html,window
import json

def display_all_task(res):
    if res.status==200:
        data=res.json
        all_task=data['All_task']

        for i in all_task:
            div=html.DIV(id=i[0])
            

            checkbox=html.INPUT(type='checkbox',id=i[0])
            

            label=html.LABEL(i[1],id=i[0])
            

            cancel=html.BUTTON(id=i[0])
            


            div.classList.add('task-div-style')
            checkbox.classList.add('checkbox-style')
            label.classList.add('taskname-style')
            cancel.classList.add('cancel-button-style')


            checkbox.bind('click',change_css)
            cancel.bind('click',remove_task)


            div<=checkbox
            div<=label 
            div<=cancel 



            document['task-display-part']<=div 




def change_css(ev):
    id=ev.target.id
    checkbox=document[id].children[0]
    label=document[id].children[1]
    if checkbox.checked==True:
        label.classList.remove('uncheck-css')
        label.classList.add('check-css')
    else:
        label.classList.remove('check-css')
        label.classList.add('uncheck-css')


def remove_task_from_screen(res):
    if res.status==200:
        data=res.json
        document[data].remove()


def remove_task(ev):
    id_remove = ev.target.id
    id=json.dumps(id_remove)
    ajax.post(
        url='/',
        data=id,
        oncomplete=remove_task_from_screen,
        headers={"Content-type":'application/json','Operation':'remove_task'}
        
    )

def add_task_to_screen(res):
    if res.status==200:
        data=res.json 
        task=data['Task']
        id=data['id']

        if task is not None and id is not None:
            div=html.DIV(id=id)
            

            checkbox=html.INPUT(type='checkbox',id=id)
            

            label=html.LABEL(task,id=id)
            

            cancel=html.BUTTON(id=id)
            


            div.classList.add('task-div-style')
            checkbox.classList.add('checkbox-style')
            label.classList.add('taskname-style')
            cancel.classList.add('cancel-button-style')


            checkbox.bind('click',change_css)
            cancel.bind('click',remove_task)


            div<=checkbox
            div<=label 
            div<=cancel 



            document['task-display-part']<=div 

        document['Input-box'].value=''
    



def send_task_to_back(ev):

    task=document['Input-box'].value
    task=task.strip()
    if task!='':
        # id=len(document['task-display-part'].children)+1
        data={
    
            'task':task,
            # 'id':id
        }

        data=json.dumps(data)


        ajax.post(
            url='/',
            data=data,
            oncomplete=add_task_to_screen,
            headers={"Content-Type":'application/json','Operation':'Submit'}
        )



def clear_all_from_screen(res):
    if res.status==200:
        for i in document['task-display-part']:
            i.remove()

def clear_all(ev):
    ajax.post(
        url='/',
        oncomplete=clear_all_from_screen,
        headers={"Operation":'Clear'}
    )
    pass        


document['Submit-button'].bind('click',send_task_to_back)
document['Input-box'].bind('keypress',lambda ev:send_task_to_back(ev) if ev.key=='Enter' else None)

document['Clear-button'].bind('click',clear_all)

if window.performance.navigation.type==1:
    ajax.post(
        url='/',
        oncomplete=display_all_task,
        headers={"Operation":'Reloaded'}
    )
