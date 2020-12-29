from flask import Flask,render_template,request,redirect,url_for

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

print(tasklists)