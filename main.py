from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/users')
def user():
  userlist = []
  f = open("data/db.txt", "r")
  for line in f:
    user, *garbage = line.split(":")
    userlist.append(user)
  f.close()
  
  return render_template("users.html", userlist=userlist)

@app.route('/todo')
def todo():
  user = request.args.get("user")
  f = open("data/db.txt", "r")
  for line in f:
    thisuser, password, todolist = line.split(":")
    if thisuser == user:
      tdlist = todolist.split(",")
      # this is just debugging, don't need
      #for item in tdlist:
      #  todo, checkd = item.split("|")
      #  print(todo,checkd)
      #print(tdlist)
      break
  f.close()
  return render_template("todo.html", user=user, tdlist=tdlist)


@app.route('/save')
def save():
  save = request.args.get("")
  f = open("data/db.txt", "w")

@app.route('/delete')
def delete():
  print("yobro")
  user = request.args.get("user")
  f = open("data/db.txt", "r")
  allstuff = f.readlines()
  for line in allstuff:
    thisuser, password, todolist = line.split(":")
    if thisuser == user: #John, This is where it stops printing things after this!
      print("Hi")
      tdlist = todolist.split(",")
      for charcter in tdlist:
        n = tdlist.find(charcter)
        nnl = tdlist[n]
        print('hello world')
        print(nnl)
  return render_template("delete.html")
  
app.run(host='0.0.0.0', port=8000)