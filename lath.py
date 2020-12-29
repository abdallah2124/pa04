from flask import Flask,render_template,request,redirect,url_for
from status import Status       # Remember to import status and priority from the provided files
from priority import Priority

#create flask app
app = Flask(__name__)


tasklists = {
    1: {
        "name": "Python list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            1,
            2,
            3
        ],
        "tags": ['python', 'programming', 'fullstack']
        },
    2: {
        "name": "Home list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            4,
            5
        ],
        "tags": ['python', 'programming', 'fullstack']
    }
}

# tasks

tasks = {
    1: {
        "name": "learn flask blueprints",
        "last_updated": "2020-04-23T18:25:43.511Z",
        "created_at": "2020-04-23T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Etiam sit amet massa nec urna hendrerit gravida et sed ipsum."
    },
    2: {
        "name": "learn Python enums",
        "last_updated": "2012-04-20T18:25:43.511Z",
        "created_at": "2012-04-20T18:25:43.511Z",
        "status": Status.IN_PROGRESS,
        "priority": Priority.MEDIUM,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    },
    3:  {
        "name": "revise OOP concepts",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Ut eget elit interdum neque faucibus viverra."
    },
    4:  {
        "name": "clean keyboard",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Donec fermentum lacus ultrices mauris pretium, sit amet placerat felis dictum."
    },
    5:  {
        "name": "water plants",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Nam imperdiet ligula quis ligula rhoncus, et vehicula sem consectetur."
    }
}

def new_task(k,name,priority):
    d={k:{"name":name,
          "last_updated":"last_update",
          "created_at": "created_at",
          "status":"status",
          "priority":priority,
          "description":"description"}}
    tasks.update(d)

def dell_task(k):
    tasks.pop(k)

def edit_task(k,name,status,priority,description):
    d={k:{"name":name,
          "last_updated":"last_update",
          "created_at": "created_at",
          "status":status,
          "priority":priority,
          "description":description}}
    tasks.update(d)





def new_list(k,name,last_update,created_at,lst):
    d={k:{"name": name,
        "last_updated": last_update,
        "created_at": created_at,
        "tasks": lst,
        "tags": ['python', 'programming', 'fullstack']}}
    tasklists.update(d)

print(tasklists)
lst=[1,2,3,4,5]
new_list(3,"laith","now","hasa",lst)
print(tasklists)

def dell_list(k):
    tasklists.pop(k)

dell_list(3)
print(tasklists)









#############################################################################################

@app.route('/')
def home():
    return render_template("index.html",t=tasklists ,new=url_for('new'))

@app.route('/new_task',methods = ['GET','POST'])
def new():
    if request.method == 'GET':
        return render_template('add_tk.html')
    else:
        k=request.form['k']
        s=int(k)
        name=request.form['name']
        last_update=(request.form['last_update'])
        created_at=(request.form['created_at'])
        lst=request.form['lst']
        lst1=[lst]
        new_list(s,name,last_update,created_at,lst1)
        return redirect(url_for('vew'))

@app.route('/vew')
def vew():
    return render_template('vew.html',t=tasklists)

@app.route('/dell',methods = ['GET','POST'])
def dell():
    if request.method == 'GET':
        return render_template('dell_tk.html')
    else:
        k=request.form['k']
        s=int(k)
        dell_list(s)

        return redirect(url_for('vew'))


@app.route('/taskss',methods = ['GET','POST'])
def taskss():
    if request.method == 'GET':
        return render_template('taskss.html',t=tasks)
    else:
        k=request.form['k']
        s=int(k)
        dell_list(s)

        return redirect(url_for('vew'))

@app.route('/n_t',methods = ['GET','POST'])
def n_t():
    if request.method == 'GET':
        return render_template('add_tasks.html')
    else:
        k=request.form['k']
        s=int(k)
        name=request.form['name']
        priority=(request.form['priority'])
        new_task(s,name,priority)
        return redirect(url_for('taskss'))

@app.route('/d_t',methods = ['GET','POST'])
def d_t():
    if request.method == 'GET':
        return render_template('dell_tasks.html')
    else:
        k=request.form['k']
        s=int(k)
        dell_task(s)

        return redirect(url_for('taskss'))


@app.route('/e_t',methods = ['GET','POST'])
def e_t():
    if request.method == 'GET':
        return render_template('edit_tasks.html')
    else:
        k=request.form['k']
        s=int(k)
        name=request.form['name']
        priority=(request.form['priority'])
        status=(request.form['status'])
        description=(request.form['description'])
        edit_task(s,name,status,priority,description)
        return redirect(url_for('taskss'))


print(tasklists)
